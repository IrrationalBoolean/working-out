from rich.prompt import IntPrompt, Prompt

from db_utils import get_pushup_menu
from ux import login_menu, main_menu, plank_menu, pushup_menu


def planks(user, cur):
    import time, datetime
    start = time.time()
    date = datetime.datetime.now().date()
    Prompt.ask("Press Enter when done:")
    cur.execute('''
            INSERT INTO plank (date, time, dur, uid) 
            VALUES(?,?,?,?)''', (date, datetime.datetime.now().time().strftime('%H:%M:%S'), time.time()-start, user))
    cur.execute('''select * from plank''')
    for row in cur.fetchall():
        print(row[1:])
        time.sleep(.31)

    con.commit()

def pushups(user, cur):
    import time, datetime
    start = time.time()
    date = datetime.datetime.now().date()
    qty = IntPrompt.ask("Enter quantity of pushups: ")
    cur.execute('''
            INSERT INTO pushup (date, time, dur, qty, uid) 
            VALUES(?,?,?,?,?)''', (date, datetime.datetime.now().time().strftime('%H:%M:%S'), time.time()-start, qty, user))
    cur.execute('''select * from pushup''')
    for row in cur.fetchall():
        print(row[1:])
    con.commit()



def the_loop(con):
    cur = con.cursor()
    user = None
    menu = None
    pushup_option = None
    while True:
        # not logged in
        if not user:
            user = login_menu(cur)
        # logged in, goes to main menu
        else:
            # default main menu
            if menu is None:
                menu = main_menu(cur, user)
            # selected logout
            if menu == 0:
                menu = None
                user = None
            # selected pushups
            elif menu == 1:
                # in pushup menu
                pushup_option = pushup_menu(cur, user)
                print(pushup_option)
                # logout
                if pushup_option == 0:
                    menu = None
                    user = None
                #todo do pushups
                if pushup_option == 1:
                    pushups(user, cur)
                # some stats
                elif pushup_option == 2:
                    text = get_pushup_menu(cur, user)
                    print(text)
                    Prompt.ask('press enter to continue')
                # main menu
                elif pushup_option == 3:
                    menu = None
            # selected planks
            elif menu == 2:
                # in plank menu
                plank_option = plank_menu(cur, user)
                print(plank_option)
                # log out
                if plank_option == 0:
                    menu = None
                    user = None
                # do plank
                if plank_option == 1:
                    planks(user, cur)
                #todo some stats
                elif plank_option == 2:
                #    text = get_pushup_menu(cur, user)
                #    print(text)
                    Prompt.ask('press enter to continue')
                # main menu
                elif plank_option == 3:
                    menu = None

if __name__ == "__main__":
    from db_utils import start_app
    con = start_app()
    the_loop(con)