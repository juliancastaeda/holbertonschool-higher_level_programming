#!/usr/bin/python3
"""

"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    ocurrency = session.query(State).filter(
        State.name.contains("a")).order_by(State.id)

    if ocurrency is not None:
        for st in ocurrency:
            print("{}: {}".format(st.id, st.name))
    else:
        print("Nothing")
    session.close()
