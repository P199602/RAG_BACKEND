from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import os
import shutil

from app.rag import save_pdf_to_db
from app.chatbot import chatbot_response

router = APIRouter()

UPLOAD_DIR = "app/uploads"


@router.post("/upload-pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    result = save_pdf_to_db(
        file_path,
        file.filename
    )

    return {
        "message": result
    }


@router.post("/chat")
async def chat(message: str):

    response = chatbot_response(message)

    return {
        "response": response
    }