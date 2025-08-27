from fastapi import APIRouter, HTTPException
from app.routes.busqueda import buscar_documentos
import google.generativeai as genai
from app.models.schemas import BusquedaRequest
from app.core.config import GEMINI_API_KEY

router = APIRouter()

genai.configure(api_key=GEMINI_API_KEY)

@router.post("/")
async def responder_con_rag(payload: BusquedaRequest):
    
    contexto_chunks = buscar_documentos(payload)

    contexto_str = "".join(chunk['texto'] for chunk in contexto_chunks['resultados'])

    prompt_template = f'''
    Basándote únicamente en el siguiente contexto, responde a la pregunta del usuario de la forma más clara y concisa posible.

    CONTEXTO:
    {contexto_str}

    PREGUNTA:
    {payload.consulta}

    RESPUESTA:
    '''

    model = genai.GenerativeModel('gemini-2.5-pro')
    respuesta_generada = model.generate_content(prompt_template)

    return {"respuesta": respuesta_generada.text}