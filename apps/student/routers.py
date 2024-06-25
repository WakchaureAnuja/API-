from email.policy import HTTP
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Request, Depends, HTTPException, status, Header
from fastapi.responses import JSONResponse
from sqlalchemy import and_
from sqlalchemy.orm import Session
from database import get_db
from models.student import *
import apps.student.crud as crud
import apps.student.schemas as schemas

router = APIRouter(
	prefix="/V1/student",
	tags=['Student API'] ,
	)

@router.post("/student/")
async def create_student(Config:schemas.CreateUpdateStudent, db: Session = Depends(get_db)):
    duplicacy_check=db.query(Student).filter(and_(Student.name==Config.name, Student.password==Config.password, Student.department==Config.department,Student.is_active==Config.is_active))
    if duplicacy_check.count() > 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="student with provided data already exists")
    try:
        result=crud.create_student(Config, db)
        return JSONResponse(status_code=201, content={"msg":f"student create successfully"})
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="student already exists with same data")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/student/")
async def update_student(id:int, Config:schemas.CreateUpdateStudent, db:Session=Depends(get_db)):
    result=crud.get_by_id(id,db)
    if not result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="entered id is invalid")

    duplicacy_check=db.query(Student).filter(and_(Student.name==Config.name, Student.password==Config.password, Student.department==Config.department,Student.is_active==Config.is_active))
    if duplicacy_check.count() > 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="student with provided data already exists")
    try:
        result=crud.update_student(result,Config,db)
        return JSONResponse(status_code=201, content={"msg":f"student update successfully"})
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="student already exists with same data")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
        

@router.get("/allstudent/")
async def all_student(db:Session=Depends(get_db)):
    result=crud.all_student(db)
    if result:
        return result

@router.get("/student")
async def active_student(db:Session=Depends(get_db)):
    result=crud.active_student(db)
    if result:
        return result


'''
@router.get("/student/")
async def get_by_id(id:int, db:Session=Depends(get_db)):
    result=crud.get_by_id(id,db)
    if result:
        return result
        
@router.put("/AS/student/")
async def update_student(id:int, Config:schemas.CreateUpdateStudent, db:Session=Depends(get_db)):
    result=crud.get_by_id(id,db)
    if  not result:
        raise HTTPException(status_code=404, content={"msg":f"entered student id not in database"})

    sample=crud.get_by_name(Config.name,db)
    if sample:
        return JSONResponse(status_code=201, content={"msg":f"entered student name already in database"})
    try:
        result=crud.update_student(result,Config,db)
        return JSONResponse(status_code=201, content={"msg":f"student update successfully"})
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
'''