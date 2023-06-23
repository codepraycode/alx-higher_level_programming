#!/usr/bin/python3
"""
Lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb as mysql
from sys import argv

DB_NAME = "hbtn_0e_0_usa"
DB_HOST = 'localhost'
DB_PORT = 3306


if __name__ == "__main__":
    # run when not imported
    # Read arguments
    _, user, password, db_name = argv

    try:
        db = mysql.connect(host=DB_HOST, port=DB_PORT, user=user,
                           passwd=password, db=db_name)
    except Exception as err:
        print("Failed to connect to database")
        exit(0)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states \
                    WHERE name LIKE BINARY 'N%' ORDER BY id ASC;")

    result_query = cursor.fetchall()

    for row in result_query:
        print(row)

    cursor.close()
    db.close()
