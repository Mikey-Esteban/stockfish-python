from flask import Flask
from stockfish import Stockfish

stockfish = Stockfish('Stockfish-sf_14.1/src/stockfish')

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/fen/<fen_with_periods>")
def find_best_move(fen_with_periods):
    fen = fen_with_periods.replace(".", "/")
    stockfish.set_fen_position(fen)

    return stockfish.get_best_move()
