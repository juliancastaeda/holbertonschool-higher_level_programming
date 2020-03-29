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
    Session = sessionmaker(bind=engine)

    session = Session()
    new = session.query(State).filter(State.id == 2).one()
    new.name = "New Mexico"
    session.commit()
