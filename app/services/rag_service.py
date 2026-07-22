class RAGService:

    def obtener_contexto(self, pregunta: str) -> str:

        return """
Este asistente responde únicamente utilizando la información del curso Moodle.

Actualmente esta respuesta proviene del servicio RAG de prueba.
"""

#Por ahora será un "mock". Más adelante leerá ChromaDB.