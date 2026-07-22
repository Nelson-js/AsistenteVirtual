#Parser de documentos
#Crearemos un único parser que decida cómo leer cada archivo según su extensión.

#Luego añadiremos funciones para PDF, DOCX, PPTX y XLSX.
#No es necesario crear un parser distinto para cada formato; un único módulo puede encargarse de ello.


from pathlib import Path

from pypdf import PdfReader

from docx import Document


#Text Splitter
#Cada documento debe dividirse en fragmentos antes de generar embeddings.

from langchain_text_splitters import RecursiveCharacterTextSplitter


splitter = RecursiveCharacterTextSplitter(

    chunk_size=800,

    chunk_overlap=150
)

#Cada PDF producirá varios fragmentos, lo que mejora la recuperación semántica.