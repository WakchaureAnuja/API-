from types import NoneType
from pydantic import BaseModel,validator
from typing import Optional

class CreateUpdateStudent(BaseModel):
    name:Optional[str]=None
    password:Optional[str]=None
    department:Optional[str]=None
    is_active:bool

    @validator('name')
    def valid_name(cls,v,values):
        assert v not in values, "name is required"
        assert 'password' not in values ,"passsword is required"
        return v

class AllStudent(BaseModel):
    name:Optional[str]=None
    password:Optional[str]=None
    department:Optional[str]=None
    is_active:bool

    class Config:
        orm_mode=True
