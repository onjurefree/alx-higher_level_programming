#!/usr/bin/python3
"""script that list all states"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
                "Usage: {} <username> <password> <database>".format(
                    sys.argv[0])
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                username, password, database), pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    onestate = session.query(State).order_by(State.id).first()
    if onestate is not None:
        print("{}: {}".format(onestate.id, onestate.name))
    else:
        print("Nothing")

    session.close()
