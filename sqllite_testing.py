import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import sqlite_version
import os
import sys


def create_connection(db_file):
    """
    create a connection to a db file and then close it
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite_version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            #hej


if __name__ == "__main__":

    db_name = sys.argv[1] if sys.argv[1] else 'py_db'
    path_to_db = 'sqlite3/'
    try:
        os.mkdir(path_to_db)
    except OSError as e:
        print(e)

    create_connection(rf'{os.getcwd()}/sqlite3/{db_name}.db')
