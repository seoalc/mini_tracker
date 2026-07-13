import uuid

def offer_destination_url(offer: int):
    click_id = uuid.uuid4()
    destination_url = f"http://127.0.0.1:8000/landing?click_id={click_id}&offer={offer}"
    return str(click_id), destination_url