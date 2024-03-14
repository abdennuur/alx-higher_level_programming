#!/usr/bin/python3
"""Deletes excess rows from the database hbtn_0e_0_usa
 Usage: ./delete_excess_states.py <mysql username>
                                  <mysql password>
                                  <database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./delete_excess_states.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    try:
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        c = db.cursor()
        c.execute("DELETE FROM `states` WHERE id BETWEEN 6 AND 25")  # Delete rows 6 to 25
        db.commit()
        print("Excess rows deleted successfully.")
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
