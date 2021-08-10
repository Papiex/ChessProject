from data import TOURNAMENTS, PLAYERS


# PLAYERS_NUMBERS = 8


class Player:
    """Class defining a player with first and last name, birthday, genre and his ranking"""
    def __init__(self, first_name, last_name, birthday, genre) -> None:

        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.genre = genre
        # self.ranking = ranking

    def save(self) -> None:
        """Save the info of a player"""
        PLAYERS.insert({
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Birthday": self.birthday,
            "Genre": self.genre
        })


class Tournament:
    """Class defining a tournament with name, place, the date, defaut rounds number, current round, list of the
       players, time and description"""
    def __init__(self, name, place, date, description) -> None:

        self.name = name
        self.place = place
        self.date = date
        self.rounds_number = 4
        self.current_round = 1
        self.players = []
        # self.time = time
        self.description = description

    def save(self) -> None:
        """Save the info in tournaments.json"""

        TOURNAMENTS.insert({
            "Name": self.name,
            "Place": self.place,
            "Date": self.date,
            "Description": self.description
            })


class Round:

    def __init__(self) -> None:
        pass


"""

Blitz = 10 min ou moins par tour
Bullet = 1 min
coup rapide = *

"""
