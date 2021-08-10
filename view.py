from data import TOURNAMENTS


class View:

    def menu(self) -> str:
        """Main menu of the program"""
        print(
            "1 - Create a tournament \n"
            "2 - Show all tournaments \n"
            "3 - Add a player to database \n"
            "4 - Show all saved players")
        response = input("Choose a number to browse the menu")
        return response

    def ask_info_tournament(self) -> str:
        """Get info of a tournament"""
        name = input("Hit the name of the tournament : ")
        place = input("Hit the place of the tournament : ")
        date = input("Enter the date with this format XX/XX/XXXX : ")
        description = input("Hit a description : ")
        return name, place, date, description

    def show_tournaments(self) -> None:
        """Show all the tournaments saved in tournaments.json"""
        for tournaments in TOURNAMENTS:
            print(tournaments)

    def ask_info_player(self) -> str:
        """Get info of a player"""
        first_name = input("Enter the first name : ")
        last_name = input("Enter the last_name : ")
        birthday = input("Enter date of birth with this format XX/XX/XXXX :  ")
        genre = input("Enter 'M' for man and 'W' for woman : ")
        return first_name, last_name, birthday, genre
