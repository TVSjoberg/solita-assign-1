import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import sqlite_version
import os
import sys
db_file = 'finnish_wind_power_orig.db'

def create_connection():
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
            return conn


if __name__ == "__main__":
    create_connection('finnish_wind_power_orig.db')

