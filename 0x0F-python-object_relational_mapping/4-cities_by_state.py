#!/usr/bin/python3
"""
 To list all cities frm database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3]
    )
    cr = db.cursor()
    cr.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id ASC""")
    [print(city) for city in cr.fetchall()]
