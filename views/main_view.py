from data import TOURNAMENTS

import utils


class View:
    """Main view"""

    def main_menu(self) -> str:
        """Main menu of the program"""
        utils.clear_terminal()
        print(" ________________________________________________________________")
        print("                            MAIN MENU                            ")
        print(
            "\n"
            "                | 1 -      Create a tournament         |\n"
            "                | 2 -   Add players to a Tournament    |\n"
            "                | 3 - Launch or continue a Tournament  |\n"
            "                | 4 -     Add player to database       |\n"
            "                | 5 -         Reports Menu             |\n"
            "                | 6 -       Exit the program           |"

            )
        print(" ________________________________________________________________")
        response = input("Choose a number to browse the menu : ")
        return response

    def report_menu(self) -> str:
        """report menu of the program"""
        utils.clear_terminal()
        print(" ________________________________________________________________")
        print("                              REPORT MENU                        ")
        print(
            "\n"
            "       | 1 -              Show all Tournaments               |\n"
            "       | 2 -             Show all saved players              |\n"
            "       | 3 -      Show players of specific Tournament        |\n"
            "       | 4 -  Show Round report menu of specific tournament  |\n"
            "       | 5 -             Back to the main menu               |  "
        )
        print(" ________________________________________________________________")
        response = input("Choose a number to browse a report : ")
        return response

    def round_report_menu(self, tournament_id) -> str:
        """round report menu of the programm"""
        utils.clear_terminal()
        tournament_data = TOURNAMENTS.get(doc_id=tournament_id)
        tournament_name = tournament_data.get("name")

        print(" ________________________________________________________________")
        print("                          ROUND REPORT MENU                    \n")
        print(
            "               ========================================       \n"
            "                 SELECTED TOURNAMENT : " + tournament_name + " \n"
            "               ========================================       \n"
            "\n                | 1 -     Show all Rounds results     |\n"
            "                | 2 -      Show Round 1 results       |\n"
            "                | 3 -      Show Round 2 results       |\n"
            "                | 4 -      Show Round 3 results       |\n"
            "                | 5 -      Show Round 4 results       |\n"
            "                | 6 -     Back to the report menu     |"
        )
        print(" ________________________________________________________________")
        response = input("Choose a number to browse a report : ")
        return response
