#!/usr/bin/python3
"""Model state"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = "states"
    id = Column('id', Integer, autoincrement=True, primary_key=True)
    name = Column('name', String(128))
