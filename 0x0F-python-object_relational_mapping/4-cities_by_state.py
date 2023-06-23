#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
from sys import argv
import MySQLdb as mysql


DB_NAME = "hbtn_0e_0_usa"
DB_HOST = 'localhost'
DB_PORT = 3306


if __name__ == '__main__':

    if (len(argv) != 4):
        print('Use: username, password, database name')
        exit(1)

    _, user, password, db_name = argv

    try:
        db = mysql.connect(host=DB_HOST, port=DB_PORT, user=user,
                           passwd=password, db=db_name)
    except Exception:
        print('Failed to connect to the database')
        exit(0)

    cursor = db.cursor()

    cursor.execute("""SELECT c.id, c.name, s.name FROM cities as c
                      INNER JOIN states as s
                      ON c.state_id = s.id
                      ORDER BY c.id ASC;""")

    result_query = cursor.fetchall()

    for row in result_query:
        print(row)

    cursor.close()
    db.close()
