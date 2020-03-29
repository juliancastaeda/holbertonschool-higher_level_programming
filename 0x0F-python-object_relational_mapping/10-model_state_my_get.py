#!/usr/bin/python3
"""


"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    search = argv[4]
    session = sessionmaker(bind=engine)()
    ocurrency = session.query(State).filter(
        State.name == search).first()

    if ocurrency is not None:
        print("{}".format(ocurrency.id))
    else:
        print("Not found")
    session.close()
