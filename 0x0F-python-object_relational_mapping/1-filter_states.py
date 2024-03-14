#!/usr/bin/python3
""" To list all states with a name starting with upper N
    from database hbtn_0e_0_usa
    Usage: ./1-filter_states.py <mysql username>
                                <mysql password>
                                <database name>"""

import sys
from unicodedata import name
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3]
    )
    cr = db.cursor()
    cr.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in cr.fetchall() if state[1][0] == "N"]
