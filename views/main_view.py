class View:
    """Main view"""

    def main_menu(self) -> str:
        """Main menu of the program"""
        print(" ________________________________________________________________")
        print("                            MAIN MENU                            ")
        print(
            "\n"
            "                | 1 -    Create a tournament      |\n"
            "                | 2 -   Add player to database    |\n"
            "                | 3 - Add players to a Tournament |\n"
            "                | 4 -        Reports Menu         |\n"
            "                | 5 -      Exit the program       |"

            )
        print(" ________________________________________________________________")
        response = input("Choose a number to browse the menu : ")
        return response

    def report_menu(self) -> str:
        """report menu of the program"""
        print(" ________________________________________________________________")
        print("                              REPORT MENU                        ")
        print(
            "\n"
            "                | 1 -       Show all Tournaments          |\n"
            "                | 2 -      Show all saved players         |\n"
            "                | 3 - Show players of specific Tournament |\n"
            "                | 4 -      Back to the Main menu          |"
        )
        print(" ________________________________________________________________")
        response = input("Choose a number to browse a report : ")
        return response
