



class Player:

    def __init__(self, first_name, last_name, birthday, genre) -> None:
        """Class defining a player with first and last name, birthday, genre and his ranking"""
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.genre = genre
        #self.ranking = ranking

class Tournament:

    def __init__(self, name, place, date) -> None:
        """Class defining a tournament with name, place, the date, defaut rounds number, current round, list of the
           players, time and description"""
        self.name = name
        self.place = place
        self.date = date
        self.rounds_number = 4
        self.current_round = 0
        #self.players = players
        #self.time = time
        #self.description = description

class Match:
    pass

class Round:
    pass