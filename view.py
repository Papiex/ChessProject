from string import punctuation, digits
from data import TOURNAMENTS, PLAYERS

import datetime


class View:

    def menu(self) -> str:
        """Main menu of the program"""
        print(
            "\n"
            "1 - Create a tournament      | 2 - Show all tournaments \n"
            "3 - Add a player to database | 4 - Show all saved players \n"
            "5 - Exit the programm        |"
            "\n"
            )
        response = input("Choose a number to browse the menu : ")
        return response

    def ask_info_tournament(self) -> str:
        """Get info of a tournament"""
        print("Enter name of the tournament : ")
        while True:
            name = input()
            if self.check_input_string_special(name) is True:
                if self.check_input_string_len(name) is True:
                    if self.check_input_string_integer(name) is True:
                        break

        print("Enter place of the tournament : ")
        while True:
            place = input()
            if self.check_input_string_special(place) is True:
                if self.check_input_string_len(place) is True:
                    if self.check_input_string_integer(place) is True:
                        break

        print("Enter the date with this format YEAR-MONTH-DAY : ")
        date = self.check_date_input()

        print(
            "1: Bullet = 1 minute \n"
            "2: Blitz = 10 minute \n"
            "3: Rapid = 15 minute \n"
            "Choose a number to define the time between tour : "
        )
        time = self.request_selection_with_number(1, 10, 15)
        description = input("Enter description of the tournament : ")

        return name, place, date, time, description

    def show_tournaments(self) -> None:
        """Show all the tournaments saved in tournaments.json"""
        for tournaments in TOURNAMENTS:
            print(tournaments)

    def ask_info_player(self) -> str:
        """Get info of a player"""

        print("Enter first name : ")
        while True:
            first_name = input()
            if self.check_input_string_special(first_name) is True:
                if self.check_input_string_len(first_name) is True:
                    if self.check_input_string_integer(first_name) is True:
                        break

        print("Enter last name : ")
        while True:
            last_name = input()
            if self.check_input_string_special(last_name) is True:
                if self.check_input_string_len(last_name) is True:
                    if self.check_input_string_integer(last_name) is True:
                        break

        print("Enter date of birth with this format YEAR-MONTH-DAY :  ")
        birthday = self.check_date_input()

        print(
            "Enter a number for choose the gender : \n"
            "1 - Man \n"
            "2 - Women"
            )
        genre = self.request_selection_with_number("Man", "Women", "none")

        print("\n The player {} {}, {}, birth on {} has been added to the database !".format(
            first_name,
            last_name,
            genre,
            birthday))

        return first_name, last_name, birthday, genre

    def show_players(self) -> None:
        """Show all players with id in players.json"""
        id = 0
        print("\n")
        for player in PLAYERS:
            id += 1
            print(str(id) + " : " + str(player))

    def check_input_string_special(self, string_to_check) -> bool:
        """Check input string entry for not to use special characters"""
        for symbol in punctuation:
            if symbol in string_to_check:
                print("No special character allowed : ")
                return False
        return True

    def check_input_string_len(self, string_to_check) -> bool:
        """Check input string entry for enter 2 character minimum"""
        if len(string_to_check) < 2:
            print("The minimum number of characters required is 2 : ")
            return False
        return True

    def check_input_string_integer(self, string_to_check) -> bool:
        """check if string have numbers in, return True or False"""
        for number in digits:
            if number in string_to_check:
                print("No numbers allowed : ")
                return False
        return True

    def check_date_input(self) -> str:
        """Check if input date string is a date format"""
        while True:
            try:
                date = input()
                datetime.datetime.strptime(date, "%Y-%m-%d")
                return date
            except ValueError:
                print("The correct date format is YEAR-MONTH-DAY : ")

    def request_selection_with_number(self, option_1: str or int, option_2: str or int, option_3: str or int) -> str:
        """
        Take user integer entry only, and assign string variable:
        variable = [1] for option_1 | [2] for option_2 | [3] for option_3
        option_3 is optional enter "none" for delete it.
        """
        while True:
            try:
                result = int(input())
            except TypeError:
                print("Enter a valid number : ")
            if result == 1:
                return str(option_1)
            elif result == 2:
                return str(option_2)
            elif result == 3:
                if option_3 == "none":
                    print("Enter a valid number : ")
                else:
                    return str(option_3)
            elif len(str(result)) >= 2:
                print("Enter a valid number : ")

    def create_players_id_dict(self) -> dict:
        """Request 8 id of players saved in players.json and return dict like this player_1 = id_selected ect"""
        players_id = {}
        key = 0
        self.show_players()
        print("\n" + "Enter id of wanted players : ")
        while len(players_id) < 8:
            while True:
                id_choice = self.request_players_id()
                if self.check_not_same_value(players_id, id_choice) is True:
                    key += 1
                    players_id["player_{0}".format(str(key))] = id_choice
                    break
        # print(players_id)
        return players_id

    def request_players_id(self) -> int:
        """request user entry for integer only"""
        while True:
            try:
                id_choice = int(input())
                return id_choice
            except ValueError:
                print("Enter only numbers : ")

    def check_not_same_value(self, players_id: dict, id_choice: int) -> bool:
        """check if dict contains two same values and return True or false"""
        for value in players_id.values():
            if value == id_choice:
                print("You already selected this player : ")
                return False
        return True
