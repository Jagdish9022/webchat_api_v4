from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(UserBase):
    id: str
    created_at: datetime
    is_active: bool = True

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[str] = None

class QARequest(BaseModel):
    question: str
    collection_name: str

class Conversation(BaseModel):
    id: str
    collection_name: str
    messages: List[Dict[str, str]]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# New models for multi-chatbot support
class ScrapeRequest(BaseModel):
    url: str
    collection_name: str  # Now required from frontend
    chatbot_name: Optional[str] = None  # Optional chatbot display name

class ChatbotCreate(BaseModel):
    name: str
    description: Optional[str] = None
    collection_name: str
    source_url: Optional[str] = None

class ChatbotInfo(BaseModel):
    id: str
    user_id: str
    name: str
    description: Optional[str] = None
    collection_name: str
    source_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    is_active: bool = True

class FileUploadRequest(BaseModel):
    collection_name: str  # Now required from frontend

class UserChatbotsResponse(BaseModel):
    chatbots: List[ChatbotInfo]
    total_count: int
