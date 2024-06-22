"""This file contains the models for request response in the api"""

from sqlmodel import SQLModel
from .geolocation import GeolocationBase


class BaseResponse(SQLModel):
    """The base attributes each response should contain"""
    reqId: str
    """The request id that was provided in the request"""
    ip: str
    """The caller id that was provided in the request"""


class GeolocationOut(GeolocationBase, BaseResponse):
    """The geolocation response from the api"""
    pass
