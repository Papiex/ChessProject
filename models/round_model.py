from data import TOURNAMENTS
from models.player_model import Player

from itertools import repeat
from typing import Union
import json

import utils

from tinydb import where


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
        return first_tour_pairing_list

    def pairing_other_rounds(self, players_list: list[Player]) -> list[Player]:
        """pairing of second tour players according to their total points of current tournament"""

        if self.check_same_tournaments_points(players_list):
            players_list = sorted(players_list, key=lambda player: player.tournament_score)
        else:
            players_list = sorted(players_list, key=lambda player: player.ranking)
        players_list.reverse()
        # Lancer fonction de génération
        apairing_players = self.generating_pairs(players_list)
        return apairing_players

    def generating_pairs(self, players_list) -> list[tuple[Player]]:
        """Generate pair of player for a round"""
        apairing_players = []
        already_paired = []
        id_number = 0
        times_number_loop = 0
        breaks_number = 0
        while len(apairing_players) != 4:
            # Briser derniére paire si nombre de boucle == 50
            times_number_loop += 1
            if id_number == 8:
                id_number = 0
            pair = self.create_pair(players_list, id_number, already_paired)
            if pair is None:
                id_number += 1
            else:
                already_paired.append(pair[0])
                already_paired.append(pair[1])
                # pair[0].faced_players.append(pair[1].first_name)
                # pair[1].faced_players.append(pair[0].first_name)
                apairing_players.append(pair)
                id_number += 1
            if times_number_loop == 50:
                already_paired, apairing_players = self.break_pair(already_paired, apairing_players, breaks_number)
                times_number_loop = 0
                breaks_number += 1
        return apairing_players

    def check_same_tournaments_points(self, players_list: list[Player]) -> bool:
        """Check if list contains duplicates of int values"""
        general_ranking_list = []
        for player in players_list:
            general_ranking_list.append(player.ranking)
        if len(general_ranking_list) == len(set(general_ranking_list)):
            return False
        else:
            return True

    def check_faced_players(self, pair: tuple[Player]) -> tuple or None:
        """Check if player have already faced another player if true return None else return the tuple"""
        player_1 = pair[0]
        player_2 = pair[1]

        if player_1.first_name in player_2.faced_players:
            return None
        else:
            return pair

    def create_pair(self, players_list: list[Player], id_number, already_paired=[]) -> tuple:
        """creating tuple and check them and return them"""
        for player_1, player_2 in zip(repeat(players_list[id_number]), players_list[1:]):
            tuple = (player_1, player_2)
            pair = self.check_faced_players(tuple)
            if pair is None:
                pass
            else:
                if pair[0] in already_paired:
                    pass
                elif pair[1] in already_paired:
                    pass
                elif pair[0] == pair[1]:
                    pass
                else:
                    return pair

    def update_rounds_score(self, tuple_results: list[tuple[Player]], round_number: str) -> None:
        """
        save the result of a match
        round_number parameter :
            Enter "round_1" for save score of the round_1
            Enter "round_2" for save score of the round_2 ect ...
        """
        utils.display_enter_to_continue()
        if round_number == "round_1":
            TOURNAMENTS.update(
                {"score_round_1": tuple_results}, where("score_round_1") == self.tournament_data.get("score_round_1")
                )
        if round_number == "round_2":
            TOURNAMENTS.update(
                {"score_round_2": tuple_results}, where("score_round_2") == self.tournament_data.get("score_round_2")
                )
        if round_number == "round_3":
            TOURNAMENTS.update(
                {"score_round_3": tuple_results}, where("score_round_3") == self.tournament_data.get("score_round_3")
                )
        if round_number == "round_4":
            TOURNAMENTS.update(
                {"score_round_4": tuple_results}, where("score_round_4") == self.tournament_data.get("score_round_4")
                )

    def break_pair(
        self,
        apairing_players: list[tuple],
        already_paired: list[tuple[Player]],
        breaks_number: int
    ) -> Union[list[tuple], list[tuple[Player]]]:
        """remove the last pair or more from apairing players and already_paired players"""
        apairing_players = apairing_players[:-breaks_number]
        already_paired = already_paired[:-breaks_number]
        return already_paired, apairing_players
