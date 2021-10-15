from models.round_model import Round
from models.player_model import Player
from models.tournament_model import Tournament
from data import TOURNAMENTS

import check_functions as check

import utils


class RoundController:
    """Round controller"""
    def __init__(self, view) -> None:
        self.view = view

    def get_score_input(self, player_a: Player, player_b: Player) -> tuple:
        """get user entry for a tour between two players"""
        result = self.view.request_specific_number_only(player_a, player_b)
        player_a.faced_players.append(player_b.first_name)
        player_b.faced_players.append(player_a.first_name)
        if result == 1:
            player_a.tournament_score += 1
            player_b.tournament_score += 0
            player_a_result = 1
            player_b_result = 0
        elif result == 0.5:
            player_a.tournament_score += 0.5
            player_b.tournament_score += 0.5
            player_a_result = 0.5
            player_b_result = 0.5
        elif result == 0:
            player_a.tournament_score += 0
            player_b.tournament_score += 1
            player_a_result = 0
            player_b_result = 1

        tuple_result = ((
            str(player_a.first_name) + " " + str(player_a_result) + " " + " | " +
            str(player_b.first_name) + " " + str(player_b_result)
            ))
        return tuple_result

    def run_rounds(self) -> None:
        """run rounds 1 to 4 of a tournament"""
        tournament_id = self.view.request_id(TOURNAMENTS)
        round = Round(tournament_id)
        tournament = Tournament.deserialize_tournament(Tournament, tournament_id)
        if tournament.get_actual_round() == 1:
            start_time = self.view.display_rounds_message("1", "start")
            pairing_players = round.pairing_first_round()
            for pair in pairing_players:
                tuple_result = self.get_score_input(pair[0], pair[1])
                round.result.append(tuple_result)
            players_list = [item for sublist in pairing_players for item in sublist]
            end_time = self.view.display_rounds_message("1", "end")
            round.result.append((start_time, end_time))
            response_for_next_round = self.save_data(tournament, round, players_list, tournament_id)
            if response_for_next_round == "Yes":
                pass
            else:
                return None
        if tournament.get_actual_round() >= 2 and not tournament.get_actual_round() == 5:
            current_round = tournament.get_actual_round()
            for i in range(current_round, 5):
                current_round = tournament.get_actual_round()
                start_time = self.view.display_rounds_message(str(tournament.current_round), "start")
                players_list = tournament.get_players_for_continue_tournament(tournament_id)
                pairing_players = round.pairing_other_rounds(players_list)
                for pair in pairing_players:
                    tuple_result = self.get_score_input(pair[0], pair[1])
                    round.result.append(tuple_result)
                players_list = [item for sublist in pairing_players for item in sublist]
                end_time = self.view.display_rounds_message(str(i), "end")
                round.result.append((start_time, end_time))
                response_for_next_round = self.save_data(tournament, round, players_list, tournament_id)
                if response_for_next_round == "Yes":
                    pass
                else:
                    return None

    def save_data(self, tournament: Tournament, round: Round, players_list: list[Player], tournament_id: int) -> str:
        """saving data when runnings rounds, return the response for the next round"""

        if tournament.get_actual_round() == 4:
            round.update_rounds_score(round.result, tournament.current_round)
            tournament.update_general_ranking_tournament(players_list)
            response_for_next_round = "No"
            tournament.current_round += 1
            tournament.save_actual_round(tournament_id)
        elif tournament.get_actual_round() == 5:
            self.view.display_tournament_end()
            utils.display_enter_to_continue()
        else:
            tournament.save_players_for_next_round(players_list, tournament_id)
            round.update_rounds_score(round.result, tournament.current_round)
            round.result = []
            tournament.current_round += 1
            tournament.save_actual_round(tournament_id)
            self.view.display_continue_to_next_round()
            response_for_next_round = check.request_selection_with_number("Yes", "No", "None")
        return response_for_next_round
