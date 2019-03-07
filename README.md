# sqlite_viewer
Small flask app to view sqlite databases

## Install
```
git clone git@github.com:bjornkpu/sqlite_viewer.git
cd sqlite_viewer
```
In `app.py` change
`dbFileName = 'testdata/user-ip.db'` to whatever and wherever your db-file is.

## Run
```
python app.py
```
Go to [localhost:5000](http://localhost:5000).

Refresh to check changes.

## Generate testdata
In /testdata

`python setup_db.py` - makes test table

`python populate_db_tables.py` -generates testdata
