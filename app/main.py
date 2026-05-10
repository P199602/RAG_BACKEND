from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base

from app.routes.chat import router as chat_router
from app.routes.pdf import router as pdf_router


# Create DB Tables
Base.metadata.create_all(bind=engine)


# FastAPI App
app = FastAPI(
    title="AI Customer Support Bot"
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routers
app.include_router(chat_router)
app.include_router(pdf_router)


# Home Route
@app.get("/")
def home():

    return {
        "message": "AI Customer Support Bot Running"
    }