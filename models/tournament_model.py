from models.player_model import Player
from data import TOURNAMENTS

from typing import Union

from tinydb import where

import json


class Tournament:
    """Class defining a tournament with name, place, the date, defaut rounds number, current round, list of the
       players, time and description"""
    def __init__(self, name, place, date, time, description) -> None:

        self.name = name
        self.place = place
        self.date = date
        self.current_round = 1
        self.players = {}
        self.players_round_list = []
        self.time = time
        self.description = description
        self.score_round_1 = []
        self.score_round_2 = []
        self.score_round_3 = []
        self.score_round_4 = []

    def save(self) -> None:
        """Save the info in tournaments.json"""
        TOURNAMENTS.insert({
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "players": self.players,
            "time": self.time,
            "description": self.description,
            "current_round": self.current_round,
            "players_round_list": self.players_round_list,
            "score_round_1": self.score_round_1,
            "score_round_2": self.score_round_2,
            "score_round_3": self.score_round_3,
            "score_round_4": self.score_round_4
            })

    def get_actual_round(self) -> int:
        """return the actual round integer"""
        return self.current_round

    def save_actual_round(self, tournament_id) -> None:
        """save the actual round number fo the tournament in tournaments.json"""
        tournament_data = TOURNAMENTS.get(doc_id=tournament_id)
        TOURNAMENTS.update(
            {"current_round": self.current_round},
            where("current_round") == tournament_data.get("current_round"))

    def save_players_for_next_round(self, players_list: list[Player], tournament_id):
        """save and serialize players_list to resume rounds"""
        tournament_data = TOURNAMENTS.get(doc_id=tournament_id)
        self.players_round_list = []
        for player in players_list:
            player = player.serialize()
            self.players_round_list.append(player)
        TOURNAMENTS.update(
            {"players_round_list": self.players_round_list},
            where("players_round_list") == tournament_data.get("players_round_list"))

    def get_players_for_continue_tournament(self, tournament_id):
        """load and instantiate player from the tournament started previously"""
        tournament_data = TOURNAMENTS.get(doc_id=tournament_id)
        players_list = tournament_data.get("players_round_list")
        deserialized_players_list = []
        for player_data in players_list:
            player = Player(**json.loads(player_data))
            deserialized_players_list.append(player)
        return deserialized_players_list

    @staticmethod
    def deserialize_tournament(cls, tournament_id: int) -> Union["Tournament", int]:
        """deserialize a tournament saved in tournaments.json and instantiate it"""
        tournament_data = TOURNAMENTS.get(doc_id=tournament_id)
        tournament = cls(
            name=tournament_data.get("name"),
            place=tournament_data.get("place"),
            date=tournament_data.get("date"),
            time=tournament_data.get("time"),
            description=tournament_data.get("description"),
        )
        tournament.current_round = tournament_data.get("current_round")
        tournament.players_round_list = tournament_data.get("players_round_list")
        return tournament
