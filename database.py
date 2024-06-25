
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy

sqlalchemy.url ="mysql://root@localhost:3306/student_db"

engine = create_engine(sqlalchemy.url)

Base=declarative_base()
SessionLocal=sessionmaker(autocommit=False, bind=engine)

Base.metadata.create_all(bind=engine)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

