from behave import *
from ChessGame.board_manager import *
from ChessGame.pieces import *

@given("'Pawn_Player' has an empty chess board with dimensons '8' by '8'")
def step_create_an_eight_by_eight_chess_board(context):
    context.chess_board = BoardManager(8, 8)
