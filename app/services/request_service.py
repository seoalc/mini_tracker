from fastapi import Request

def client_info(request: Request):
    client_ip = request.client.host
    user_agent = request.headers.get("User-Agent")
    referer = request.headers.get("Referer")
    return {"client_ip": client_ip, "user_agent": user_agent, "referer": referer}