from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from deep_translator import GoogleTranslator

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TranslationRequest(BaseModel):
    text: str
    from_lang: str
    to_lang: str

@app.post("/translate/")
async def translate(request: TranslationRequest):
    try:
        translated = GoogleTranslator(
            source=request.from_lang,
            target=request.to_lang
        ).translate(request.text)
        return {"translated_text": translated}
    except Exception as e:
        return {"error": str(e)}

from fastapi.responses import FileResponse
import os

@app.get("/", response_class=FileResponse)
async def serve_index():
    return FileResponse(os.path.join("static", "index.html"))
