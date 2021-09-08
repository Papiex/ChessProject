from model import Tournament, Player
from data import PLAYERS


class Controller:
    """Main Controller"""

    def __init__(self, view) -> None:
        self.view = view

    def get_info_tournament(self) -> None:
        """Get the user entry info and create tournament"""
        while True:
            if self.check_data_players_numbers() is True:
                break
        name, place, date, time, description = self.view.ask_info_tournament()
        players = self.instantiates_players()
        tournament = Tournament(name, place, date, players, time, description)
        tournament.save()
        print("\n The tournament named '{}' has been saved !".format(name))
        # TEST
        print(tournament.players["player_1"].first_name)

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
                self.instantiates_players()

    def check_data_players_numbers(self) -> bool:
        """check if database has 8 minimum players saved in """
        get_players_numbers_saved = 0
        for player in PLAYERS:
            get_players_numbers_saved += 1
        if get_players_numbers_saved <= 7:
            print("The database of players need 8 saved players minimum !")
            return False
        elif get_players_numbers_saved == 8:
            return True

    def instantiates_players(self) -> dict:
        """instantiates 8 players selected by the user in a dict"""

        players_list = self.view.create_players_id_dict()
        for key in players_list:
            player_data = PLAYERS.get(doc_id=players_list.get(key))
            players_list[key] = Player(
                first_name=player_data.get("first_name"),
                last_name=player_data.get("last_name"),
                birthday=player_data.get("birthday"),
                genre=player_data.get("genre")
            )
        # print(players_list["player_1"].first_name)
        # print(players_list["player_4"].first_name)
        return players_list
