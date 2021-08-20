from tinydb import TinyDB


TOURNAMENTS_DATA = TinyDB("tournaments.json")
TOURNAMENTS = TOURNAMENTS_DATA.table("Tournaments")
PLAYERS_DATA = TinyDB("players.json")
PLAYERS = PLAYERS_DATA.table("Players")

PLAYERS_NUMBERS = 1


def get_field_data(field_name, table_name) -> list:
    """extract field data from table"""
    result = [r[field_name] for r in table_name]
    print(type(result))
    return result
