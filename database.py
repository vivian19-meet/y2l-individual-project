from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
def if_in_list(x,fields):
    if fields.count(x) == 1:
        b=fields.index(x)
        return True

def add_univ(name,location, fields,logo,link,pics):
    print("Added an university!")
    university = University(name=name,location=location, fields=fields, logo=logo, link=link ,pics=pics)
    session.add(university)
    session.commit()
def get_univ_by_field(field):
        universities = session.query(University).all()
        output = []
        for university in universities :
            if field in university.fields:
                output.append(university)
        return output 
def get_univ_by_id(id):
    university = session.query(
    University).filter_by(
    id=id).first()
    return university

def delete_univ_by_id(id):
    session.query(University).filter_by(
    id=id).delete()
    session.commit()