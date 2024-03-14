#!/usr/bin/python3
"""
 To print all City objects from database hbtn_0e_14_usa
"""

import sys
from venv import create
from sqlalchemy import create_engine, true
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    sess_maker = sessionmaker(bind=eng)
    sess = sess_maker()

    for ct, stt in sess.query(City, State)\
        .filter(City.state_id == State.id)\
            .order_by(City.id):
        print("{}: ({}) {}".format(stt.name, ct.id, ct.name))
