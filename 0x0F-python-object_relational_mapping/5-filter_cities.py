#!/usr/bin/python3
"""
Script that uses parameterized queries to safely insert args
avoiding SQL injection
"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    if len(sys.argv) != 5:
        print(
                "Usage: {} <username> <password> <database> <state>"
                .format(sys.argv[0])
                )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
                host="localhost", port=3306,
                user=username, password=password,
                db=database_name
                )
        cursor = db.cursor()
        qu = """
        SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ')
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        """
        cursor.execute(qu, (state_name,))
        outcome = cursor.fetchone()

        if outcome[0]:
            print(outcome[0])
        else:
            print()

    except MySQLdb.Error as e:
        pass
        sys.exit(1)

    finally:
        cursor.close()
        db.close()
