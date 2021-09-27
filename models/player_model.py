from data import PLAYERS

import json


class Player:
    """Class defining a player with first and last name, birthday, genre and his ranking"""
    def __init__(self, first_name, last_name, birthday, genre, ranking, faced_players, tournament_score=0) -> None:

        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.genre = genre
        self.ranking = ranking
        self.faced_players = faced_players
        self.tournament_score = tournament_score

    def save(self) -> None:
        """Save the info of a player"""
        PLAYERS.insert({
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthday": self.birthday,
            "genre": self.genre,
            "ranking": self.ranking,
            "faced_players": self.faced_players
        })

    def serialize(self) -> dict:
        """serialize a player"""
        serialized_player = json.dumps(self.__dict__)
        return serialized_player

    @staticmethod
    def deserialize_player(cls, key: int) -> "Player":
        """deserialize one player and instantiate it"""
        player_data = PLAYERS.get(doc_id=key)
        player = cls(
            first_name=player_data.get("first_name"),
            last_name=player_data.get("last_name"),
            birthday=player_data.get("birthday"),
            genre=player_data.get("genre"),
            ranking=player_data.get("ranking"),
            faced_players=player_data.get("faced_players")
        )
        return player

    @staticmethod
    def deserialize_player_for_next_round(cls, player_dict) -> "Player":
        """deserialize one player and instantiate it"""
        player = cls(
            first_name=player_dict.get("first_name"),
            last_name=player_dict.get("last_name"),
            birthday=player_dict.get("birthday"),
            genre=player_dict.get("genre"),
            ranking=player_dict.get("ranking"),
        )
        player.faced_players = player_dict.get("faced_players")
        return player

    def __repr__(self):
        """redifining repr method for print cleaned data"""
        return f"{self.first_name} {self.last_name} | {self.birthday} | {self.genre} | {self.ranking}"
