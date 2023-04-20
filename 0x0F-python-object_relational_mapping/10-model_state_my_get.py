#!/usr/bin/python3
"""
    A script that prints the State object
    with the name passed as argument from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
          argv[1], argv[2], argv[3]
        ),
        pool_pre_ping=True)
    Sessions = sessionmaker(bind=engine)
    session = Sessions()
    instance = session.query(State).filter(State.name == argv[4]).first()
    if instance is None:
        print("Not found")
    else:
        print("{0}".format(instance.id))