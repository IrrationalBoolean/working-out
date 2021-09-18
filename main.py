#!/home/k/Documents/Python/Pushups/env/bin/python
import datetime
import sqlite3
import time

from db_utils import start_app
from the_loop import the_loop


if __name__ == '__main__':
    con = start_app()
    cur = con.cursor()
    the_loop(con)
