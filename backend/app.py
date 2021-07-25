from sqlalchemy.orm.session import Session
from fastapi import FastAPI, Depends
from typing import List

from backend.dao import crud, schema, models
from backend.dao.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/contents', response_model=List[schema.Content])
def contents(db: Session = Depends(get_db)):
    return crud.get_contents(db)


@app.get('/content/{content_id}', response_model=schema.Content)
def content(content_id: int, db: Session = Depends(get_db)):
    return crud.get_content(db, content_id)


@app.post('/content', response_model=schema.Content)
def content_create(content: schema.ContentCreate, db: Session = Depends(get_db)):
    return crud.create_content(db, content)
