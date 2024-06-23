#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                       format(username, password, db_name),
                       pool_pre_ping=True)

Base = declarative_base()
Base.metadata.create_all(engine)
