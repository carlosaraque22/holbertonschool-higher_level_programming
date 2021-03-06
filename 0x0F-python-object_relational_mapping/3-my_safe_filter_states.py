#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa with a
given name and is safe from MySQL injections
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            )
        cursor = db.cursor()
        query = """
            SELECT id, name
            FROM states
            WHERE BINARY name = %s
            ORDER BY id;
            """
        cursor.execute(query, (argv[4], ))
        rows = cursor.fetchall()
        for row in rows:
            if row in rows:
                print(row)
        cursor.close()
        db.close()
    except Exception as e:
        print("Error: {}".format(e))
