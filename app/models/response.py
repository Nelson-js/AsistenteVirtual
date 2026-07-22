from pydantic import BaseModel

class ChatResponse(BaseModel):
    respuesta: str