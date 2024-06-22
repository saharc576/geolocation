"""This file contains service functions for the geolocation service"""
from typing import Optional, Union
from config import settings
from libs.redis import RedisClient
from .models.req_res import GeolocationBase
from src.models.geolocation import *

# Union for all possible provider types
GEO_PROVIDER_TYPE = Union[IpApiGeolocationProvider]


def _factory(name: str) -> GEO_PROVIDER_TYPE:
    """
    Get he geolocation which name is the given name
    :raise ValueError: if there is no such geolocation provider
    """
    for subclass in GeolocationProvider.__subclasses__():
        if subclass().name == name:
            return subclass()
        
    raise ValueError(f"No geolocation provider found with name '{name}'")


def _get_geolocation_provider() -> GeolocationProvider:
    """:returns The geolocation provider to use. Determined by settings"""
    name = settings["geolocation_provider"]
    return _factory(name=name)


def _get_cached_geolocation(ip: str) -> Optional[GeolocationBase]:
    """
    Check for cache hits in redis before pulling the data from external sources.
    :return: The cached geolocation if cached, else None.
    """
    client = RedisClient()
    geolocation = client.get_value(ip)
    if geolocation is None:
        return None
    
    return GeolocationBase(**geolocation)


def _cache_geolocation(ip: str, geolocation: GeolocationBase):
    """Cache the geolocation for the given ip."""
    client = RedisClient()
    client.set_value(ip, geolocation.dict())


def get_geolocation_by_ip(ip: str) -> GeolocationBase:
    """
    :param ip: The ip to get the geolocation for
    .. note::
        This function uses the relevant provider defined in settings.
    :return: The current geolocation based on the given ip
    """
    cached_geolocation = _get_cached_geolocation(ip=ip)
    if cached_geolocation is not None:
        return cached_geolocation
        
    geolocation_provider = _get_geolocation_provider()
    geolocation = geolocation_provider.get_geolocation(ip=ip)
    
    # Cache the geolocation for this ip
    _cache_geolocation(ip=ip, geolocation=geolocation)
    
    return geolocation