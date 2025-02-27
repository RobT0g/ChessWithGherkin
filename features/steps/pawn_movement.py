import time
from behave import *
from ChessGame.pieces import *
from ChessGame.board_manager import *

@given("'Pawn_Player' has an empty chess board with dimensons '8' by '8'")
def step_create_an_eight_by_eight_chess_board(context):
    context.chess_board = BoardManager(8, 8)
    print(context.chess_board.board)
    context.chess_board.display_board()
    time.sleep(1)

@given("'Pawn_Player' adds a 'Pawn' in position '6' '6' with color 'White'")
def step_add_a_white_pawn_in_pos_6_6(context):
    context.chess_board.board[6][6] = Pawn(True)
    context.chess_board.board[6][6].x = 6
    context.chess_board.board[6][6].y = 6
    
    context.chess_board.display_board()
    time.sleep(1)
