from fastapi import FastAPI

from app.routes import busqueda, documentos, rag, rag_memory, rag_re_ranker

app = FastAPI()

app.include_router(rag.router, prefix="/rag")
app.include_router(rag_memory.router, prefix="/rag_memory")
app.include_router(rag_re_ranker.router, prefix="/rag_re_ranker")
app.include_router(documentos.router, prefix="/documentos")
app.include_router(busqueda.router, prefix="/buscar")