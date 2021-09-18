import sqlite3

db_name = 'test.db'


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
            REFERENCES user (id)
        )
    ''')


def insert_pushup_row(cur, data):
    cur.execute("""
    INSERT INTO pushup (date, time, dur, qty, uid)
    VALUES(?,?,?,?,?)""", data)


def get_pushup_menu(cur, user) -> str:
    """Returns a string of text representing user statistics"""
    text = ''

    # get most recent pushup session details
    cur.execute(f'''SELECT * FROM pushup WHERE id = 
                    (SELECT max(id) FROM pushup WHERE uid={user})''')
    most_recent = cur.fetchall()
    if most_recent:
        mr = most_recent[0]
        text += f'Your most recent pushups were on {mr[1]} at {mr[2]},\n'
        text += f'You did {mr[4]} pushups in {mr[3]:.3f} seconds.\n'

    # get max qty session details
    cur.execute(f'''SELECT * FROM pushup WHERE qty = 
                    (SELECT max(qty) FROM pushup WHERE uid={user})
                    ORDER BY date DESC, time DESC''')

    max_qty = cur.fetchall()
    if max_qty:
        mq = max_qty[0]
        text += f'Your best was {mq[4]} pushups in {mq[3]:.3f} seconds on {mq[1]}\n'

    # get average time per pushup
    cur.execute(f'''SELECT sum(dur) / sum(qty) FROM pushup
                WHERE uid={user}''')
    avg_time = cur.fetchall()
    if avg_time[0][0]:
        at = avg_time[0][0]
        text += f'You average {at:.3f} seconds per pushup\n'

    # get total pushups recorded
    cur.execute(f'''SELECT sum(qty), sum(dur) FROM pushup WHERE uid={user}''')
    total_pushups = cur.fetchall()
    if total_pushups[0][0]:
        tp = total_pushups[0]
        text += f"You've recoded {tp[0]} pushups over {tp[1]:.0f} seconds with this program! \n"

    return text + '\n'


def _create_table_plank(cur) -> None:
    """creates table for planks if table does not exist"""
    cur.execute('''
    CREATE TABLE IF NOT EXISTS plank
        ( id INTEGER PRIMARY KEY
        , date TEXT
        , time TEXT
        , dur REAL
        , uid INTEGER
        , FOREIGN KEY (uid)
            REFERENCES user (id)
        )
    ''')


def _create_table_user(cur) -> None:
    """creates table for users if table does not exist"""
    cur.execute('''
    CREATE TABLE IF NOT EXISTS user
    (id INTEGER PRIMARY KEY, name TEXT)
    ''')


def get_user_by_id(cur, id) -> str:
    """retrieves user name from db with cursor and user id"""
    cur.execute(f'''
    SELECT name FROM user WHERE id = {id} ''')
    return cur.fetchone()


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
    con = sqlite3.connect(db_name)
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
