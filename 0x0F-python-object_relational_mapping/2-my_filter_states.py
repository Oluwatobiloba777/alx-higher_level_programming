#!/usr/bin/python3
"""
    A script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3],
                                port=3306, charset="utf8")
    curr = connection.cursor()
    curr.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(argv[4]))
    rows = curr.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    curr.close()
    connection.close()