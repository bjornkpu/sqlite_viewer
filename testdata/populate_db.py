#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3

import datetime, time

def run_sql_file(filename, connection):
    '''
    The function takes a filename and a connection as input
    and will run the SQL query on the given connection
    '''
    start = time.time()

    file = open(filename, 'r')
    print("--Start executing: " + filename + " at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")) + "\n")
    cursor = connection.cursor()
    for lines in file:
        print(lines,end="")
        cursor.execute(lines)

    connection.commit()

    end = time.time()
    print("\n--Time elapsed to run the query:")
    print(str((end - start)*1000//1)[:-2] + ' ms')



def main():
    connection = sqlite3.connect('user-ip.db')
    run_sql_file("populate_db_tables.sql", connection)
    connection.close()

if __name__ == "__main__":
    main()
