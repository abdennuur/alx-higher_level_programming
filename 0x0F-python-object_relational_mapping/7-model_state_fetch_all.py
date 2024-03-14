#!/usr/bin/python3
"""
 To list all State objects frm database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    eng = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    sess_maker = sessionmaker(bind=eng)
    sess = sess_maker()

    for state in sess.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
