from models.player_model import Player


class RoundView:
    """Round view"""

    def request_specific_number_only(self, player_a: Player, player_b: Player) -> float:
        """request user entry for specific number only, player_a and player_b parameter is for print player name"""
        print(str(player_a.first_name) + " versus " + str(player_b.first_name))
        print(
            "Enter the result of " + str(player_a.first_name) + " : \n"
            "| 1   - for winner   |\n"
            "| 0.5 - for equality |\n"
            "| 0   - for defeated |"
        )

        while True:
            result = input()
            result = float(result)
            if result == 1:
                return result
            elif result == 0.5:
                return result
            elif result == 0:
                return result
            else:
                print("You must enter [1], [0.5] or [0] : ")

    def request_id(self, data_file) -> int:
        """request user entry for integer only"""
        while True:
            try:
                id_choice = int(input())
            except ValueError:
                print("Enter only numbers : ")

            object_counter = 0
            for object in data_file:
                object_counter += 1
            if id_choice > object_counter:
                print("Select a valid id : ")
            elif id_choice == 0:
                print("Select a valid id : ")
            else:
                return id_choice
