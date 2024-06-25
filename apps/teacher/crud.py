from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from models.teacher import Teacher
from apps.teacher.schemas import *

def create_teacher(Config : CreateUpdateTeacher, db:Session):
    teacher = Teacher(
        name=Config.name,
        password=Config.password,
        subject=Config.subject,
        department=Config.department,
        is_active=Config.is_active
    )
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher

def update_teacher(AS:AllTeacher, Config : CreateUpdateTeacher, db:Session):
    AS.name=Config.name
    AS.password=Config.password
    AS.subject=Config.subject
    AS.department=Config.department
    AS.is_active=Config.is_active
    db.commit()
    db.refresh(AS)
    return AS

def get_by_id(id:int, db:Session):
    result=db.query(Teacher).filter(Teacher.id==id).first()
    return result

def get_by_name(name:str, db:Session):
    result=db.query(Teacher).filter(Teacher.name==name).first()
    return result

def all_teachers(db:Session):
    result=db.query(Teacher).all()
    return result
    
def active_teachers(db:Session):
    result=db.query(Teacher).filter(Teacher.is_active==True).all()
    return result