from fastapi import FastAPI,Depends,Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List,Optional
from database import Base,SessionLocal,engine
from apps.student.routers import router as student_router
from apps.teacher.routers import router as teacher_router

app = FastAPI()



app.add_middleware(
	CORSMiddleware,
	allow_credentials=["*"],
	allow_headers=["*"],
	)


app.include_router(student_router)

app.include_router(teacher_router)


