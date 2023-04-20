#!/usr/bin/python3
""" A script that selects states"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3],
                                port=3306, charset="utf8")
    curr = connection.cursor()
    curr.execute("SELECT * FROM states ORDER BY id ASC")
    rows = curr.fetchall()
    for row in rows:
        print(row)
    curr.close()
    connection.close()