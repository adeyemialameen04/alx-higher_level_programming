#!/usr/bin/python3
"""14"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    session = Session(bind=engine)

    city = session.query(State, City).join(City).order_by(City.id)
    for state, city in city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
