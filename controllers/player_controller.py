from models.player_model import Player


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

    def instantiates_players(self) -> list[Player]:
        """deserialize 8 players selected by the user in a dict"""
        deserialized_players_list = []
        players_ids_list = self.view.create_players_id_dict()
        for player_id in players_ids_list:
            player = Player.deserialize_player(Player, player_id)
            deserialized_players_list.append(player)

        return deserialized_players_list
