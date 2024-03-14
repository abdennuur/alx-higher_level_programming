#!/usr/bin/python3
"""
 To define a state model contain the class definition of City
 and instance Base = declarative_base()
"""
from lib2to3.pytree import Base
from sre_parse import State
from unicodedata import name
from sqlalchemy import Column, ForeignKey, Integer, String, null
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Represents a city model that corresponds to the MySQL table cities.

    Attributes:
        id: An auto-generated, unique int column representing primary key.
        name: A string column with a maximum length of 128 characters.
        state_id: An int column representing a foreign key to states table.

    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
