#!/usr/bin/python3
"""
    A script that lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
          argv[1], argv[2], argv[3]
        ),
        pool_pre_ping=True)
    result = engine.execute("SELECT * FROM states")
    for row in result:
        print("{}: {}".format(row[0], row[1]))
