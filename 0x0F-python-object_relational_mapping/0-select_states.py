#!/usr/bin/python3
""" lists id and name from a database """
import MySQLdb
import sys

if __name__ = "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )

    cursor = db.cursor()

    query = "SELECT * FROM states"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
