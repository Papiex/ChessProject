from models.tournament_model import Tournament
from controllers.player_controller import PlayerController
from views.player_view import PlayerView
from data import TOURNAMENTS

import check_functions as check
import utils

from tinydb import where


class TournamentController:
    """Tournament Controller"""
    def __init__(self, view) -> None:
        self.view = view
        self.player_view = PlayerView()
        self.player_controller = PlayerController(self.player_view)

    def get_info_tournament(self) -> None:
        """Get the user entry info and create tournament"""
        while True:
            if self.view.check_data_players_numbers() is True:
                break
        name, place, date, time, description = self.view.ask_info_tournament()
        tournament = Tournament(name, place, date, time, description)
        tournament.save()

    def add_tournament_players(self) -> None:
        """Add 8 serialized players to a selected tournament"""
        if self.check_data_tournaments_numbers():
            self.view.display_empty_tournaments_file()
        else:
            self.view.show_tournaments()
            self.view.display_choose_a_tournament()
            tournament_id = check.request_id(TOURNAMENTS)
            tournament = Tournament.deserialize_tournament(Tournament, tournament_id)
            tournament.players = self.player_controller.instantiates_players()
            tournament_data = TOURNAMENTS.get(doc_id=tournament_id)
            serialized_players_list = []

            for player in tournament.players:
                serialized_player = player.serialize()
                serialized_players_list.append(serialized_player)

            TOURNAMENTS.update({"players": serialized_players_list}, where("name") == tournament_data.get("name"))

            utils.clear_terminal()
            self.view.display_selected_players(tournament.players)

    def check_data_tournaments_numbers(self) -> bool:
        """check if json are empty or not"""
        tournaments_number = 0
        for tournament in TOURNAMENTS:
            tournaments_number += 1

        if tournaments_number != 0:
            return False
        else:
            return True

    def check_if_empty_score_json(self, tournament_id: int, number: int) -> bool:
        """check if score_round_X have score saved in"""
        score_round = "score_round_" + number
        tournament_data = TOURNAMENTS.get(doc_id=tournament_id)
        if tournament_data.get(score_round) == []:
            return True
        else:
            return False
