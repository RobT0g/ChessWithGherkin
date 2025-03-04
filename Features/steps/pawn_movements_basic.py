import time
from behave import *
from pieces import *
from board_manager import *

@given("'Pawn_Player_2' has an empty chess board with dimensons '8' by '8'")
def step_pawn_2_create_an_eight_by_eight_chess_board(context):
    context.chess_board = BoardManager(8, 8)
    print('Created an 8x8 chess board')

@given("'Pawn_Player_2' adds a 'Pawn' in position {row} {column} with color 'White'")
def step_pawn_2_add_a_white_pawn_in_pos(context, row, column):
    row, column = int(row), int(column)
    context.chess_board.board[row][column] = Pawn(True)
    context.chess_board.board[row][column].x = row
    context.chess_board.board[row][column].y = column
    print(f'Added a white pawn in position {row} {column}')
    print(context.chess_board.board[row][column])

@given ("'Pawn_Player_2' has clicked on the 'Pawn' in position {row} {column}")
def step_pawn_2_has_clicked_on_pawn_in_pos(context, row, column):
    step_pawn_2_clicks_on_pawn_in_pos(context, row, column)

@given("'Pawn_Player_2' sees the square {row} {column} highlighted in 'yellow'")
def step_pawn_2_sees_square_highlighted(context, row, column):
    row, column = int(row), int(column)
    step_pawn_2_should_see_square_highlighted_in_yellow(context, row, column)

@given("'Pawn_Player_2' sees the square {row} {column} highlighted in 'green'")
def step_pawn_2_sees_square_highlighted(context, row, column):
    row, column = int(row), int(column)
    step_pawn_2_should_see_square_highlighted_in_green(context, row, column)

@when("'Pawn_Player_2' clicks on the 'Pawn' in position {row} {column}")
def step_pawn_2_clicks_on_pawn_in_pos(context, row, column):
    row, column = int(row), int(column)
    context.chess_board.on_click((row, column), False)
    print(f'Clicked on the white pawn in position {row} {column}')
    print(f'Is it my turn: {context.chess_board.player_turn}')
    print(f'Highlighted moves: {context.chess_board.highlighted_moves}')
    print(f'Highlighted attacks: {context.chess_board.highlighted_attacks}')

@when("'Pawn_Player_2' clicks on the highlighted square {row} {column}")
def step_pawn_2_clicks_on_highlighted_square(context, row, column):
    row, column = int(row), int(column)
    context.chess_board.on_click((row, column), False)
    print(f'Clicked on the highlighted square {row} {column}')
    print(f'Is it my turn: {context.chess_board.player_turn}')
    print(f'Highlighted moves: {context.chess_board.highlighted_moves}')
    print(f'Highlighted attacks: {context.chess_board.highlighted_attacks}')

@then("'Pawn_Player_2' should see square {row} {column} highlighted in 'yellow'")
def step_pawn_2_should_see_square_highlighted_in_yellow(context, row, column):
    row, column = int(row), int(column)
    print(f'Checking if square {row} {column} is highlighted')
    assert (row, column) == context.chess_board.highlighted_piece.get_piece_position()

@then("'Pawn_Player_2' should see square {row} {column} highlighted in 'green'")
def step_pawn_2_should_see_square_highlighted_in_green(context, row, column):
    row, column = int(row), int(column)
    print(f'Checking if square {row} {column} is highlighted')
    assert (row, column) in context.chess_board.highlighted_moves

@then("'Pawn_Player_2' shold see 'Pawn' move from the square {row_init} {column_init} to the square {row_to_move} {column_to_move}")
def step_pawn_2_should_see_pawn_move_to_square(context, row_init, column_init, row_to_move, column_to_move):
    row_init, column_init, row_to_move, column_to_move = int(row_init), int(column_init), int(row_to_move), int(column_to_move)
    print(f'Checking if the pawn moved from {row_init} {column_init} to {row_to_move} {column_to_move}')
    assert not context.chess_board.highlighted_piece
    assert not context.chess_board.board[row_init][column_init]
    assert context.chess_board.board[row_to_move][column_to_move]
    assert context.chess_board.board[row_to_move][column_to_move].player

@then("'Pawn_Player_2' should see square {row} {column} no longer highlighted")
def step_pawn_2_should_see_square_no_longer_highlighted(context, row, column):
    row, column = int(row), int(column)
    print(f'Checking if square {row} {column} is no longer highlighted')
    assert not context.chess_board.highlighted_piece
    assert (row, column) not in context.chess_board.highlighted_moves
    assert (row, column) not in context.chess_board.highlighted_attacks
