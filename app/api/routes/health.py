from fastapi import APIRouter
import requests

from app.core.config import OLLAMA_URL

router = APIRouter()


@router.get("/health")
def health():

    ollama = False

    try:

        r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)

        if r.status_code == 200:
            ollama = True

    except Exception:
        pass

    return {
        "status": "OK",
        "ollama": ollama
    }