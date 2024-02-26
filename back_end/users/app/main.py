from fastapi import FastAPI
import logging


def create_application() -> FastAPI:
    application = FastAPI(
        openapi_url="/users/openapi.json",
        docs_url="/users/docs")

    return application


app = create_application()
log = logging.getLogger("uvicorn")


@app.get('/')
async def index():
    return {"Real": "user"}

