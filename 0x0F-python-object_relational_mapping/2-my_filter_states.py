#!/usr/bin/python3
""" To take an arg and display all values
    instates table of hbtn_0e_0_usa where
    name matche arg
    Usage: ./2-my_filter_states.py <mysql username>
                                   <mysql password>
                                   <database name>
                                   <state name searched>
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
    cr.execute("""SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC""".format(sys.argv[4]).strip("'"))
    [print(state) for state in cr.fetchall()]
