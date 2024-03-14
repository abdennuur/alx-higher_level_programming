#!/usr/bin/python3
"""
 To delete all State objects with a name containing 'a'
 from database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    sess_maker = sessionmaker(bind=eng)
    sess = sess_maker()

    stts = sess.query(State).filter(State.name.like('%a%')).all()
    for stt in stts:
        sess.delete(stt)

    sess.commit()
