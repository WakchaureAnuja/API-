from datetime import date
from database import Base
from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.orm import relationship


class Teacher(Base):
    __tablename__="teacher"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100))
    subject=Column(String(50))
    password=Column(String(50), unique=True)
    department=Column(String(100))
    is_active=Column(Boolean)
    