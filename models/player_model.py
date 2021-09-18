from data import PLAYERS


class Player:
    """Class defining a player with first and last name, birthday, genre and his ranking"""
    def __init__(self, first_name, last_name, birthday, genre, ranking, faced_players=[], tournament_score=0) -> None:

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
        })

    def add_faced_player(self, player) -> None:
        """Save a faced player in a list"""
        self.faced_players.append(player)

    def __repr__(self):
        """redifining repr method for print cleaned data"""
        return f"{self.first_name} {self.last_name} | {self.birthday} | {self.genre} | {self.ranking}"
