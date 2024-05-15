from fastapi import FastAPI
import httpx
from pydantic import BaseModel
import pytest
import respx

app = FastAPI()

class Payload(BaseModel):
    message: str

class Result(BaseModel):
    status: str
    data: dict

@app.post("/call")
async def call():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://external-api.com", 
            json=Payload(message="hello").model_dump()
        )
    result = Result(**response.json())
    return  {"status": "success", "data": result.model_dump()}

@pytest.mark.asyncio
async def test_external_call(respx_mock: respx.Router):
    respx_mock.post(
        "http://external-api.com", json={"message":"hello"}
    ).mock(
        return_value=httpx.Response(
            200, json={"status": "ok", "data": {}}
        )
    )
    
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), 
        base_url="http://testserver/"
    ) as client:
        response = await client.post("/call")
        
    assert response.status_code == 200
    assert response.json() ==  {
        "status": "success",
        "data": {"status": "ok", "data": {}},
    }
