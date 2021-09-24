from data import TOURNAMENTS, PLAYERS

import check_functions as check


class TournamentView:

    def ask_info_tournament(self) -> str:
        """Get info of a tournament"""
        check.clear_terminal()
        print(
            "=====================\n"
            "TOURNAMENT'S CREATION\n"
            "====================="
            )
        print("Enter name of the tournament : ")
        while True:
            name = input()
            if check.check_input_string_special(name) is True:
                if check.check_input_string_len(name) is True:
                    if check.check_input_string_integer(name) is True:
                        break
        check.clear_terminal()
        print("Enter place of the tournament : ")
        while True:
            place = input()
            if check.check_input_string_special(place) is True:
                if check.check_input_string_len(place) is True:
                    if check.check_input_string_integer(place) is True:
                        break
        check.clear_terminal()
        print("Enter the start date of the tournament with this format YEAR-MONTH-DAY : ")
        start_date = check.check_date_input()
        check.clear_terminal()
        print("Enter the end date of the tournament with this format YEAR-MONTH-DAY : ")
        end_date = check.check_date_input()
        date = f"{start_date} to {end_date}"
        check.clear_terminal()
        print(
            "1: Bullet = 1 minute \n"
            "2: Blitz = 10 minute \n"
            "3: Rapid = 15 minute \n"
            "Choose a number to define the time between tour : "
        )
        time = check.request_selection_with_number(1, 10, 15)
        check.clear_terminal()
        description = input("Enter description of the tournament : ")
        check.clear_terminal()
        print(f"The tournament named '{name}' has been saved !")
        input("Press enter to continue...")
        return name, place, date, time, description

    def show_tournaments(self) -> None:
        """Show all the tournaments with id saved in tournaments.json"""
        check.clear_terminal()
        tournament_id = 0
        print("\n")
        for tournament in TOURNAMENTS:
            tournament_id += 1
            print(
                f"{str(tournament_id)} : {tournament.get('name')} |"
                f" {tournament.get('place')} |"
                f" {tournament.get('date')}  |"
                f" {tournament.get('description')}"
            )
        input("Press Enter to continue...")

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

    def show_rounds_results(self, tournament_id) -> None:
        """Show the results of all round of the selected tournament"""
        check.clear_terminal()
        tournament_data = TOURNAMENTS.get(doc_id=tournament_id)
        round_1 = tournament_data.get("score_round_1")
        round_2 = tournament_data.get("score_round_2")
        round_3 = tournament_data.get("score_round_3")
        round_4 = tournament_data.get("score_round_4")
        print("===================")
        print("|RESULT OF ROUND 1|")
        print("===================")
        for tuple_round_1 in round_1:
            print(tuple_round_1)
        print("===================")
        print("|RESULT OF ROUND 2|")
        print("===================")
        for tuple_round_2 in round_2:
            print(tuple_round_2)
        print("===================")
        print("|RESULT OF ROUND 3|")
        print("===================")
        for tuple_round_3 in round_3:
            print(tuple_round_3)
        print("===================")
        print("|RESULT OF ROUND 4|")
        print("===================")
        for tuple_round_4 in round_4:
            print(tuple_round_4)
        print("___________________________")
        input("Press Enter to continue...")
        check.clear_terminal()

    def show_round_1_results(self, tournament_id) -> None:
        """Show the round_1 result"""
        check.clear_terminal()
        tournament_data = TOURNAMENTS.get(doc_id=tournament_id)
        round = tournament_data.get("score_round_1")
        print("===================")
        print("|RESULT OF ROUND 1|")
        print("===================")
        for tuple_round in round:
            print(tuple_round)
        print("___________________________")
        input("Press Enter to continue...")
        check.clear_terminal()

    def show_round_2_results(self, tournament_id) -> None:
        """Show the round_2 result"""
        check.clear_terminal()
        tournament_data = TOURNAMENTS.get(doc_id=tournament_id)
        round = tournament_data.get("score_round_2")
        print("===================")
        print("|RESULT OF ROUND 2|")
        print("===================")
        for tuple_round in round:
            print(tuple_round)
        print("___________________________")
        input("Press Enter to continue...")
        check.clear_terminal()

    def show_round_3_results(self, tournament_id) -> None:
        """Show the round_3 result"""
        check.clear_terminal()
        tournament_data = TOURNAMENTS.get(doc_id=tournament_id)
        round = tournament_data.get("score_round_3")
        print("===================")
        print("|RESULT OF ROUND 3|")
        print("===================")
        for tuple_round in round:
            print(tuple_round)
        print("___________________________")
        input("Press Enter to continue...")
        check.clear_terminal()

    def show_round_4_results(self, tournament_id) -> None:
        """Show the round_4 result"""
        check.clear_terminal()
        tournament_data = TOURNAMENTS.get(doc_id=tournament_id)
        round = tournament_data.get("score_round_4")
        print("===================")
        print("|RESULT OF ROUND 4|")
        print("===================")
        for tuple_round in round:
            print(tuple_round)
        print("___________________________")
        input("Press Enter to continue...")
        check.clear_terminal()
