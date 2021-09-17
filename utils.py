import sqlite3

con = sqlite3.connect('pushups.db')

def check_table(con, table):
    cur = con.cursor()
    table_data = cur.execute(f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'""")
    table_fetch = table_data.fetchall()
    if table_fetch:
        return True
    return False

def create_pushup_table(con):
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS pushup
        (id INTEGER PRIMARY KEY, date TEXT, time TEXT, dur REAL, qty INTEGER)
        ''')
    cur.commit()