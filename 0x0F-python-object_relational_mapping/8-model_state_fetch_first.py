#!/usr/bin/python3
"""8"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    result = session.query(State).order_by(State.id.asc()).first()
    if result:
        print('{}: {}'.format(result.id, result.name))
    else:
        print('Nothing')
