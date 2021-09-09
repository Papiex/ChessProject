from model import Tournament, Player
from data import PLAYERS, TOURNAMENTS

from typing import Union
import json

from tinydb import where


class Controller:
    """Main Controller"""

    def __init__(self, view) -> None:
        self.view = view

    def get_info_tournament(self) -> None:
        """Get the user entry info and create tournament"""
        while True:
            if self.check_data_players_numbers() is True:
                break
        name, place, date, time, description = self.view.ask_info_tournament()
        tournament = Tournament(name, place, date, time, description)
        tournament.save()
        print("\n The tournament named '{}' has been saved !".format(name))
        # TEST
        # print(tournament.players["player_1"].first_name)

    def get_info_player(self) -> None:
        """Get the user entry info and create a player"""

        first_name, last_name, birthday, genre = self.view.ask_info_player()
        ranking = 0
        player = Player(first_name, last_name, birthday, genre, ranking)
        player.save()

    def run_menu_selection(self) -> None:
        """Get the user menu selection entry"""
        run = "Yes"
        while run == "Yes":
            selection = self.view.menu()
            if selection == "1":
                self.get_info_tournament()
            if selection == "2":
                self.view.show_tournaments()
            if selection == "3":
                self.get_info_player()
            if selection == "4":
                self.view.show_players()
            if selection == "5":
                run = "No"
            if selection == "6":
                self.add_tournament_players()
            if selection == "7":
                # TEST
                self.view.show_players_specific_tournament()

    def check_data_players_numbers(self) -> bool:
        """check if database has 8 minimum players saved in """
        get_players_numbers_saved = 0
        for player in PLAYERS:
            get_players_numbers_saved += 1
        if get_players_numbers_saved <= 7:
            print("The database of players need 8 saved players minimum !")
            return False
        elif get_players_numbers_saved == 8 or get_players_numbers_saved > 8:
            return True

    def instantiates_players(self) -> dict:
        """instantiates 8 players selected by the user in a dict"""

        players_list = self.view.create_players_id_dict()
        for key in players_list:
            player_data = PLAYERS.get(doc_id=players_list.get(key))
            players_list[key] = Player(
                first_name=player_data.get("first_name"),
                last_name=player_data.get("last_name"),
                birthday=player_data.get("birthday"),
                genre=player_data.get("genre"),
                ranking=player_data.get("ranking")
            )
        return players_list

    def instantiate_tournament(self) -> Union[Tournament, int]:
        """instantiate tournament saved in tournaments.json"""
        self.view.show_tournaments()
        tournament_id = self.view.request_id(TOURNAMENTS)
        tournament_data = TOURNAMENTS.get(doc_id=tournament_id)
        tournament = Tournament(
            name=tournament_data.get("name"),
            place=tournament_data.get("place"),
            date=tournament_data.get("date"),
            time=tournament_data.get("time"),
            description=tournament_data.get("description")
        )
        return tournament, tournament_id

    def add_tournament_players(self):
        """Add 8 players to a selected tournament"""
        tournament, tournament_id = self.instantiate_tournament()
        tournament.players = self.instantiates_players()
        tournament_data = TOURNAMENTS.get(doc_id=tournament_id)
        serialized_players_list = []

        for player in tournament.players.values():
            serialized_player = json.dumps(player.__dict__)
            serialized_players_list.append(serialized_player)

        TOURNAMENTS.update({"players": serialized_players_list}, where("name") == tournament_data.get("name"))
        print("Selected players have been added to the tournament")
