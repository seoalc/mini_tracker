from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from app.services.routing_service import offer_destination_url
from app.services.request_service import client_info

router = APIRouter()

@router.get("/click")
async def click(request: Request,offer: int):
    destination_url = offer_destination_url(offer)

    client_data = client_info(request)
    return {"message": "Click registered", "offer": offer, "destination_url": destination_url, **client_data}

    # return RedirectResponse(url=destination_url, status_code=302)

@router.get("/landing")
async def landing(click_id: str, offer: int):
    return {"message": "Landing page", "click_id": click_id, "offer": offer}