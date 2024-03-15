#!/usr/bin/python3
""" To list states"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=eng)
    sess = Session()

    for ct, stt in sess.query(City, State)\
                              .join(State, State.id == City.state_id)\
                              .order_by(City.id):
        print("{}: {} -> {}".format(ct.id, ct.name, stt.name))
