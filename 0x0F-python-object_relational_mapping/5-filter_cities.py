#!/usr/bin/python3
"""
 To list all cities of state, using database hbtn_0e_4_usa
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
    cr.execute("""SELECT * FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id""")
    print(", ".join([city[2]
                     for city in cr.fetchall()
                     if city[4] == sys.argv[4]]))
