from model import Tournament, Player


class Controller:
    """Main Controller"""

    def __init__(self, view) -> None:
        self.view = view

    def get_info_tournament(self) -> None:
        """Get the user entry info and create tournament"""

        name, place, date, description = self.view.ask_info_tournament()
        tournament = Tournament(name, place, date, description)
        tournament.save()

    def get_info_player(self) -> None:
        """Get the user entry info and create a player"""

        first_name, last_name, birthday, genre = self.view.ask_info_player()
        player = Player(first_name, last_name, birthday, genre)
        player.save()

    def run_menu_selection(self) -> None:
        """Get the user menu selection entry"""

        selection = self.view.menu()
        if selection == "1":
            self.get_info_tournament()
        if selection == "2":
            self.view.show_tournaments()
