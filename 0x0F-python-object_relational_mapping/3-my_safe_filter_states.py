#!/usr/bin/python3
"""
 To display all values in states table of
 hbtn_0e_0_usa where name matche the arg
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
    cr.execute("""SELECT * FROM states""")
    [print(state) for state in cr.fetchall() if state[1] == sys.argv[4]]
