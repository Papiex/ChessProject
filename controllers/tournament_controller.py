from models.tournament_model import Tournament
from controllers.player_controller import PlayerController
from views.player_view import PlayerView
from data import TOURNAMENTS, PLAYERS

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
        name, place, date, time, description = self.view.ask_info_tournament()
        tournament = Tournament(name, place, date, time, description)
        tournament.save()

    def add_tournament_players(self) -> None:
        """Add 8 serialized players to a selected tournament"""
        if self.check_data_tournaments_numbers():
            self.view.display_empty_tournaments_file()
        self.view.show_tournaments()
        self.view.display_choose_a_tournament()
        tournament_id = check.request_id(TOURNAMENTS)
        if self.check_tournament_players(tournament_id):
            utils.clear_terminal()
            self.view.display_already_players()
        else:
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

    def check_tournament_players(self, tournament_id: int) -> bool:
        """check if a players have already 8 players"""
        tournament_data = TOURNAMENTS.get(doc_id=tournament_id)
        players = tournament_data.get("players")
        if players == []:
            return False
        else:
            return True

    def check_data_players_numbers(self) -> bool:
        """check if database has 8 minimum players saved in for create a tournament"""
        get_players_numbers_saved = 0
        for player in PLAYERS:
            get_players_numbers_saved += 1
        if get_players_numbers_saved <= 7:
            return False
        elif get_players_numbers_saved == 8 or get_players_numbers_saved > 8:
            return True
