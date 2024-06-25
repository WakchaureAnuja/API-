from datetime import date
from enum import unique
from database import Base
from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.orm import relationship


class Student(Base):
    __tablename__="student"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100))
    password=Column(String(50), unique=True)
    department=Column(String(100))
    is_active=Column(Boolean)
    