#!/usr/bin/python3
"""script that list all states"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
                "Usage: {} <username> <password> <database> <state>".format(
                    sys.argv[0])
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_n = sys.argv[4]

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                username, password, database), pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_n).first()
    if state is not None:
        print(state.id)
    else:
        print("Not found")

    session.close()
