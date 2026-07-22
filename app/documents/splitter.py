from langchain_text_splitters import RecursiveCharacterTextSplitter



class TextSplitter:


    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(

            chunk_size=800,

            chunk_overlap=150

        )


    def dividir(
        self,
        texto
    ):


        return self.splitter.split_text(
            texto
        )