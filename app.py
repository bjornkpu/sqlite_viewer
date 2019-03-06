#!/usr/bin/python
from flask import Flask, render_template
import sqlite3
import os
import time

tableName = ('clients')
databaseName = 'user-ip.db'


db_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), databaseName)
app = Flask(__name__)

def refresh():
    print('__________________________________________________________________\n')
    db = sqlite3.connect(db_file)
    cursor = db.cursor()

    tableHeaders = []
    dbData = []

    # Get tables
    cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' ''')
    tables = cursor.fetchall()
    print('tables: ',tables)

    # Get table data
    for i,table in enumerate(tables):
        print('\n-table: ',table[0])
        #get headers
        cursor.execute("PRAGMA table_info({0})".format(table[0]))
        rowNames = cursor.fetchall()

        rowHead = ()
        for rowName in rowNames:
            print('rowName: ',rowName[1])
            rowHead += (rowName[1],)
        tableHeaders.append(rowHead)


        cursor.execute("SELECT * FROM {0}".format(table[0]))
        tableData = cursor.fetchall()
        print()
        print('tableData: ',(tableData),)

        dbData.append(tableData)

    print('\n--- End ---\n')
    print('tableHeaders: ',tableHeaders)
    print('\ndbData: ',dbData)


    cursor.close()
    db.close()
    return render_template('main.html', tables=tables, tableHeaders=tableHeaders, dbData=dbData)



@app.route('/')
def main():
    LastChanged = os.stat(databaseName).st_mtime

    print(time.ctime(LastChanged))


    return refresh()


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
