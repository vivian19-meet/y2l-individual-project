from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_elder(name,location, feilds):
    print("Added an university!")
    university = University(name=name,location=location, feilds=feilds)
    session.add(university)
    session.commit()
