from app.services.ollama_service import OllamaService
from app.services.rag_service import RAGService


class ChatService:

    def __init__(self):

        self.ollama = OllamaService()
        self.rag = RAGService()

    def responder(self, pregunta: str):

        contexto = self.rag.obtener_contexto(pregunta)

        prompt = f"""
Eres un asistente virtual para Moodle.

Responde únicamente utilizando el siguiente contexto.

Si el contexto no contiene la respuesta, responde:

"No encontré esa información en el curso."

============================
CONTEXTO
============================

{contexto}

============================
PREGUNTA
============================

{pregunta}

============================
RESPUESTA
============================
"""

        return self.ollama.preguntar(prompt)