from models.player import Player

player1 = Player("Sonic", "rock")
player2 = Player("Eggman", "scissors")
players = [player1, player2]


def get_players():
    return players


def get_players_choice():
    return players.choice
