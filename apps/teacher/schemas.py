
from pydantic import BaseModel,validator
from typing import Optional

class CreateUpdateTeacher(BaseModel):
    name:str
    password:str
    subject:str
    department:str
    is_active:bool

    @validator("name", always=True)
    def valid_name(cls,v):
        if str(v)== "":
            raise ValueError(f'Invalid name::{v}')
        return v

class AllTeacher(BaseModel):
    name:str
    password:str
    subject:str
    department:str
    is_active:bool

    class Config:
        orm_mode=True
