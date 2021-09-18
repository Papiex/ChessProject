from data import TOURNAMENTS
from models.player_model import Player

import json


class Round:
    """Class defining a round"""

    def __init__(self, tournament_id: int) -> None:
        self.tournament_id = tournament_id
        self.tournament_data = TOURNAMENTS.get(doc_id=tournament_id)

    def pairing_first_round(self) -> list[Player]:
        """pairing of first-round players according to their ranking"""
        players_list = self.tournament_data.get("players")
        deserialized_players_list = []
        for player_data in players_list:
            player = Player(**json.loads(player_data))
            deserialized_players_list.append(player)

        deserialized_players_list = sorted(deserialized_players_list, key=lambda player: player.ranking)
        deserialized_players_list.reverse()
        strong_players = deserialized_players_list[0:4]
        weak_players = deserialized_players_list[4:8]
        first_tour_pairing_list = []
        for strong_player, weak_player in zip(strong_players, weak_players):
            first_tour_pairing_list.append((strong_player, weak_player))
        print(first_tour_pairing_list)
        return first_tour_pairing_list

    def pairing_second_round(self, players_list: list[Player]) -> list[Player]:
        """pairing of second tour players according to their total points of current tournament"""

        if self.check_same_tournaments_points(players_list):
            players_list = sorted(players_list, key=lambda player: player.tournament_score)
        else:
            players_list = sorted(players_list, key=lambda player: player.ranking)
        players_list.reverse()
        # Checker si chaque joueur de paire se sont déja affronter

    def check_same_tournaments_points(self, players_list: list[Player]) -> bool:
        """Check if list contains duplicates of int values"""
        general_ranking_list = []
        for player in players_list:
            general_ranking_list.append(player.ranking)
        if len(general_ranking_list) == len(set(general_ranking_list)):
            return False
        else:
            return True
