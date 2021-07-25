from sqlalchemy.sql.expression import desc
from sqlalchemy.orm import Session
from backend.dao import models, schema


def create_content(db: Session, content: schema.ContentCreate):
    db_content = models.Content(
        title=content.title,
        description=content.description,
        video_url=content.video_url,
        audio_url=content.audio_url)
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content


def get_contents(db: Session):
    return db.query(models.Content).all()


def get_content(db: Session, id: int):
    return db.query(models.Content).filter(models.Content.id == id).first()
