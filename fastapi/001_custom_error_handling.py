from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()
subapp = FastAPI()


app.mount("/subapp", subapp)


class RequestModel(BaseModel):
    key: str


@app.post("/request-validation-error")
def request_validation_error(request_model: RequestModel):
    return {"key": request_model.key}


@subapp.post("/request-validation-error")
def subapp1_request_validation_error(request_model: RequestModel):
    return {"key": request_model.key}


@subapp.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, 
        content={"message": "error"}
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
        content={"detail": "error"}
    )


def test_exception_handler():
    with TestClient(app) as client:
        response = client.post("/request-validation-error", json={})
        assert response.status_code == 422
        assert response.json() == {"detail": "error"}


def test_subapp_exception_handler():
    with TestClient(app) as client:
        response = client.post("/subapp/request-validation-error", json={})
        assert response.status_code == 400
        assert response.json() == {"message": "error"}
