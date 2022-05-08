from datetime import date
from pydantic import BaseModel


class QuestionNum(BaseModel):
    count: int


class Question(BaseModel):
    id: int
    text: str
    answer: str
    date: date