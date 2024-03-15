#!/usr/bin/python3
"""
 To create State "California" with City "San Francisco" from
 the database hbtn_0e_100_usa
"""

import sys
from unicodedata import name
from venv import create
from sqlalchemy import create_engine, true
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)
    sess_maker = sessionmaker(bind=eng)
    sess = sess_maker()

    sess.add(City(name="San Francisco", stt=State(name="California")))
    sess.commit()
    sess.close()
