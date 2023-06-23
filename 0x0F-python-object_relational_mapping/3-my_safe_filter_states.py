#!/usr/bin/python3
"""
Displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
(Safe from SQL Injection)
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

    searched = ' '.join(searched.split())

    if (re.search('^[a-zA-Z ]+$', searched) is None):
        print('Enter a valid name state (example: Arizona)')
        exit(1)

    try:
        db = mysql.connect(host=DB_HOST, port=DB_PORT, user=user,
                           passwd=password, db=db_name)
    except Exception:
        print('Failed to connect to the database')
        exit(0)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states \
                    WHERE name = '{:s}' ORDER BY id ASC;".format(searched))

    result_query = cursor.fetchall()

    for row in result_query:
        print(row)

    cursor.close()
    db.close()
