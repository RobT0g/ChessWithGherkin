import time
from behave import *
from pieces import *
from board_manager import *

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

@given("'Pawn_Player' has clicked on the 'Pawn' in position '6' '6'")
def step_pawn_player_has_clicked_on_pawn_in_pos_6_6(context):
    step_pawn_player_clicks_on_pawn_in_pos_6_6(context)

@given("'Pawn_Player' sees the square '6' '6' highlighted in 'yellow'")
def step_pawn_player_sees_square_6_6_highlighted(context):
    step_pawn_player_should_see_square_6_6_highlighted(context)

@given("'Pawn_Player' sees the square '5' '6' highlighted in 'green'")
def step_pawn_player_sees_square_5_6_highlighted(context):
    step_pawn_player_should_see_square_5_6_highlighted(context)

@given("'Pawn_Player' sees the square '4' '6' highlighted in 'green'")
def step_pawn_player_sees_square_4_6_highlighted(context):
    step_pawn_player_should_see_square_4_6_highlighted(context)

@when("'Pawn_Player' clicks on the 'Pawn' in position '6' '6'")
def step_pawn_player_clicks_on_pawn_in_pos_6_6(context):
    context.chess_board.on_click((6, 6), False)
    print('Clicked on the white pawn in position 6 6')
    print(f'Is it my turn: {context.chess_board.player_turn}')
    print(f'Highlighted moves: {context.chess_board.highlighted_moves}')
    print(f'Highlighted attacks: {context.chess_board.highlighted_attacks}')

@when("'Pawn_Player' clicks on the highlighted square '5' '6'")
def step_pawn_player_clicks_on_highlighted_square_5_6(context):
    context.chess_board.on_click((5, 6), False)
    print('Clicked on the highlighted square 5 6')
    print(f'Is it my turn: {context.chess_board.player_turn}')
    print(f'Highlighted moves: {context.chess_board.highlighted_moves}')
    print(f'Highlighted attacks: {context.chess_board.highlighted_attacks}')

@then("'Pawn_Player' should see square '6' '6' highlighted in 'yellow'")
def step_pawn_player_should_see_square_6_6_highlighted(context):
    print('Checking if square 6 6 is highlighted in yellow')
    assert (6, 6) == context.chess_board.highlighted_piece.get_piece_position()

@then("'Pawn_Player' should see square '5' '6' highlighted in 'green'")
def step_pawn_player_should_see_square_5_6_highlighted(context):
    print('Checking if square 5 6 is highlighted')
    assert (5, 6) in context.chess_board.highlighted_moves

@then("'Pawn_Player' should see square '4' '6' highlighted in 'green'")
def step_pawn_player_should_see_square_4_6_highlighted(context):
    print('Checking if square 4 6 is highlighted')
    assert (4, 6) in context.chess_board.highlighted_moves

@then("'Pawn_Player' shold see 'Pawn' move from the square '6' '6' to the square '5' '6'")
def step_pawn_player_should_see_pawn_move_from_6_6_to_5_6(context):
    print('Checking if the pawn moved from 6 6 to 5 6')
    assert not context.chess_board.board[6][6]
    assert context.chess_board.board[5][6]
    assert not context.chess_board.board[5][6].player

@then("'Pawn_Player' should see square '6' '6' no longer highlighted")
def step_pawn_player_should_see_square_6_6_no_long_longer_highlighted(context):
    print('Checking if square 6 6 is no longer highlighted')
    assert (6, 6) not in context.chess_board.highlighted_moves
    assert not context.chess_board.highlighted_piece

@then("'Pawn_Player' should see square '5' '6' no longer highlighted")
def step_pawn_player_should_see_square_5_6_no_longer_highlighted(context):
    print('Checking if square 5 6 is no longer highlighted')
    assert (5, 6) not in context.chess_board.highlighted_moves

@then("'Pawn_Player' should see square '4' '6' no longer highlighted")
def step_pawn_player_should_see_square_4_6_no_longer_highlighted(context):
    print('Checking if square 4 6 is no longer highlighted')
    assert (4, 6) not in context.chess_board.highlighted_moves


