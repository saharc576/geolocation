from abc import ABC, abstractmethod
from requests import Response, request
from typing_extensions import override
import pydantic


class GeolocationBase(pydantic.BaseModel):
    """The geolocation response from the api"""
    countryCode: str
    lat: float
    lon: float
    
    class Config:
        # Make the class ignore all given key-value pairs that are not class members
        extra = "ignore"
    

class GeolocationProvider(ABC):
    """Geolocation provider base class"""
    
    @property
    @abstractmethod
    def base_url(self):
        """:return: The provider's base url"""
        pass

    @property
    @abstractmethod
    def name(self):
        """:return: The provider's name"""
        pass
    
    @abstractmethod
    def _request(self, ip: str) -> Response:
        pass
        
    @abstractmethod
    def _parse_geolocation(self, response: Response) -> GeolocationBase:
        """:returns The parsed geolocation object from the response"""    
        pass
    
    def get_geolocation(self, ip: str) -> GeolocationBase:
        """Get the geolocation based on ip"""
        res = self._request(ip=ip)
        return self._parse_geolocation(response=res)


class IpApiGeolocationProvider(GeolocationProvider):
    
    @property
    @override
    def base_url(self) -> str:
        return "http://ip-api.com/json"

    @property
    @override
    def name(self):
        return "IP_API"
    
    @override
    def _request(self, ip: str) -> Response:
        req_url = self._build_req_url(ip=ip)
        return request("GET", req_url)
    
    def _build_req_url(self, ip: str) -> str:
        """:return: The request url with the ip to query for"""
        return f"{self.base_url}/{ip}"
        
    @override
    def _parse_geolocation(self, response: Response) -> GeolocationBase:
        """:returns The parsed geolocation object from the response"""    
        return GeolocationBase(**response.json())
