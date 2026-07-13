from fastapi import Request

def client_info(request: Request):
    ip_address = request.client.host
    user_agent = request.headers.get("User-Agent")
    referer = request.headers.get("Referer")
    return {"ip_address": ip_address, "user_agent": user_agent, "referer": referer}