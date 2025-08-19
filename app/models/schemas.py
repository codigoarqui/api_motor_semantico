from typing import Dict

from pydantic import BaseModel


class DocumentoRequest(BaseModel):
    texto: str
    metadatos: Dict = {}

class BusquedaRequest(BaseModel):
    consulta: str
    top_k: int = 3