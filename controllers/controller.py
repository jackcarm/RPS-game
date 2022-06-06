from flask import render_template

from app import app
from models.player import *
from models.game import *
from models.player_list import *


# from models.game_moves import


@app.route("/rock/scissors")
def play_game(rock, scissors):
    player1 = Player("Player 1", "rock")
    player2 = Player("Player 2", "scissors")
    game = Game()
    winner = game.play_game(player1, player2)
    return render_template(
        "index.html", player1=player1, player2=player2, winner=winner
    )
