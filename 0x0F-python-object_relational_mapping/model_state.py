#!/usr/bin/python3
"""
 To define a state modelcontain class definition
 of State and instance Base = declarative_base()
"""
from lib2to3.pytree import Base
from sre_parse import State
from unicodedata import name
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents state model that corresponds to the MySQL table states.

    Attributes:
        id: An auto-generated, unique int column representing the primary key.
        name: A string column representing the name of the state,
            with a max length of 128 characters.

    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
