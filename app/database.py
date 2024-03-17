import os
from sqlmodel import SQLModel, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# get the database url from the environment
print(os.getenv("DATABASE_URL"))
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create a base class for our models
Base = declarative_base()

# create a function to create the tables
def create_tables():
    SQLModel.metadata.create_all(engine)
