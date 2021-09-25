# Utility files functions

import os

from datetime import datetime


def clear_terminal() -> None:
    """clear the terminal on windows or linux"""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_enter_to_continue() -> None:
    """simply display this message ("Press Enter to continue")"""
    input("Press Enter to continue...")


def get_actual_date_and_time() -> str:
    """get actual date and time and return them"""
    now = datetime.now()
    date_string = now.strftime("%Y/%m/%d %H:%M:%S")
    return date_string
