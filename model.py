from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Product(Base):
    pass
Base = declarative_base()
class university(Base):
    __tablename__ = "universities"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    location = Column(String)
    fields =Column(list)
   
