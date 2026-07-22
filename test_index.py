from app.services.index_service import IndexService

index = IndexService()

resultado = index.indexar_archivo(
    "app/documents/manual.pdf"
)

print(resultado)