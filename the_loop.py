from rich.prompt import Prompt

from db_utils import get_pushup_menu
from ux import login_menu, main_menu, plank_menu, pushup_menu


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
                pushup_option = plank_menu(cur, user)
                print(pushup_option)
                # log out
                if pushup_option == 0:
                    menu = None
                    user = None
                #todo do plank
                #todo some stats
                elif pushup_option == 2:
                #    text = get_pushup_menu(cur, user)
                #    print(text)
                    Prompt.ask('press enter to continue')
                # main menu
                elif pushup_option == 3:
                    menu = None

if __name__ == "__main__":
    from db_utils import start_app
    con = start_app()
    the_loop(con)