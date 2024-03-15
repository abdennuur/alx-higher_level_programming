#!/usr/bin/python3
"""
 To define a state model contain the class definition
 of State and instance Base = declarative_base()
"""
from lib2to3.pytree import Base
from sre_parse import State
from unicodedata import name
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City
Base = declarative_base()


class State(Base):
    """
    Represents a state model that corresponds to the MySQL table states.

    Attributes:
        id: An auto-generated, unique int column representing the primary key.
        name: A string column representing name of the state,
            with a max length of 128 characters.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
