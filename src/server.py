from fastapi import FastAPI, Request
from pydantic import BaseModel
from src.proxy import Proxy

app = FastAPI()
proxy = Proxy()

class ProxyRequest(BaseModel):
    user_id: str
    message: str

@app.post("/proxy")
async def handle_proxy(req: ProxyRequest):
    result = proxy.handle_request(req.dict())
    return result
