from models.player_model import Player
from data import PLAYERS, TOURNAMENTS

import check_functions as check

import json


class PlayerView:

    def ask_info_player(self) -> str:
        """Get info of a player"""

        print("Enter first name : ")
        while True:
            first_name = input()
            if check.check_input_string_special(first_name) is True:
                if check.check_input_string_len(first_name) is True:
                    if check.check_input_string_integer(first_name) is True:
                        break

        print("Enter last name : ")
        while True:
            last_name = input()
            if check.check_input_string_special(last_name) is True:
                if check.check_input_string_len(last_name) is True:
                    if check.check_input_string_integer(last_name) is True:
                        break

        print("Enter date of birth with this format YEAR-MONTH-DAY :  ")
        birthday = check.check_date_input()

        print(
            "Enter a number for choose the gender : \n"
            "1 - Man \n"
            "2 - Women"
            )
        genre = check.request_selection_with_number("Man", "Women", "none")

        print("\n The player {} {}, {}, birth on {} has been added to the database !".format(
            first_name,
            last_name,
            genre,
            birthday))

        return first_name, last_name, birthday, genre

    def show_players(self) -> None:
        """Show all players with id in players.json in alphabetical order or not according to the user choice"""
        players_list = []
        for player in PLAYERS:
            data_player = (
                str(player.get("first_name")) + " " +
                str(player.get("last_name")) + " | " +
                str(player.get("birthday")) + " | " +
                str(player.get("genre"))
                )
            players_list.append(data_player)

        print(
            "Do you want the list of players by alphabetical order ? \n"
            "1 - Yes \n"
            "2 - No"
            )
        choice = check.request_selection_with_number("Yes", "No", "None")
        if choice == "Yes":
            player_id = 0
            players_list.sort()
            print("LIST OF ALL PLAYERS IN ALPHABETICAL ORDER : ")
            for player in players_list:
                player_id += 1
                print(str(player_id) + " : " + player)
        elif choice == "No":
            player_id = 0
            print("LIST OF ALL PLAYERS : ")
            for player in players_list:
                player_id += 1
                print(str(player_id) + " : " + player)

    def show_players_specific_tournament(self) -> None:
        """Show player of specific tournament"""
        id_choice = check.request_id(TOURNAMENTS)
        tournament_data = TOURNAMENTS.get(doc_id=id_choice)
        if tournament_data.get("players") == {}:
            print("\n This tournaments has no players yet")
        else:
            players_list = tournament_data.get("players")
            deserialized_player_list = []
            for player_data in players_list:
                deserialized_player = Player(**json.loads(player_data))
                deserialized_player_list.append(deserialized_player)
            print(
                "Do you want the list of players by alphabetical order ? \n"
                "1 - Yes \n"
                "2 - No"
                )
            choice = check.request_selection_with_number("Yes", "No", "None")
            if choice == "Yes":
                deserialized_player_list = sorted(deserialized_player_list, key=lambda player: player.first_name)
                for deserialized_player in deserialized_player_list:
                    print(deserialized_player)
            elif choice == "No":
                for deserialized_player in deserialized_player_list:
                    print(deserialized_player)

    def create_players_id_dict(self) -> dict:
        """Request 8 id of players saved in players.json and return dict like this player_1 = id_selected ect"""
        players_id = {}
        key = 0
        self.show_players()
        print("\n" + "Enter id of wanted players : ")
        while len(players_id) < 8:
            while True:
                id_choice = check.request_id(PLAYERS)
                if check.check_not_same_value(players_id, id_choice) is True:
                    key += 1
                    players_id["player_{0}".format(str(key))] = id_choice
                    break
        return players_id
