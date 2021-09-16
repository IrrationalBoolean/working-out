#!/home/k/miniconda3/bin/python
import datetime
import sqlite3
import time
con = sqlite3.connect('pushups.db')
cur = con.cursor()
cur.execute('''
        CREATE TABLE IF NOT EXISTS pushup
        (id INTEGER PRIMARY KEY, date TEXT, time TEXT, dur REAL, qty INTEGER)
        ''')
if __name__ == '__main__':
    start = time.time()
    date = datetime.datetime.now().date()
    qty = 0
    while not qty:
        try:
            qty = int(input('How many pushups?  '))
        except Exception as e:
            print('Enter a number, error: ', e)
    cur.execute('''
            INSERT INTO pushup (date, time, dur, qty) 
            VALUES(?,?,?,?)''', (date, datetime.datetime.now().time().strftime('%H:%M:%S'), time.time()-start, qty))
    cur.execute('''select * from pushup''')
    for row in cur.fetchall():
        print(row)
    con.commit()
    con.close()
