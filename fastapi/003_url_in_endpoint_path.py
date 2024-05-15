from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

app = FastAPI()


@app.get("/path/{external_path:path}/end")
async def external_path_ep(external_path: str):
    return {"external_path": external_path}


@app.get("/string/{external_path}/end")
async def external_path_str(external_path: str):
    return {"external_path": external_path}


@pytest.mark.parametrize(
    "path, status_code", [
        ("/path/some/end", 200),
        ("/path/some/other/end", 200),
        ("/string/some/end", 200),
        ("/string/some/other/end", 404),
    ]
)
def test_get(path, status_code):
    with TestClient(app) as client:
        response = client.get(path)
        assert response.status_code == status_code
