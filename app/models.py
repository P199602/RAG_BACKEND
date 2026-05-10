from sqlalchemy import Column, Integer, String, Text
from .database import Base

class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)
    user_message = Column(Text)
    bot_response = Column(Text)