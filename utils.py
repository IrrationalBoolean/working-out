import sqlite3


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


def check_table(con, table: str) -> bool:
    """checks if table exists in database, returns boolean"""
    cur = con.cursor()
    table_data = cur.execute(f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'""")
    table_fetch = table_data.fetchall()
    if table_fetch:
        return True
    return False


def start_app():
    """creates tables if they don't exist, returns connection to database"""
    con = sqlite3.connect('pushups.db')
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