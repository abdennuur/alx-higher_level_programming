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

    for stt in sess.query(State).order_by(State.id):
        print("{}: {}".format(stt.id, stt.name))
        for ct in stt.cities:
            print("\t{}: {}".format(ct.id, ct.name))
