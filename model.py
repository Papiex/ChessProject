from data import TOURNAMENTS, PLAYERS


class Player:
    """Class defining a player with first and last name, birthday, genre and his ranking"""
    def __init__(self, first_name, last_name, birthday, genre) -> None:

        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.genre = genre
        self.ranking = 0

    def save(self) -> None:
        """Save the info of a player"""
        PLAYERS.insert({
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthday": self.birthday,
            "genre": self.genre,
            "ranking": self.ranking
        })


class Tournament:
    """Class defining a tournament with name, place, the date, defaut rounds number, current round, list of the
       players, time and description"""
    def __init__(self, name, place, date, players, time, description) -> None:

        self.name = name
        self.place = place
        self.date = date
        self.rounds_number = 4
        self.current_round = 1
        self.players = players
        self.time = time
        self.description = description

    def save(self) -> None:
        """Save the info in tournaments.json"""
        TOURNAMENTS.insert({
            "Name": self.name,
            "Place": self.place,
            "Date": self.date,
            "Time": self.time,
            "Description": self.description
            })


class Round:
    """Class defining a round"""

    def __init__(self, players) -> None:
        self.players = players
