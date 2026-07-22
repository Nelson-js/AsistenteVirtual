import requests

from app.core.config import OLLAMA_MODEL
from app.core.config import OLLAMA_URL


class OllamaService:

    def preguntar(self, prompt: str):

        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        return response.json()["response"]