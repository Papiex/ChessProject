from data import TOURNAMENTS


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
