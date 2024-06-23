#!/usr/bin/python3
"""13"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    session = Session(bind=engine)

    # delete all the object containing a
    result = session.query(State).filter(State.name.like("%a%"))
    for res in result.all():
        session.delete(res)
    session.commit()
    session.close()
