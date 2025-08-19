from fastapi import FastAPI

from app.routes import busqueda, documentos

app = FastAPI()

app.include_router(documentos.router, prefix="/documentos")
app.include_router(busqueda.router, prefix="/buscar")