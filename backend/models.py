from datetime import date
from sqlalchemy import Column, Date, Integer, String

from database import Base


class Question(Base):
    __tablename__ = 'questions'

    ID = Column(Integer, primary_key=True, index=True)
    id = Column(Integer)
    answer = Column(String)
    question = Column(String)
    date = Column(Date, default=date.today)