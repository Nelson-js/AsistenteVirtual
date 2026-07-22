from fastapi import APIRouter

from app.models.request import ChatRequest
from app.models.response import ChatResponse

from app.services.chat_service import ChatService

router = APIRouter()

service = ChatService()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    respuesta = service.responder(request.pregunta)

    return ChatResponse(
        respuesta=respuesta
    )
    