from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from models.student import Student
from apps.student.schemas import *

def create_student(Config : CreateUpdateStudent, db:Session):
    student = Student(
        name=Config.name,
        password=Config.password,
        department=Config.department,
        is_active=Config.is_active
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def update_student(AS:AllStudent, Config : CreateUpdateStudent, db:Session):
    AS.name=Config.name
    AS.password=Config.password
    AS.department=Config.department
    AS.is_active=Config.is_active
    db.commit()
    db.refresh(AS)
    return AS

def get_by_id(id:int, db:Session):
    result=db.query(Student).filter(Student.id==id).first()
    if result:
        return result

def get_by_name(name:str, db:Session):
    result=db.query(Student).filter(Student.name==name).first()
    return result

def all_student(db:Session):
    result=db.query(Student).all()
    return result

def active_student(db:Session):
    result=db.query(Student).filter(Student.is_active==True).first()
    return result