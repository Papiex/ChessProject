from models.player_model import Player
from data import PLAYERS, TOURNAMENTS

import check_functions as check
import utils

import json


class PlayerView:

    def ask_info_player(self) -> str:
        """Get info of a player"""
        utils.clear_terminal()
        self.display_player_creation()
        print("Enter first name : ")
        while True:
            first_name = input()
            if check.check_input_string_special(first_name) is True:
                if check.check_input_string_len(first_name) is True:
                    if check.check_input_string_integer(first_name) is True:
                        break
        utils.clear_terminal()
        self.display_player_creation()
        print("Enter last name : ")
        while True:
            last_name = input()
            if check.check_input_string_special(last_name) is True:
                if check.check_input_string_len(last_name) is True:
                    if check.check_input_string_integer(last_name) is True:
                        break
        utils.clear_terminal()
        self.display_player_creation()
        print("Enter date of birth with this format YEAR-MONTH-DAY :  ")
        birthday = check.check_date_input()
        utils.clear_terminal()
        self.display_player_creation()
        print(
            "Enter a number for choose the gender : \n"
            "1 - Man \n"
            "2 - Women"
            )
        genre = check.request_selection_with_number("Man", "Women", "none")
        utils.clear_terminal()
        self.display_player_creation()
        print("The player {} {}, {}, birth on {} has been added to the database !".format(
            first_name,
            last_name,
            genre,
            birthday))
        utils.display_enter_to_continue()
        return first_name, last_name, birthday, genre

    def show_players(self) -> None:
        """Show all players with id in players.json in alphabetical order or not according to the user choice"""
        players_list = []
        for players in PLAYERS:
            player = Player.deserialize_player(Player, players.doc_id)
            players_list.append(player)
        utils.clear_terminal()
        print(
            "Do you want the list of players by alphabetical order or by ranking ? \n"
            "1 - Ranking players list \n"
            "2 - Alphabetical players list"
            )
        choice = check.request_selection_with_number("ranking", "alphabetical", "None")
        if choice == "ranking":
            player_id = 0
            players_list = sorted(players_list, key=lambda player: player.ranking)
            players_list.reverse()
            utils.clear_terminal()
            print("==========================================")
            print("List of all Players in ranking order : ")
            print("==========================================")
            for player in players_list:
                player_id += 1
                print(str(player_id) + " : " + str(player))
        elif choice == "alphabetical":
            player_id = 0
            players_list = sorted(players_list, key=lambda player: player.first_name)
            utils.clear_terminal()
            print("============================================")
            print("List of all Players in alphabetical order : ")
            print("============================================")
            for player in players_list:
                player_id += 1
                print(str(player_id) + " : " + str(player))

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
            utils.clear_terminal()
            print(
                "Do you want the list of players by alphabetical order or by ranking ? \n"
                "1 - Ranking players list \n"
                "2 - Alphabetical players list"
                )
            choice = check.request_selection_with_number("alphabetical", "ranking", "None")
            if choice == "alphabetical":
                utils.clear_terminal()
                deserialized_player_list = sorted(deserialized_player_list, key=lambda player: player.first_name)
                for deserialized_player in deserialized_player_list:
                    print(deserialized_player)
            elif choice == "ranking":
                utils.clear_terminal()
                deserialized_player_list = sorted(deserialized_player_list, key=lambda player: player.ranking)
                for deserialized_player in deserialized_player_list:
                    print(deserialized_player)

    def create_players_ids_list(self) -> list:
        """Request 8 id of players saved in players.json and return a list of ids"""
        players_id = []
        self.show_players()
        print("\n" + "Enter id of wanted players : ")
        while len(players_id) < 8:
            while True:
                id_choice = check.request_id(PLAYERS)
                if check.check_not_same_value(players_id, id_choice) is True:
                    players_id.append(id_choice)
                    break
        return players_id

    def display_empty_players_file(self) -> None:
        """Simply display message if players.json are empty"""
        utils.clear_terminal()
        print("\nNo players has been created yet")

    def display_player_creation(self) -> None:
        """simply print message for players creation"""
        print(
            "=====================\n"
            "   PLAYER CREATION   \n"
            "====================="
            )

    def display_choose_player_modify_score(self) -> None:
        """simply print message for choose player for modify his ranking"""
        print("\nSelect Player id to modify his ranking : ")
