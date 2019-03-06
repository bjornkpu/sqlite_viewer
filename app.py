#!/usr/bin/python
from flask import Flask, render_template
import sqlite3
import os

tableName = ('clients')
databaseName = 'user-ip.db'


db_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), databaseName)
app = Flask(__name__)


@app.route('/')
def main():
    print()
    db = sqlite3.connect(db_file)
    cursor = db.cursor()

    tableHeaders = []
    data = []

    # Get tables
    cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' ''')
    tables = cursor.fetchall()
    print('tables: ',tables)

    # Get table data
    for i,table in enumerate(tables):
        print('table: ',table[0])
        #get headers
        cursor.execute("PRAGMA table_info({0})".format(table[0]))
        rowNames = cursor.fetchall()

        rowHead = ()
        for rowName in rowNames:
            print('rowName: ',rowName[1])
            rowHead += (rowName[1],)
        tableHeaders.append(rowHead)



        cursor.execute("SELECT * FROM {0}".format(table[0]))
        data.append(cursor.fetchall())


    print('tableHeaders: ',tableHeaders)
    print('data: ',data)
    cursor.execute('SELECT * FROM clients')
    data = cursor.fetchall()


    cursor.close()
    db.close()
    return render_template('main.html', tables=tables, tableHeaders=tableHeaders, data=data)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
