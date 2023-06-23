#!/usr/bin/python3
"""
Takes in the name of a state as an argument and
lists all cities of that state, using
the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb as mysql
import re


DB_NAME = "hbtn_0e_0_usa"
DB_HOST = 'localhost'
DB_PORT = 3306


if __name__ == '__main__':

    if (len(argv) != 5):
        print('Use: username, password, database name, state name')
        exit(1)

    _, user, password, db_name, searched = argv

    state_name = ' '.join(searched.split())

    if (re.search('^[a-zA-Z ]+$', state_name) is None):
        print('Enter a valid name state (example: California)')
        exit(1)

    try:
        db = mysql.connect(host=DB_HOST, port=DB_PORT, user=user,
                           passwd=password, db=db_name)
    except Exception:
        print('Failed to connect to the database')
        exit(0)

    cursor = db.cursor()

    cuantity = cursor.execute("""SELECT c.name FROM cities as c
                      INNER JOIN states as s
                      ON c.state_id = s.id
                      WHERE s.name = '{:s}'
                      ORDER BY c.id ASC;""".format(state_name))

    result_query = cursor.fetchall()

    final = []

    for i in range(cuantity):
        final.append(result_query[i][0])

    print(', '.join(final))

    cursor.close()
    db.close()
