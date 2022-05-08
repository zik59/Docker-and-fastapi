from datetime import date
import json
from fastapi import FastAPI, Depends
from fastapi_sqlalchemy import db
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import Response

import requests

from models import Question
from schemas import Count, QuestionBase
from database import SessionLocal, engine


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/", response_model=QuestionBase)
def create_quiz(count: Count, db:Session = Depends(get_db)):
    url = "https://jservice.io/api/random?" + str(count)
    response = requests.get(url)
    questions = json.loads(response.text)
    print(questions)
    for q in questions:
        if q['id'] in db.query(Question.id):
            response = requests.get("https://jservice.io/api/random?count=1")
            questions.update(json.loads(response))
        db_question = Question(id=q["id"], answer=q["answer"], question=q["question"])
        print(db_question)
        db.add(db_question)
        db.commit()
    return db_question