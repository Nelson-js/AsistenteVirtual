#Parser de documentos
#Crearemos un único parser que decida cómo leer cada archivo según su extensión.

#Luego añadiremos funciones para PDF, DOCX, PPTX y XLSX.
#No es necesario crear un parser distinto para cada formato; un único módulo puede encargarse de ello.


from pypdf import PdfReader

from docx import Document



class DocumentParser:



    def leer_pdf(
        self,
        archivo
    ):


        reader = PdfReader(
            archivo
        )


        texto=""


        for pagina in reader.pages:

            texto += pagina.extract_text()



        return texto



    def leer_docx(
        self,
        archivo
    ):


        doc = Document(
            archivo
        )


        texto=""


        for parrafo in doc.paragraphs:

            texto += parrafo.text + "\n"



        return texto



    def leer(
        self,
        archivo
    ):


        if archivo.endswith(".pdf"):

            return self.leer_pdf(
                archivo
            )


        if archivo.endswith(".docx"):

            return self.leer_docx(
                archivo
            )


        return ""

#Cada PDF producirá varios fragmentos, lo que mejora la recuperación semántica.