#!/usr/bin/python3
""" Filter states by user secure input """

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s"
    cursor.execute(query, (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
