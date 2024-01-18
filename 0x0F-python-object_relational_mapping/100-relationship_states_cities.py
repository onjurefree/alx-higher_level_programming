#!/usr/bin/python3
"""this script creates state california with city san francisco"""

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

    new_s = State(name="California")
    new_c = City(name="San Francisco", state=new_s)
    new_s.cities.append(new_c)

    session.add(new_s)
    session.add(new_c)
    session.commit()

    session.close()
