from models.tournament_model import Tournament
from models.player_model import Player

from data import TOURNAMENTS, PLAYERS

import check_functions as check
import utils


class TournamentView:

    def ask_info_tournament(self) -> str:
        """Get info of a tournament"""
        utils.clear_terminal()
        self.display_tournament_creation()
        print("Enter name of the tournament : ")
        while True:
            name = input()
            if check.check_input_string_special(name) is True:
                if check.check_input_string_len(name) is True:
                    if check.check_input_string_integer(name) is True:
                        break
        utils.clear_terminal()
        self.display_tournament_creation()
        print("Enter place of the tournament : ")
        while True:
            place = input()
            if check.check_input_string_special(place) is True:
                if check.check_input_string_len(place) is True:
                    if check.check_input_string_integer(place) is True:
                        break
        utils.clear_terminal()
        self.display_tournament_creation()
        print("Enter the start date of the tournament with this format YEAR-MONTH-DAY : ")
        start_date = check.check_date_input()
        utils.clear_terminal()
        self.display_tournament_creation()
        print("Enter the end date of the tournament with this format YEAR-MONTH-DAY : ")
        end_date = check.check_date_input()
        date = f"{start_date} to {end_date}"
        utils.clear_terminal()
        self.display_tournament_creation()
        print(
            "1: Bullet = 1 minute \n"
            "2: Blitz = 10 minute \n"
            "3: Rapid = 15 minute \n"
            "Choose a number to define the time between tour : "
        )
        time = check.request_selection_with_number("Bullet", "Blitz", "Rapid")
        utils.clear_terminal()
        self.display_tournament_creation()
        description = input("Enter description of the tournament : ")
        utils.clear_terminal()
        self.display_tournament_creation()
        print(f"The tournament named '{name}' has been saved !")
        utils.display_enter_to_continue()
        return name, place, date, time, description

    def show_tournaments(self) -> None:
        """Show all the tournaments with id saved in tournaments.json"""
        tournament_id = 0
        print("==========================")
        print("List of all Tournaments : ")
        print("==========================")

        for tournaments in TOURNAMENTS:
            tournament_id += 1
            tournament = Tournament.deserialize_tournament(Tournament, tournament_id)
            print(f"{str(tournament_id)} : {tournament}")

    def check_data_players_numbers(self) -> bool:
        """check if database has 8 minimum players saved in for create a tournament"""
        get_players_numbers_saved = 0
        for player in PLAYERS:
            get_players_numbers_saved += 1
        if get_players_numbers_saved <= 7:
            print("The database of players need 8 saved players minimum !")
            return False
        elif get_players_numbers_saved == 8 or get_players_numbers_saved > 8:
            return True

    def show_rounds_results(self, tournament_id, selected_round: str) -> None:
        """
        Show the results of selected round, "score_round_1", "score_round_2" ect...
        Use "all" for all rounds.
        """
        utils.clear_terminal()
        tournament_data = TOURNAMENTS.get(doc_id=tournament_id)
        if selected_round == "all":
            round_1 = tournament_data.get("score_round_1")
            round_2 = tournament_data.get("score_round_2")
            round_3 = tournament_data.get("score_round_3")
            round_4 = tournament_data.get("score_round_4")
            rounds_list = {"ROUND 1": round_1, "ROUND 2": round_2, "ROUND 3": round_3, "ROUND 4": round_4}
            for round_key, round in rounds_list.items():
                if round == []:
                    print("This Round have not been played yet")
                else:
                    print("===================")
                    print(f"|RESULT OF {round_key}|")
                    print("===================")
                    print("START TIME :")
                    print(round[4][0])
                    print("END TIME :")
                    print(round[4][1])
                    print("___________________________")
                    for tuple_round in round[0:4]:
                        print(tuple_round)
                    print("___________________________")
                    utils.display_enter_to_continue()
                    utils.clear_terminal()
        else:
            round = tournament_data.get(selected_round)
            print("===================")
            print(f"|RESULT OF {selected_round.replace('score_', '').replace('_', ' ').upper()}|")
            print("===================")
            print("START TIME :")
            print(round[4][0])
            print("END TIME :")
            print(round[4][1])
            print("___________________________")
            for tuple_round in round[0:4]:
                print(tuple_round)
            print("___________________________")
            utils.display_enter_to_continue()
            utils.clear_terminal()

    def display_selected_players(self, deserialized_players_list: list[Player]) -> None:
        "Display a message for print selected players of a tournament"
        print("Selected players have been added to the Tournament :\n")
        for player in deserialized_players_list:
            print(player)
        print("\n")

    def display_choose_a_tournament(self) -> None:
        """simply print a message"""
        print("\nChoose a tournament for add players : ")

    def display_empty_tournaments_file(self) -> None:
        """Simply display message if tournaments.json are empty"""
        utils.clear_terminal()
        print("\nNo tournament has been created yet")

    def display_tournament_creation(self) -> None:
        """simply print message for tournaments creation"""
        print(
            "=====================\n"
            "TOURNAMENT'S CREATION\n"
            "====================="
            )

    def display_launch_continue_tournament(self) -> None:
        """ simply print message when continue or launch tournament"""
        print("\nChoose tournament to launch or continue : ")

    def display_show_specific_tournament_players(self) -> None:
        """simply print message before view tournaments players"""
        print("\nChoose a tournament to see its players : ")

    def display_no_score(self, number: str) -> None:
        """simply print message when a requested round result is empty"""
        print(f"ROUND {number} have not been played yet")

    def display_no_enought_players(self) -> None:
        """simply print message if database players < 8"""
        print("The database of players need 8 saved players minimum !")

    def display_already_players(self) -> None:
        """simply print message if tourrnament have already 8 players"""
        print("8 players have already been added to this tournament !")
