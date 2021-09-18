import os

from rich import print
from rich.console import Console
from rich.prompt import IntPrompt
from rich.table import Table

from db_utils import get_user_by_id, select_all, start_app

con = start_app()
cur = con.cursor()
id_color ='bold'
choice_color = 'white'


def login_menu(cur) -> int:
    """Greets user and returns user id"""
    available_users = select_all(cur, 'user')
    table = Table(title='Available Users')
    table.add_column("UID".rjust(9), justify='right', style=id_color, no_wrap=True)
    table.add_column('Name'.ljust(20), justify='left', style=choice_color, no_wrap=True)
    table.add_row("0", "Register")
    for user in available_users:
        table.add_row(str(user[0]), user[1])
    options = ["0"] + [str(user[0]) for user in available_users]

    print(options)

    console = Console()
    os.system('clear')
    console.print(table)
    user = IntPrompt.ask("Enter your uid or pick 0 to register", choices=options)
    print(f'Welcome: {available_users[user - 1][1]}')
    return user


def main_menu(cur, user):
    user_name = get_user_by_id(cur, user)
    table = Table(title=f"{user_name}: Let's Exercise")
    table.add_column("Choice ID", justify='right', style=id_color, no_wrap=True)
    table.add_column("Option".ljust(20), justify='left', style=choice_color, no_wrap=True)
    table.add_row("0", "Log Out")
    table.add_row("1", "Pushups")
    table.add_row("2", "Plank")

    console = Console()
    os.system('clear')
    console.print(table)
    choice = IntPrompt.ask("Select a Choice ID: ", choices=[str(x) for x in range(3)])
    return choice


def pushup_menu(cur, user):
    user_name = get_user_by_id(cur, user)
    table = Table(title=f"{user_name}: Pushup Time")
    table.add_column("Choice ID", justify='right', style=id_color, no_wrap=True)
    table.add_column("Option".ljust(20), justify='left', style=choice_color, no_wrap=True)
    table.add_row("0", "Log Out")
    table.add_row("1", "Start Pushups")
    table.add_row("2", "Some Stats")
    table.add_row("3", "Back")
    console = Console()
    os.system('clear')
    console.print(table)
    choice = IntPrompt.ask("Please select:  ", choices=[str(x) for x in range(0, 4)])
    return choice


def plank_menu(cur, user):
    user_name = get_user_by_id(cur, user)
    table = Table(title=f"{user_name}: Plank It Out")
    table.add_column("Choice ID", justify='right', style=id_color, no_wrap=True)
    table.add_column("Option".ljust(20), justify='left', style=choice_color, no_wrap=True)
    table.add_row("0", "Log Out")
    table.add_row("1", "Start Plank")
    table.add_row("2", "Some Stats")
    table.add_row("3", "Back")
    console = Console()
    os.system('clear')
    console.print(table)
    choice = IntPrompt.ask("Please select:  ", choices=[str(x) for x in range(0, 4)])
    return choice

