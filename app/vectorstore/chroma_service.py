import chromadb

from app.core.config import CHROMA_PATH


class ChromaService:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=CHROMA_PATH
        )

        self.collection = self.client.get_or_create_collection(
            name="moodle_course"
        )


    # Método para insertar documentos
    def agregar(self, id_documento, texto, embedding, metadata):

        self.collection.add(

            ids=[id_documento],

            documents=[texto],

            embeddings=[embedding],

            metadatas=[metadata]
        )


    # Método para buscar documentos similares
    def buscar(self, embedding, cantidad=5):

        return self.collection.query(

            query_embeddings=[embedding],

            n_results=cantidad
        )