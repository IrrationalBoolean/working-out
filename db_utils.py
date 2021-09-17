import sqlite3


def _create_table_pushup(cur) -> None:
    """creates table for pushups if table does not exist"""
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


def insert_pushup_row(cur, data):
    cur.execute("""
    INSERT INTO pushup (date, time, dur, qty, uid)
    VALUES(?,?,?,?,?)""", data)


def _create_table_plank(cur) -> None:
    """creates table for planks if table does not exist"""
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


def _create_table_user(cur) -> None:
    """creates table for users if table does not exist"""
    cur.execute('''
    CREATE TABLE IF NOT EXISTS user
    (id INTEGER PRIMARY KEY, name TEXT)
    ''')



def check_table(cur, table: str) -> bool:
    """checks if table exists in database, returns boolean"""
    table_data = cur.execute(f"""
    SELECT name 
    FROM sqlite_master 
    WHERE type='table' 
      AND name='{table}'
    """)
    table_fetch = table_data.fetchall()
    if table_fetch:
        return True
    return False


def select_all(cur, table) -> list:
    """returns 'SELECT * FROM table'"""
    cur.execute(f'''SELECT * FROM {table}''')
    return cur.fetchall()


def start_app() -> sqlite3.Connection:
    """creates tables if they don't exist, returns connection to database"""
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    con.commit()
    if not check_table(cur, 'user'):
        _create_table_user(cur)
    if not check_table(cur, 'pushup'):
        _create_table_pushup(cur)
    if not check_table(cur, 'plank'):
        _create_table_plank(cur)
    return con
