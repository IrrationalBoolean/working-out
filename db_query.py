

def check_table(con, table: str) -> bool:
    """checks if table exists in database, returns boolean"""
    cur = con.cursor()
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

def select_all(con, table) -> list:
    """returns 'SELECT * FROM table'"""
    cur = con.cursor()
    cur.execute(f'''SELECT * FROM {table}''')
    return cur.fetchall()
