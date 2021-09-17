import sqlite3

from db_query import check_table


def _create_table_pushup(con) -> None:
    """creates table for pushups if table does not exist"""
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS pushup
        ( id INTEGER PRIMARY KEY
        , date TEXT
        , time TEXT
        , dur REAL
        , qty INTEGER
        , uid INTEGER
        , FOREIGN KEY (uid)
            REFERENCES user (uid)
        )
    ''')


def _create_table_plank(con) -> None:
    """creates table for planks if table does not exist"""
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS plank
        ( id INTEGER PRIMARY KEY
        , date TEXT, time TEXT
        , dur REAL
        , uid INTEGER
        , FOREIGN KEY (uid)
            REFERENCES user (uid)
        )
    ''')


def _create_table_user(con) -> None:
    """creates table for users if table does not exist"""
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS user
    (id INTEGER PRIMARY KEY, name TEXT)
    ''')


def start_app() -> sqlite3.Connection:
    """creates tables if they don't exist, returns connection to database"""
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    con.commit()
    if not check_table(con, 'user'):
        _create_table_user(con)
    if not check_table(con, 'pushup'):
        _create_table_pushup(con)
    if not check_table(con, 'plank'):
        _create_table_plank(con)
    return con
