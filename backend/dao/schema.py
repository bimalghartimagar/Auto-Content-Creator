from pydantic import BaseModel
from typing import Optional


class ContentBase(BaseModel):
    title: str
    description: Optional[str] = None
    video_url: str
    audio_url: str


class ContentCreate(ContentBase):
    pass


class Content(ContentBase):
    id: int
    video_status: Optional[str] = None
    audio_status: Optional[str] = None

    class Config:
        orm_mode = True
