from rich import print
from rich.console import Console
from rich.prompt import IntPrompt
from rich.table import Table
from db_utils import select_all, start_app

con = start_app()
cur = con.cursor()


def login_menu(cur) -> int:
    """Greets user and returns user id"""
    available_users = select_all(cur, 'user')
    table = Table(title='Available Users')
    table.add_column('UID', justify='right', style='green', no_wrap=True)
    table.add_column('Name', justify='left', style='blue', no_wrap=True)
    table.add_row("0", "Register")
    for user in available_users:
        table.add_row(str(user[0]), user[1])
    options = ["0"] + [str(user[0]) for user in available_users]
    print(options)
    console = Console()
    console.print(table)
    user = IntPrompt.ask("Enter your uid or pick 0 to register", choices=options)
    print(f'Welcome: {available_users[user - 1][1]}')
    return user

