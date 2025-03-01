import time
from behave import *
from pieces import *
from board_manager import *

def check_piece_in_pos(context, row:int, column:int, piece_name:str, piece_color:str):
    row, column = int(row), int(column)
    assert context.chess_board.board[row][column], 'Piece not added'
    assert context.chess_board.board[row][column].get_name == piece_name, 'Piece name not set'
    assert context.chess_board.board[row][column].player == piece_color, 'Piece color not set'

def check_square_highlighted_in_yellow(context, row:int, column:int) -> bool:
    if not context.chess_board.highlighted_piece:
        return False
    
    return context.chess_board.highlighted_piece.get_piece_position() == (row, column)

def check_square_highlighted_in_green(context, row:int, column:int) -> bool:
    return (row, column) in context.chess_board.highlighted_moves

def check_square_highlighted_in_red(context, row:int, column:int) -> bool:
    return (row, column) in context.chess_board.highlighted_attacks

def check_square_is_not_highlighted(context, row:int, column:int) -> bool:
    is_highlighted = False
    is_highlighted |= check_square_highlighted_in_yellow(context, row, column)
    is_highlighted |= check_square_highlighted_in_green(context, row, column)
    is_highlighted |= check_square_highlighted_in_red(context, row, column)
    return not is_highlighted
    
def get_positions_list_from_string(squares:str) -> list[tuple[int]]:
    squares = squares.replace('[', '').replace(']', '').replace('(', '').replace(')', '').replace(' ', '')
    positions = squares.split(',')
    return [(int(positions[i*2]), int(positions[i*2+1])) for i in range(len(positions)//2)]

@given("I have an empty chess board with dimensons {length} by {width}")
def step_create_chess_board_with_dimensions(context, length:int, width:int):
    context.chess_board = BoardManager(length, width)
    print(f'Created a {length}x{width} chess board')

@given("'I add a {piece_type} in position {row} {column} with color {piece_color}")
def step_add_a_piece_in_pos(context, piece_type:str, row:int, column:int, piece_color:str):
    row, column = int(row.replace("'", '')), int(column.replace("'", ''))
    piece_type = piece_type.replace("'", '')
    piece_color = piece_color.replace("'", '')
    is_white_piece = piece_color == 'White'
    piece = None
    
    match piece_type:
        case 'Pawn':
            piece = Pawn(is_white_piece)

        case 'Rook':
            piece = Rook(is_white_piece)

        case 'Knight':
            piece = Knight(is_white_piece)
        
        case 'Bishop':
            piece = Bishop(is_white_piece)

        case 'Queen':
            piece = Queen(is_white_piece)

        case 'King':
            piece = King(is_white_piece)

        case _:
            assert False, f"Invalid piece type: {piece_type}"

    context.chess_board.board[row][column] = piece
    piece.x = row
    piece.y = column
    print(f'Added a {piece_color} {piece_type} in position {row} {column}')
    check_piece_in_pos(context, row, column, piece_type, is_white_piece)

@given ("I have clicked on the {piece_color} {piece_type} in position {row} {column}")
def step_i_clicked_on_piece_in_pos(context, piece_color:str, piece_type:str, row:int, column:int):
    row, column = int(row.replace("'", '')), int(column.replace("'", ''))
    piece_type = piece_type.replace("'", '')
    piece_color = piece_color.replace("'", '')

    check_piece_in_pos(context, row, column, piece_type, piece_color)
    context.chess_board.on_click((row, column), False)
    print(f'Clicked on the {piece_color} {piece_type} in position {row} {column}')

@given("I see the square {row} {column} highlighted in 'yellow'")
def step_i_see_square_highlighted_in_yellow(context, row, column):
    row, column = int(row.replace("'", '')), int(column.replace("'", ''))
    assert check_square_highlighted_in_yellow(context, row, column), f'Square {row} {column} not highlighted in yellow'
    try:
        print(context.chess_board.highlighted_piece.get_piece_position())
    except:
        print(f'No highlighted piece')

@given("I see all the squares in the list {squares} highlighted in {highlight_color}")
def step_pawn_2_sees_square_highlighted(context, squares, highlight_color):
    squares = get_positions_list_from_string(squares)
    for square in squares:
        row, column = square
        
        if highlight_color == 'yellow':
            assert check_square_highlighted_in_yellow(context, row, column), f'Square {row} {column} not highlighted in yellow'

        elif highlight_color == 'green':
            assert check_square_highlighted_in_green(context, row, column), f'Square {row} {column} not highlighted in green'

        elif highlight_color == 'red':
            assert check_square_highlighted_in_red(context, row, column), f'Square {row} {column} not highlighted in red'

        else:
            assert False, f'Invalid highlight color: {highlight_color}'

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
    assert not context.chess_board.board[row_to_move][column_to_move].player

@then("'Pawn_Player_2' should see square {row} {column} no longer highlighted")
def step_pawn_2_should_see_square_no_longer_highlighted(context, row, column):
    row, column = int(row), int(column)
    print(f'Checking if square {row} {column} is no longer highlighted')
    assert not context.chess_board.highlighted_piece
    assert (row, column) not in context.chess_board.highlighted_moves
    assert (row, column) not in context.chess_board.highlighted_attacks
