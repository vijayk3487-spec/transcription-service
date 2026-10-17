from fastapi import FastAPI, UploadFile, File
from services.converter import convert_audio
from services.transcriber import transcribe_audio
import os
import shutil

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):

    input_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    wav_path = convert_audio(input_path)

    result = transcribe_audio(wav_path)

    return {
        "filename": file.filename,
        "segments": result
    }