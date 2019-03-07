#!/usr/bin/python
from flask import Flask, render_template
import sqlite3
import os


dbFileName = 'testdata/user-ip.db'
db_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), dbFileName)
app = Flask(__name__)


@app.route('/')
def main():
    tableHeaders = []
    dbData = []

    db = sqlite3.connect(db_file)
    cursor = db.cursor()

    # Get table names
    cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' ''')
    tables = cursor.fetchall()

    # Get table data
    for i,table in enumerate(tables):

        #get headers
        cursor.execute("PRAGMA table_info({0})".format(table[0]))
        rowNames = cursor.fetchall()

        rowHead = ()
        for rowName in rowNames:
            rowHead += (rowName[1],)
        tableHeaders.append(rowHead)

        # Get data
        cursor.execute("SELECT * FROM {0}".format(table[0]))
        tableData = cursor.fetchall()
        dbData.append(tableData)

    cursor.close()
    db.close()
    return render_template('main.html', tables=tables, tableHeaders=tableHeaders, dbData=dbData)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
