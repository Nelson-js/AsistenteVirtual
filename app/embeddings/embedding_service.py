#Este modelo es ligero y funciona bien para un primer RAG. Más adelante podremos cambiarlo por otro si lo necesitas.
from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def generar(self, texto):

        return self.model.encode(texto).tolist()

        