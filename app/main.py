from fastapi import FastAPI

from app.api.router import router

from app.core.config import APP_NAME
from app.core.config import VERSION

app = FastAPI(

    title=APP_NAME,

    version=VERSION
)

app.include_router(router)