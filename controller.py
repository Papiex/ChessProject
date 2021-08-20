from model import Tournament, Player
from data import PLAYERS, PLAYERS_NUMBERS, get_field_data


class Controller:
    """Main Controller"""

    def __init__(self, view) -> None:
        self.view = view

    def get_info_tournament(self) -> None:
        """Get the user entry info and create tournament"""

        name, place, date, time, description = self.view.ask_info_tournament()
        tournament = Tournament(name, place, date, time, description)
        tournament.save()

    def get_info_player(self) -> None:
        """Get the user entry info and create a player"""

        first_name, last_name, birthday, genre = self.view.ask_info_player()
        player = Player(first_name, last_name, birthday, genre)
        player.save()

    def run_menu_selection(self) -> None:
        """Get the user menu selection entry"""
        run = "Yes"
        while run == "Yes":
            selection = self.view.menu()
            if selection == "1":
                self.get_info_tournament()
            if selection == "2":
                self.view.show_tournaments()
            if selection == "3":
                self.get_info_player()
            if selection == "4":
                self.view.show_players()
            if selection == "5":
                run = "No"
            if selection == "6":
                # TEST
                print(get_field_data("First Name", PLAYERS))

    def check_players_numbers(self) -> None:
        """check if database has 8 minimum players saved in """
        get_players_numbers_saved = 0
        for player in PLAYERS:
            get_players_numbers_saved += 1
            if get_players_numbers_saved == PLAYERS_NUMBERS:
                # proposer les joueur dans la database et les instancier p1 p2 ect...
                pass
            elif get_players_numbers_saved <= 7:
                print("minimum players required is 8 !")
            else:
                pass
