from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from controllers.round_controller import RoundController
from views.tournament_view import TournamentView
from views.player_view import PlayerView
from views.round_view import RoundView

from data import TOURNAMENTS

import check_functions as check


class Controller:
    """Main Controller"""

    def __init__(self, view) -> None:
        self.view = view
        self.tournament_view = TournamentView()
        self.player_view = PlayerView()
        self.round_view = RoundView()
        self.tournament_controller = TournamentController(self.tournament_view)
        self.player_controller = PlayerController(self.player_view)
        self.round_controller = RoundController(self.round_view)

        self.run_main_menu = "Yes"
        self.run_report_menu = "Yes"
        self.run_round_report_menu = "Yes"

    def run_main_menu_selection(self) -> None:
        """Get the user menu selection entry.."""
        self.run_report_menu = "No"
        self.run_round_report_menu = "No"

        while self.run_main_menu == "Yes":
            selection = self.view.main_menu()
            if selection == "1":
                self.tournament_controller.get_info_tournament()
            if selection == "2":
                self.player_controller.get_info_player()
            if selection == "3":
                self.tournament_controller.add_tournament_players()
            if selection == "4":
                self.run_report_menu = "Yes"
                self.run_report_menu_selection()
            if selection == "5":
                self.run_main_menu = "No"
            if selection == "8":
                self.tournament_controller.view.show_tournaments()
                # Tour 1
                players_list, round, tuple_results = self.round_controller.run_first_round()
                round.update_rounds(tuple_results, "round_1")
                # Tour 2
                players_list, round, tuple_results = self.round_controller.run_rounds_2_to_4(players_list, round)
                round.update_rounds(tuple_results, "round_2")
                # Tour 3
                players_list, round, tuple_results = self.round_controller.run_rounds_2_to_4(players_list, round)
                round.update_rounds(tuple_results, "round_3")
                # Tour 4
                players_list, round, tuple_results = self.round_controller.run_rounds_2_to_4(players_list, round)
                round.update_rounds(tuple_results, "round_4")
            if selection == "":
                print("You must enter a number ! ")

    def run_report_menu_selection(self) -> None:
        """Get the user report menu selection entry"""
        while self.run_report_menu == "Yes":
            selection = self.view.report_menu()
            if selection == "1":
                self.tournament_controller.view.show_tournaments()
            if selection == "2":
                self.player_controller.view.show_players()
            if selection == "3":
                self.tournament_controller.view.show_tournaments()
                self.player_controller.view.show_players_specific_tournament()
            if selection == "4":
                self.run_round_report_menu = "Yes"
                self.run_round_report_menu_selection()
            if selection == "5":
                self.run_main_menu_selection()
            if selection == "":
                print("You must enter a number ! ")

    def run_round_report_menu_selection(self) -> None:
        """Get user entry for view a particular round score of a tournament or all the round score of a tournament"""
        self.tournament_controller.view.show_tournaments()
        print("Choose a tournament to view the results : ")
        tournament_id = check.request_id(TOURNAMENTS)
        while self.run_round_report_menu == "Yes":
            selection = self.view.round_report_menu(tournament_id)
            if selection == "1":
                self.tournament_view.show_rounds_results(tournament_id)
            if selection == "2":
                self.tournament_view.show_round_1_results(tournament_id)
            if selection == "3":
                self.tournament_view.show_round_2_results(tournament_id)
            if selection == "4":
                self.tournament_view.show_round_3_results(tournament_id)
            if selection == "5":
                self.tournament_view.show_round_4_results(tournament_id)
            if selection == "6":
                self.run_report_menu_selection()
