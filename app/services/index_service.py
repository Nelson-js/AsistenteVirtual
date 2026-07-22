#Este servicio coordinará todo el proceso.
#Este será el cerebro del proceso.

import uuid


from app.documents.parser import DocumentParser

from app.documents.splitter import TextSplitter

from app.embeddings.embedding_service import EmbeddingService

from app.vectorstore.chroma_service import ChromaService



class IndexService:


    def __init__(self):

        self.parser = DocumentParser()

        self.splitter = TextSplitter()

        self.embedding = EmbeddingService()

        self.chroma = ChromaService()



    def indexar_archivo(
        self,
        archivo
    ):


        texto = self.parser.leer(
            archivo
        )


        fragmentos = self.splitter.dividir(
            texto
        )


        for fragmento in fragmentos:


            vector = self.embedding.generar(
                fragmento
            )


            self.chroma.agregar(

                str(uuid.uuid4()),

                fragmento,

                vector,

                {
                    "archivo":archivo
                }

            )


        return {

            "archivo":archivo,

            "fragmentos":len(fragmentos)

        }