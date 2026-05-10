from fastapi import APIRouter
import os

router = APIRouter()

UPLOAD_DIR = "app/uploads"


@router.get("/pdfs")
def get_pdfs():

    files = os.listdir(UPLOAD_DIR)

    return {
        "pdfs": files
    }

from langchain_chroma import Chroma
from app.rag import embeddings


@router.delete("/delete-pdf/{filename}")
def delete_pdf(filename: str):

    file_path = os.path.join(
        UPLOAD_DIR,
        filename
    )

    if os.path.exists(file_path):
        os.remove(file_path)

    vectorstore = Chroma(
        persist_directory="app/chroma_db",
        embedding_function=embeddings,
        collection_name="pdf_collection"
    )

    vectorstore.delete(
        where={"source": filename}
    )

    return {
        "message": "PDF Deleted Successfully"
    }