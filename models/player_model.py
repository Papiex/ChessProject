from data import PLAYERS
import check_functions as check
import utils

import json

from tinydb import Query


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

    def modify_player_ranking(self, player_id: int) -> None:
        """To modify manually the player ranking"""
        utils.clear_terminal()
        print(f"The general score of {self.first_name} is {str(self.ranking)}")
        print(f"Enter the new general score for {self.first_name} : ")
        new_player_score = check.request_only_numbers()
        PLAYERS.update({"ranking": new_player_score}, doc_ids=[player_id])
        print(f"The general score of {self.first_name} is now at {str(new_player_score)}")
        utils.display_enter_to_continue()

    def update_general_ranking(self) -> None:
        """Update the general ranking of a player after a tournament"""
        User = Query()
        self.ranking = self.ranking + self.tournament_score
        player_db = PLAYERS.get((User.first_name == self.first_name) & (User.last_name == self.last_name))
        player_id = player_db.doc_id
        PLAYERS.update({"ranking": self.ranking}, doc_ids=[player_id])

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

    def __repr__(self) -> str:
        """redifining repr method for print cleaned data"""
        return f"{self.first_name} {self.last_name} | {self.birthday} | {self.genre} | {self.ranking}"
