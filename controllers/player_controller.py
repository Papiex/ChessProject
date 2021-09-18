from models.player_model import Player

from data import PLAYERS


class PlayerController:
    """Player controller"""
    def __init__(self, view) -> None:
        self.view = view

    def get_info_player(self) -> None:
        """Get the user entry info and create a player"""

        first_name, last_name, birthday, genre = self.view.ask_info_player()
        ranking = 0
        player = Player(first_name, last_name, birthday, genre, ranking)
        player.save()

    def instantiates_players(self) -> dict:
        """instantiates 8 players selected by the user in a dict"""

        players_list = self.view.create_players_id_dict()
        for key in players_list:
            player_data = PLAYERS.get(doc_id=players_list.get(key))
            players_list[key] = Player(
                first_name=player_data.get("first_name"),
                last_name=player_data.get("last_name"),
                birthday=player_data.get("birthday"),
                genre=player_data.get("genre"),
                ranking=player_data.get("ranking"),
            )
        return players_list
