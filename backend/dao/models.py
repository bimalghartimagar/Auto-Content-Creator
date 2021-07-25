from sqlalchemy import Column, Integer, String

from backend.dao.database import Base


class Content(Base):
    __tablename__ = "content"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    video_url = Column(String)
    audio_url = Column(String)
    video_status = Column(String)
    audio_status = Column(String)
