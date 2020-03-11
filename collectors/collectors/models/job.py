import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Float, Text, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm.session import Session
from .config import engine
 
Base = declarative_base()

def create_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def close_session(session):
    if session is not None:
        session.close()

def create_schema(clear):
    if clear:
        print('dropping database schema...')
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

class JobPost(Base):
    __tablename__ = 'job_post'
    id = Column(Integer, primary_key=True)
    title = Column(String(500), nullable=False)
    company = Column(String(100), nullable=False)
    location = Column(String(150), nullable=False)
    description = Column(Text, nullable=False)
    source = Column(String(50), nullable=False)


class CompReview(Base):
    __tablename__ = 'comp_review'
    id = Column(Integer, primary_key=True)
    company = Column(String(500), nullable=False)
    title = Column(String(500), nullable=False)
    rating = Column(String(5), nullable=False)
    author = Column(String(100), nullable=False)
    author_status = Column(String(100), nullable=False)
    location = Column(String(150), nullable=False)
    date = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    source = Column(String(50), nullable=False)



class TitleInterview(Base):
    __tablename__ = 'title_interview'
    id = Column(Integer, primary_key=True)
    company = Column(String(500), nullable=False)
    title = Column(String(500), nullable=False)
    question = Column(String(500), nullable=False)
    date = Column(String(50), nullable=False)
    source = Column(String(50), nullable=False)
