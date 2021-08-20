from data import TOURNAMENTS, PLAYERS

from string import punctuation
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
        is_valid = False
        while is_valid is not True:
            name = input("Enter the name of the tournament : ").title()
            is_valid = self.check_input_string(name)

        is_valid = False
        while is_valid is not True:
            place = input("Enter the place of the tournament : ").title()
            is_valid = self.check_input_string(place)

        date = input("Enter the date with this format YEAR-MONTH-DAY : ")
        self.check_date_input(date)

        is_valid = False
        while is_valid is not True:
            time = input(
                "1: Bullet = 1 minute \n"
                "2: Blitz = 10 minute \n"
                "3: Rapid = 15 minute \n"
                "Choose a number to define the time between tour : "
            )
            if len(time) >= 2:
                print("Accept only [1] for bullet and [2] for blitz and [3] for rapid !")
            elif time == "1":
                time = 1
                is_valid = True
                break
            elif time == "2":
                time = 10
                is_valid = True
                break
            elif time == "3":
                time = 15
                is_valid = True
            else:
                pass

        description = input("Enter description of the tournament : ")
        print("\n The tournament named '{}' has been saved !".format(name))
        return name, place, date, time, description

    def show_tournaments(self) -> None:
        """Show all the tournaments saved in tournaments.json"""
        for tournaments in TOURNAMENTS:
            print(tournaments)

    def ask_info_player(self) -> str:
        """Get info of a player"""
        is_valid = False
        while is_valid is not True:
            first_name = input("Enter first name : ").title()
            is_valid = self.check_input_string(first_name)

        is_valid = False
        while is_valid is not True:
            last_name = input("Enter last name : ").title()
            is_valid = self.check_input_string(last_name)

        birthday = input("Enter date of birth with this format YEAR-MONTH-DAY :  ")
        self.check_date_input(birthday)

        is_valid = False
        while is_valid is not True:
            genre = input(
                "1: Man \n"
                "2: Women \n"
                "Choose a number to define the gender : "
            )
            if len(genre) >= 2:
                print("Accept only [1] for man and [2] for women !")
            elif genre == "1":
                genre = "Man"
                is_valid = True
                break
            elif genre == "2":
                genre = "Woman"
                is_valid = True
                break
            else:
                pass
        print("\n The player {} {}, {}, birth on {} has been added to the database !".format(
            first_name,
            last_name,
            genre,
            birthday))

        return first_name, last_name, birthday, genre

    def show_players(self) -> None:
        """Show all players in players.json"""
        for player in PLAYERS:
            print(player)

    def check_input_string(self, string_to_check) -> bool:
        """Check input string entry for not to use special characters and check
           if the string have 2 character minimum"""
        for symbol in punctuation:
            if symbol in string_to_check:
                is_valid = False
                print("No special character allowed !")
                break
            else:
                is_valid = True

        if is_valid:
            while len(string_to_check) < 2:
                is_valid = False
                print("The minimum number of characters required is 2")
                break
            else:
                is_valid = True
        return is_valid

    def check_date_input(self, date_to_check) -> None:
        """Check if input date string is a date format"""
        while True:
            try:
                datetime.datetime.strptime(date_to_check, "%Y-%m-%d")
                break
            except ValueError:
                date_to_check = input("The correct date format is YEAR-MONTH-DAY : ")
