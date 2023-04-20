#!/usr/bin/python3
"""
    A script that lists all State objects that
    contain the letter a from the database hbtn_0e_6_usa
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

    for instance in session.query(State).filter(State.name.contains('a')):
        print("{0}: {1}".format(instance.id, instance.name))