from models.round_model import Round
from models.player_model import Player
from models.tournament_model import Tournament
from data import TOURNAMENTS

from typing import Union

import check_functions as check


class RoundController:
    """Round controller"""
    def __init__(self, view) -> None:
        self.view = view

    def get_score_input(self, player_a: Player, player_b: Player):
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

    def run_rounds(self) -> Union[list[list[tuple]], Round]:
        """run rounds 1 to 4 and return result list and the round instance"""
        tournament_id = self.view.request_id(TOURNAMENTS)
        round = Round(tournament_id)
        tournament = Tournament.deserialize_tournament(Tournament, tournament_id)
        if tournament.get_actual_round() == 1:
            tuple_results = []

            start_time = self.view.display_rounds_message("1", "start")
            pairing_players = round.pairing_first_round()
            for pair in pairing_players:
                tuple_result = self.get_score_input(pair[0], pair[1])
                tuple_results.append(tuple_result)
            players_list = [item for sublist in pairing_players for item in sublist]
            tournament.save_players_for_next_round(players_list, tournament_id)
            end_time = self.view.display_rounds_message("1", "end")
            tuple_results.append((start_time, end_time))

            tournament.current_round += 1
            tournament.save_actual_round(tournament_id)
            round.update_rounds_score(tuple_results, "round_1")
            self.view.display_continue_to_next_round()
            response_for_next_round = check.request_selection_with_number("Yes", "No", "None")
            if response_for_next_round == "Yes":
                pass
            else:
                # STOP METHODE
                return

        if tournament.get_actual_round() >= 2:
            current_round = tournament.get_actual_round()

            for i in range(current_round, 5):
                current_round = tournament.get_actual_round()
                start_time = self.view.display_rounds_message(str(tournament.current_round), "start")
                tuple_results = []
                players_list = tournament.get_players_for_continue_tournament(tournament_id)
                pairing_players = round.pairing_other_rounds(players_list)
                for pair in pairing_players:
                    tuple_result = self.get_score_input(pair[0], pair[1])
                    tuple_results.append(tuple_result)
                players_list = [item for sublist in pairing_players for item in sublist]
                tournament.save_players_for_next_round(players_list, tournament_id)
                end_time = self.view.display_rounds_message(str(i), "end")
                tuple_results.append((start_time, end_time))

                tournament.current_round += 1
                tournament.save_actual_round(tournament_id)
                round.update_rounds_score(tuple_results, "round_" + str(current_round))
                self.view.display_continue_to_next_round()
                response_for_next_round = check.request_selection_with_number("Yes", "No", "None")
                if response_for_next_round == "Yes":
                    pass
                else:
                    # STOP METHODE
                    return

        return round
