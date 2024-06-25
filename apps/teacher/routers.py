from ctypes.wintypes import HACCEL
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Request, Depends, HTTPException, status, Header
from fastapi.responses import JSONResponse
from sqlalchemy import and_
from sqlalchemy.orm import Session
from database import get_db
from models.teacher import *
import apps.teacher.crud as crud
import apps.teacher.schemas as schemas

router = APIRouter(
	prefix="/V1/Teacher",
	tags=['Teacher API'] ,
	)

@router.post("/teacher/")
async def create_teacher(Config:schemas.CreateUpdateTeacher, db: Session = Depends(get_db)):
    duplicacy_check=db.query(Teacher).filter(and_(Teacher.name==Config.name, Teacher.password==Config.password, Teacher.subject==Config.subject, Teacher.department==Config.department, Teacher.is_active==Config.is_active))
    if duplicacy_check.count() > 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="teacher with provided data already exists")
    try:
        result=crud.create_teacher(Config, db)
        return JSONResponse(status_code=201, content={"msg":f"Teacher create successfully"})
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="teacher already exists with same data")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))



@router.put("/teacher/")
async def update_teacher(id:int, Config:schemas.CreateUpdateTeacher, db:Session=Depends(get_db)):
    result=crud.get_by_id(id,db)
    if not result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="entered id is invalid")
    duplicacy_check=db.query(Teacher).filter(and_(Teacher.name==Config.name, Teacher.password==Config.password, Teacher.subject==Config.subject, Teacher.department==Config.department, Teacher.is_active==Config.is_active))
    if duplicacy_check.count() > 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="teacher with provided data already exists")
    try:
        result=crud.update_teacher(result,Config,db)
        return JSONResponse(status_code=201, content={"msg":f"teacher update successfully"})
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="teacher already exists with same data")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.get("/active_teachers")
async def active_teachers(db:Session=Depends(get_db)):
    result=crud.active_teachers(db)
    if result:
        return result


@router.get("/teacher")
async def all_teachers(db:Session=Depends(get_db)):
    result=crud.all_teachers(db)
    if result:
        return result


'''
@router.get("/teacher/")
async def get_by_id(id:int, db:Session=Depends(get_db)):
    result=crud.get_by_id(id,db)
    if result:
        return result


@router.put("/AT/teacher/")
async def update_teacher(id:int, Config:schemas.CreateUpdateTeacher, db:Session=Depends(get_db)):
    result= crud.get_by_id(id,db)
    if not result:
        raise HTTPException(status_code=404, content={"msg":f"enter teacher id is not in database"})
    sample=crud.get_by_name(Config.name,db)
    if sample:
        return JSONResponse(status_code=201, content={"msg":f"entered Teacher name already in database"})
    try:
        result=crud.update_teacher(result,Config,db)
        return JSONResponse(status_code=201, content={"msg":f"Teacher update successfully"})
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
'''