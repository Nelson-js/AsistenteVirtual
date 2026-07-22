from app.embeddings.embedding_service import EmbeddingService
from app.vectorstore.chroma_service import ChromaService


class RAGService:

    def __init__(self):

        self.embedding = EmbeddingService()

        self.chroma = ChromaService()

    def obtener_contexto(self, pregunta):

        vector = self.embedding.generar(
            pregunta
        )

        resultado = self.chroma.buscar(vector)

        documentos = resultado["documents"][0]

        return "\n\n".join(documentos)