#!/usr/bin/python3
"""
 To print first State object from database hbtn_0e_6_usa
"""

import sys
from venv import create
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    sess_maker = sessionmaker(bind=eng)
    sess = sess_maker()

    stt = sess.query(State).order_by(State.id).first()
    if stt is None:
        print("Nothing")
    else:
        print("{}: {}".format(stt.id, stt.name))
