from models.tournament_model import Tournament
from controllers.player_controller import PlayerController
from views.player_view import PlayerView
from data import TOURNAMENTS

from typing import Union

import json

from tinydb import where


class TournamentController:
    """Tournament Controller"""
    def __init__(self, view) -> None:
        self.view = view
        # self.player_view = PlayerView()
        self.player_controller = PlayerController(PlayerView)

    def get_info_tournament(self) -> None:
        """Get the user entry info and create tournament"""
        while True:
            if self.view.check_data_players_numbers() is True:
                break
        name, place, date, time, description = self.view.ask_info_tournament()
        tournament = Tournament(name, place, date, time, description)
        tournament.save()
        print("\n The tournament named '{}' has been saved !".format(name))

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
        # player
        tournament.players = self.player_controller.instantiates_players()
        tournament_data = TOURNAMENTS.get(doc_id=tournament_id)
        serialized_players_list = []

        for player in tournament.players.values():
            serialized_player = json.dumps(player.__dict__)
            serialized_players_list.append(serialized_player)

        TOURNAMENTS.update({"players": serialized_players_list}, where("name") == tournament_data.get("name"))
        print("Selected players have been added to the tournament")
