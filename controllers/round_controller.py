from models.round_model import Round
from models.player_model import Player
from data import TOURNAMENTS


class RoundController:
    """Round controller"""
    def __init__(self, view) -> None:
        self.view = view

    def run_first_round(self):
        """generate players pair of the first tour"""
        tournament_id = self.view.request_id(TOURNAMENTS)
        match = Round(tournament_id)
        pairing_players = match.pairing_first_round()
        for pair in pairing_players:
            self.get_score_input(pair[0], pair[1])
        pairing_players = [item for sublist in pairing_players for item in sublist]
        match.pairing_second_round(pairing_players)

    def get_score_input(self, player_a: Player, player_b: Player):
        """get user entry for a tour between two players"""
        result = self.view.request_specific_number_only(player_a, player_b)
        player_a.faced_players.append(player_b.first_name)
        player_b.faced_players.append(player_a.first_name)
        if result == 1:
            player_a.tournament_score += 1
            player_b.tournament_score += 0
        elif result == 0.5:
            player_a.tournament_score += 0.5
            player_b.tournament_score += 0.5
        elif result == 0:
            player_a.tournament_score += 0
            player_b.tournament_score += 1
        print(
            str(player_a.first_name) + " " + str(player_a.tournament_score) + " " + " | " +
            str(player_b.first_name) + " " + str(player_b.tournament_score) + "\n"
            )
