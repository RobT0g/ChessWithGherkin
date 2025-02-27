import time
from behave import *
from ChessGame.pieces import *
from ChessGame.board_manager import *

step_latency = 2

@given("'Pawn_Player' has an empty chess board with dimensons '8' by '8'")
def step_create_an_eight_by_eight_chess_board(context):
    context.chess_board = BoardManager(8, 8)
    print('Created an 8x8 chess board')

@given("'Pawn_Player' adds a 'Pawn' in position '6' '6' with color 'White'")
def step_add_a_white_pawn_in_pos_6_6(context):
    context.chess_board.board[6][6] = Pawn(True)
    context.chess_board.board[6][6].x = 6
    context.chess_board.board[6][6].y = 6
    print('Added a white pawn in position 6 6')
    print(context.chess_board.board[6][6])
    
@when("'Pawn_Player' clicks on the 'Pawn' in position '6' '6'")
def step_pawn_player_clicks_on_pawn_in_pos_6_6(context):
    context.chess_board.on_click((6, 6), False)
    print('Clicked on the white pawn in position 6 6')
    print(f'Is it my turn: {context.chess_board.player_turn}')
    print(f'Highlighted moves: {context.chess_board.highlighted_moves}')
    print(f'Highlighted attacks: {context.chess_board.highlighted_attacks}')

@then("'Pawn_Player' should see square '5' '6' highlighted in 'green'")
def step_pawn_player_should_see_square_5_6_highlighted(context):
    print('Checking if square 5 6 is highlighted')
    assert (5, 6) in context.chess_board.highlighted_moves

@then("'Pawn_Player' should see square '4' '6' highlighted in 'green'")
def step_pawn_player_should_see_square_4_6_highlighted(context):
    print('Checking if square 4 6 is highlighted')
    assert (4, 6) in context.chess_board.highlighted_moves


