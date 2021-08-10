from tinydb import TinyDB


TOURNAMENTS_DATA = TinyDB("tournaments.json")
TOURNAMENTS = TOURNAMENTS_DATA.table("Tournaments")
PLAYERS_DATA = TinyDB("players.json")
PLAYERS = PLAYERS_DATA.table("Players")
