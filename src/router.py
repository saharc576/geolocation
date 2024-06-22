
from fastapi import Query, APIRouter

from .models.req_res import GeolocationOut
from .service import get_geolocation_by_ip

router = APIRouter()

@router.get("/ip")
async def get_geolocation_ip_based(
    reqId: str = Query(..., description="The request id of the request to enrich"),
    ip_address: str = Query(..., description="The ip to query")
):
    """Get geolocation details based on the given ip"""
    geolocation = get_geolocation_by_ip(ip=ip_address)
    return GeolocationOut(
        **geolocation.dict(),
        ip=ip_address,
        reqId=reqId,
    )
