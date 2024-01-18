#!/usr/bin/python3
"""
Script to select all states
"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    if len(sys.argv) != 4:
        print(
                "Usage: {} <mysql_username> <mysql_password> <database_name>"
                .format(sys.argv[0])
                )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        db = MySQLdb.connect(
                host="localhost", port=3306,
                user=username, password=password,
                db=database_name
                )
        cursor = db.cursor()
        qu = """
        SELECT cities.id, cities.name, states.name FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """
        cursor.execute(qu)
        cities = cursor.fetchall()

        for k in cities:
            print(k)

    except MySQLdb.Error as e:
        pass
        sys.exit(1)

    finally:
        cursor.close()
        db.close()
