#!/usr/bin/python3
"""this script prints all city objects"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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

    Session = sessionmaker(bind=engine)
    session = Session()

    all_cities = session.query(City).order_by(City.id).all()

    for city in all_cities:
        state = session.query(State).filter(State.id == city.state_id).first()
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
