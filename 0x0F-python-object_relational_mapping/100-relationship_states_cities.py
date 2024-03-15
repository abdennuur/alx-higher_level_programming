#!/usr/bin/python3
"""To list states"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    sess = Session()
    n_state = State(name="California")
    sess.add(n_state)
    sess.commit()
    n_city = City(name="San Francisco", state_id=n_state.id)
    sess.add(n_city)
    sess.commit()
    sess.close()
