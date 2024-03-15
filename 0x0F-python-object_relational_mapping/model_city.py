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
        id: An auto-generated, unique int column representing the primary key.
        name: A string column representing name of city,
            with a maximum length of 128 characters.
        state_id: An integer column representing foreign key to states table,
        indicating the state to which the city belongs.

    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
