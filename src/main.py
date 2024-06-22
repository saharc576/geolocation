from fastapi import FastAPI, Request
from src.router import router as geolocation_enrichment
from config import settings as dynaconf_settings  
import traceback

app = FastAPI()
app.include_router(
    geolocation_enrichment,
    prefix="/location",
    tags=["location"],
)

@app.middleware("http")
async def middleware(
    request: Request,
    call_next
):
    try:
        response = await call_next(request)
    except Exception as e:
        print(f"Failed to make request to {request.url=}\n" + traceback.format_exc())
        raise
    return response


    """
    - Write points for the code
    """