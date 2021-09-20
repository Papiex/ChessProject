from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from controllers.round_controller import RoundController
from views.tournament_view import TournamentView
from views.player_view import PlayerView
from views.round_view import RoundView


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

    def run_main_menu_selection(self) -> None:
        """Get the user menu selection entry"""
        self.run_report_menu = "No"

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
                self.round_controller.run_first_round()
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
                self.run_main_menu_selection()
            if selection == "":
                print("You must enter a number ! ")

# pairing_players = [item for sublist in pairing_players for item in sublist]
