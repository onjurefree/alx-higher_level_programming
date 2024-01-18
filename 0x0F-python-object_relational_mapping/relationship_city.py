#!/usr/bin/python3
"""this is class City and its attributes"""

from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base


class City(Base):
    """This is City class"""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
