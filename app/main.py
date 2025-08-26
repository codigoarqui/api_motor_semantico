from fastapi import FastAPI

from app.routes import busqueda, documentos, rag

app = FastAPI()

app.include_router(rag.router, prefix="/rag")
app.include_router(documentos.router, prefix="/documentos")
app.include_router(busqueda.router, prefix="/buscar")