from pydantic import BaseModel, HttpUrl, Field
from datetime import datetime
from typing import Optional


class URLCreate(BaseModel):
    """What client sends when creating short url"""
    original_url: HttpUrl


class URLPublic(BaseModel):
    """What we return to client"""
    short_url: str          # full url like http://localhost:8000/abc123
    original_url: str
    short_code: str
    created_at: datetime
    clicks: int = 0


class URLStats(URLPublic):
    """Extended info for stats page/endpoint"""
    last_clicked: Optional[datetime] = None