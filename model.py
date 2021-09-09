from data import TOURNAMENTS, PLAYERS


class Player:
    """Class defining a player with first and last name, birthday, genre and his ranking"""
    def __init__(self, first_name, last_name, birthday, genre, ranking) -> None:

        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.genre = genre
        self.ranking = ranking

    def save(self) -> None:
        """Save the info of a player"""
        PLAYERS.insert({
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthday": self.birthday,
            "genre": self.genre,
            "ranking": self.ranking
        })

    def __repr__(self):
        """redifining repr method for print cleaned data"""
        rep = "{} {} | {} | {} | {}".format(self.first_name, self.last_name, self.birthday, self.genre, self.ranking)
        return rep


class Tournament:
    """Class defining a tournament with name, place, the date, defaut rounds number, current round, list of the
       players, time and description"""
    def __init__(self, name, place, date, time, description) -> None:

        self.name = name
        self.place = place
        self.date = date
        self.rounds_number = 4
        self.current_round = 1
        self.players = {}
        self.time = time
        self.description = description

    def save(self) -> None:
        """Save the info in tournaments.json"""
        TOURNAMENTS.insert({
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "players": self.players,
            "time": self.time,
            "description": self.description
            })

    def __repr__(self):
        """"""
        players = []
        for player in self.players:
            players.append(player.first_name)
        return players


class Round:
    """Class defining a round"""

    def __init__(self, players) -> None:
        self.players = players
