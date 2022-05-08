from pydantic import BaseModel


class Count(BaseModel):
    count: int


class QuestionBase(BaseModel):
    id: int
    answer: str
    question: str

    class Config:
        orm_mode = True