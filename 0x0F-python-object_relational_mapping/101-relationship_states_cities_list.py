#!/usr/bin/python3
"""this script prints all cities and their states"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv, exit

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                username, password, database), pool_pre_ping=True
            )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).order_by(State.id).all()

    for state in all_states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()
