#!/usr/bin/python3
"""11"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    session = Session(bind=engine)
    state = State()
    state.name = "Louisiana"
    session.add(state)
    session.commit()

    result = session.query(State).order_by(State.id.asc())
    print(state.id)
