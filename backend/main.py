from fastapi import FastAPI
from starlette import status
from starlette.responses import Response

import requests

from models import Question, QuestionNum

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/")
def create_quiz(count: QuestionNum):
    url = "https://jservice.io/api/random?" + str(count)
    print(url)
    response = requests.get(url)
    print(response)
    return Response(status_code=status.HTTP_200_OK)