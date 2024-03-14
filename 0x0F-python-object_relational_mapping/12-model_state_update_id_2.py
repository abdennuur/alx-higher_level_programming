#!/usr/bin/python3
"""
 To change the name of State object from database hbtn_0e_6_usa
"""

import sys
from unicodedata import name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    sess_maker = sessionmaker(bind=eng)
    sess = sess_maker()

    stt = sess.query(State).filter_by(id=2).first()
    stt.name = "New Mexico"
    sess.commit()
