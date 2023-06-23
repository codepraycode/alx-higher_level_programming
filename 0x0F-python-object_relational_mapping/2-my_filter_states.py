#!/usr/bin/python3
"""
Displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb as mysql
from sys import argv

DB_NAME = "hbtn_0e_0_usa"
DB_HOST = 'localhost'
DB_PORT = 3306


if __name__ == "__main__":
    # run when not imported
    # Read arguments
    _, user, password, db_name, searched = argv

    try:
        db = mysql.connect(host=DB_HOST, port=DB_PORT, user=user,
                           passwd=password, db=db_name)
    except Exception as err:
        print("Failed to connect to database")
        exit(0)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name = BINARY '{:s}' \
                    ORDER BY id ASC;".format(searched))

    result_query = cursor.fetchall()

    for row in result_query:
        print(row)

    cursor.close()
    db.close()
