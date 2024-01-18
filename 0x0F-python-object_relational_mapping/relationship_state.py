#!/usr/bin/python3
"""Module for defination of State class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """This is states class"""
    __tablename__ = "states"

    id = Column(
            Integer, primary_key=True,
            nullable=False, autoincrement=True
            )
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", backref="state",
            cascade="all, delete-orphan"
            )
