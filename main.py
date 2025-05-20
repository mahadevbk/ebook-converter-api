# main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os
import uuid

app = FastAPI()

@app.post("/convert/")
async def convert(file: UploadFile = File(...)):
    input_path = f"/tmp/{uuid.uuid4()}_{file.filename}"
    output_path = input_path + ".converted"  # adjust this!

    # Save uploaded file
    with open(input_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Here, call your actual conversion logic
    # For example:
    # your_converter.convert(input_path, output_path)

    # TEMP MOCK: just copy the input to output
    shutil.copy(input_path, output_path)

    return FileResponse(output_path, filename="converted.epub")

