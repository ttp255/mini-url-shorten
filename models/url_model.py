from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field,field_validator


class URLDocument(BaseModel):
    """MongoDB document structure"""
    
    original_url: str
    short_code: str
    created_at: datetime = datetime.now()
    clicks: int = 0
    last_clicked: Optional[datetime] = None 

    # @field_validator('id', mode='before')
    # @classmethod
    # def convert_objectid_to_str(cls, v):
    #     if hasattr(v, '__str__'):  # Works for ObjectId
    #         return str(v)
    #     return v