#!/usr/bin/python3
"""base module city"""
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    __tablename__ = 'cities'
    id = Column('id', Integer, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column('name', String(128))
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State')
