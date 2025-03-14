import time
from behave import *
from pieces import *
from board_manager import *

def check_piece_in_pos(context, row:int, column:int, piece_name:str, piece_color:str, check_not_there:bool=False):
    '''
        Common function to check if a piece is in a given position.
        Note: Will return error if used to check an empty square.
        Args:
            context (object): The context object.
            row (int): The row of the piece.
            column (int): The column of the piece.
            piece_name (str): The name of the piece.
            piece_color (str): The color of the piece.
            check_not_there (bool, optional): Set to True if the piece should not be there. Defaults to False.
    '''

    row, column = int(row), int(column)
    if not check_not_there and context.chess_board.board[row][column] is None:
        assert False, f'Square {row} {column} is empty'

    elif check_not_there:
        return

    assert (context.chess_board.board[row][column].get_icon_name() == f'{piece_name}_{piece_color[0]}') != check_not_there, f'Piece name not matching: {context.chess_board.board[row][column].get_icon_name()} should {"not" if check_not_there else ""}be {piece_name}_{piece_color[0]}'
    assert (context.chess_board.board[row][column].player == (piece_color == 'White')) != check_not_there, f'Piece color not matching: {context.chess_board.board[row][column].player} should {"not" if check_not_there else ""}be {"White"  if piece_color else "Black"}'

def check_square_highlighted_in_yellow(context, row:int, column:int) -> bool:
    '''
        Check if a square is highlighted in yellow
        Args:
            context: The context object
            row (int): The row of the square
            column (int): The column of the square
        Returns:
            bool: True if the square is highlighted in yellow, False otherwise
    '''
    if not context.chess_board.highlighted_piece:
        return False
    
    return context.chess_board.highlighted_piece.get_piece_position() == (row, column)

def check_square_highlighted_in_green(context, row:int, column:int) -> bool:
    '''    
        Check if a square is highlighted in green.
            context: The test context containing the chess board.
            row (int): The row index of the square.
            column (int): The column index of the square.
        Returns:
            bool: True if the square is highlighted in green, False otherwise.
    '''
   
    return (row, column) in context.chess_board.highlighted_moves

def check_square_highlighted_in_red(context, row:int, column:int) -> bool:
    """
    Checks if a specific square on the chess board is highlighted in red.
    Args:
        context: The context object containing the chess board state.
        row (int): The row index of the square to check.
        column (int): The column index of the square to check.
    Returns:
        bool: True if the square is highlighted in red, False otherwise.
    """

    return (row, column) in context.chess_board.highlighted_attacks

def check_square_is_not_highlighted(context, row:int, column:int) -> bool:
    """
    Checks if a specific square on the chessboard is not highlighted in any color.
    Args:
        context: The context object containing the state of the chessboard.
        row (int): The row index of the square to check.
        column (int): The column index of the square to check.
    Returns:
        bool: True if the square is not highlighted in yellow, green, or red; False otherwise.
    """


    is_highlighted = False
    is_highlighted |= check_square_highlighted_in_yellow(context, row, column)
    is_highlighted |= check_square_highlighted_in_green(context, row, column)
    is_highlighted |= check_square_highlighted_in_red(context, row, column)
    return not is_highlighted
    
def get_positions_list_from_string(squares:str) -> list[tuple[int]]:
    """
    Converts a string representation of chessboard positions into a list of tuples.
    Args:
        squares (str): A string containing chessboard positions in the format 
                        "(x1, y1), (x2, y2), ...]".
    Returns:
        list[tuple[int]]: A list of tuples where each tuple represents a position 
                            on the chessboard as (x, y).
    """

    squares = squares.replace('[', '').replace(']', '').replace('(', '').replace(')', '').replace(' ', '')
    positions = squares.split(',')
    return [(int(positions[i*2]), int(positions[i*2+1])) for i in range(len(positions)//2)]

@given("I have an empty chess board with dimensons {length} by {width}")
def step_create_chess_board_with_dimensions(context, length:int, width:int):
    context.chess_board = BoardManager(int(length.replace("'", '')), int(width.replace("'", '')))
    print(f'Created a {length}x{width} chess board')

@given("I add a {piece_type} in position {row} {column} with color {piece_color}")
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
    check_piece_in_pos(context, row, column, piece_type, piece_color)

@given("it is {piece_color} turn to play")
def step_set_player_turn(context, piece_color:str):
    context.chess_board.player_turn = piece_color.replace("'", '') == 'White'
    print(f"It's {piece_color} turn to play")

@given ("I have clicked on the {piece_color} {piece_type} in position {row} {column}")
def step_i_clicked_on_piece_in_pos(context, piece_color:str, piece_type:str, row:int, column:int):
    row, column = int(row.replace("'", '')), int(column.replace("'", ''))
    piece_type = piece_type.replace("'", '')
    piece_color = piece_color.replace("'", '')

    check_piece_in_pos(context, row, column, piece_type, piece_color)
    context.chess_board.on_click((row, column), False)
    print(f'Clicked on the {piece_color} {piece_type} in position {row} {column}')

@given("I see the square {row} {column} highlighted in {highlight_color}")
def step_i_see_square_highlighted_in_yellow(context, row, column, highlight_color):
    row, column = int(row.replace("'", '')), int(column.replace("'", ''))
    highlight_color = highlight_color.replace("'",'')
    if highlight_color == 'yellow':
        assert check_square_highlighted_in_yellow(context, row, column), f'Square {row} {column} not highlighted in yellow'

    elif highlight_color == 'green':
        assert check_square_highlighted_in_green(context, row, column), f'Square {row} {column} not highlighted in green'

    elif highlight_color == 'red':
        assert check_square_highlighted_in_red(context, row, column), f'Square {row} {column} not highlighted in red'

    else:
        assert False, f'Invalid highlight color: {highlight_color}'
    
@given("I see all the squares in the list {squares} highlighted in {highlight_color}")
def step_i_see_squares_highlighted_in_color(context, squares, highlight_color):
    squares = get_positions_list_from_string(squares)
    highlight_color = highlight_color.replace("'", '')
    
    highlight_function = None    
    match highlight_color:
        case 'yellow':
            highlight_function = check_square_highlighted_in_yellow

        case 'green':
            highlight_function = check_square_highlighted_in_green

        case 'red':
            highlight_function = check_square_highlighted_in_red

        case _:
            assert False, f'Invalid highlight color: {highlight_color}'

    for l in range(context.chess_board.board_length):
        for w in range(context.chess_board.board_width):
            assert highlight_function(context, l, w) == ((l, w) in squares), f'Square {l} {w} {"" if highlight_function(context, l, w) else "not "}highlighted in {highlight_color}'

@given("the {piece_color} {piece_type} in position {row} {column} has already moved")
def step_set_piece_as_already_moved(context, piece_color, piece_type, row, column):
    row, column = int(row.replace("'", '')), int(column.replace("'", ''))
    piece_type = piece_type.replace("'", '')
    piece_color = piece_color.replace("'", '')
    check_piece_in_pos(context, row, column, piece_type, piece_color)

    piece = context.chess_board.board[row][column]
    piece.has_moved = True
    print(f'Set the {piece_color} {piece_type} in position {row} {column} as already moved')

@given("I click on the square {row} {column}")
def step_i_click_on_square(context, row, column):
    row, column = int(row.replace("'", '')), int(column.replace("'", ''))
    
    context.chess_board.on_click((row, column), False)
    print(f'Clicked on the square {row} {column}')
    print(f'> Is it my turn: {context.chess_board.player_turn}')
    print(f'> Highlighted moves: {context.chess_board.highlighted_moves}')
    print(f'> Highlighted attacks: {context.chess_board.highlighted_attacks}\n')

@given("I see the {piece_color} {piece_type} in position {row} {column}")
def step_i_see_piece_in_position(context, piece_color, piece_type, row, column):
    row, column = int(row.replace("'", '')), int(column.replace("'", ''))
    piece_type = piece_type.replace("'", '')
    piece_color = piece_color.replace("'", '')
    check_piece_in_pos(context, row, column, piece_type, piece_color)

@given("I get prompted with an option to choose which piece to promote the {piece_color} 'Pawn' on square {row} {column} to")
def step_i_get_prompted_with_promotion_options(context, piece_color, row, column):
    row, column = int(row.replace("'", '')), int(column.replace("'", ''))
    piece_color = piece_color.replace("'", '')
    check_piece_in_pos(context, row, column, 'Pawn', piece_color)

    assert context.chess_board.promotion_options, 'No promotion options available'
    assert context.chess_board.play_state == 'Promotion', f'Playstate not set to Promotion: {context.chess_board.playstate}'
    assert context.chess_board.player_turn == (piece_color == 'White'), f'Player turn not set correctly: {context.chess_board.player_turn}'
    print(f'Promotion options: {context.chess_board.promotion_options}')

@when("I click on the square {row} {column}")
def step_i_click_on_square_when(context, row, column):
    step_i_click_on_square(context, row, column)

@when("I choose to promote the pawn to a {promotion_piece}")
def step_i_choose_pawn_promotion(context, promotion_piece):
    promotion_options = ['Queen', 'Rook', 'Bishop', 'Knight']
    promotion_piece = promotion_options.index(promotion_piece.replace("'", ''))
    row_to_click = (promotion_piece//2)*75 + context.chess_board.screen_size[0]//2 - 75 + 30
    column_to_click = (promotion_piece%2)*75 + context.chess_board.screen_size[1]//2 - 75 + 30

    context.chess_board.on_click((row_to_click, column_to_click), False)
    print(f'Chose to promote the pawn to a {promotion_options[promotion_piece]} by clicking on {row_to_click} {column_to_click}')

@then("I shold see the {piece_color} {piece_type} move from the square {row_init} {column_init} to the square {row_to_move} {column_to_move}")
def step_i_should_see_piece_move_to_square(context, piece_color, piece_type, row_init, column_init, row_to_move, column_to_move):
    row_init = int(row_init.replace("'", ''))
    column_init = int(column_init.replace("'", ''))
    row_to_move = int(row_to_move.replace("'", ''))
    column_to_move = int(column_to_move.replace("'", ''))
    piece_type = piece_type.replace("'", '')
    piece_color = piece_color.replace("'", '')

    print(f'Checking if the {piece_color} {piece_type} moved from {row_init} {column_init} to {row_to_move} {column_to_move}')
    assert not context.chess_board.highlighted_piece or context.chess_board.play_state != 'Playing', 'Highlighted piece not removed'
    assert not context.chess_board.board[row_init][column_init]
    assert context.chess_board.board[row_to_move][column_to_move]
    check_piece_in_pos(context, row_to_move, column_to_move, piece_type, piece_color)

@then("there should not be any squares highlighted in any color")
def step_i_should_see_no_squares_highlighted(context):
    print('Checking if there are no more squares highlighted')
    assert not context.chess_board.highlighted_piece
    assert not context.chess_board.highlighted_moves
    assert not context.chess_board.highlighted_attacks 

@then("I shold see the {piece_color} {piece_type} removed from the square {row} {column}")
def step_check_piece_was_removed_from_square(context, piece_color, piece_type, row, column):
    row, column = int(row.replace("'", '')), int(column.replace("'", ''))
    piece_type = piece_type.replace("'", '')
    piece_color = piece_color.replace("'", '')

    print(f'Checking if the {piece_color} {piece_type} was removed from {row} {column}')
    check_piece_in_pos(context, row, column, piece_type, piece_color, True)

@then("I should get prompted with an option to choose which piece to promote the {piece_color} 'Pawn' on square {row} {column} to")
def step_check_promotion_options(context, piece_color, row, column):
    row, column = int(row.replace("'", '')), int(column.replace("'", ''))
    piece_color = piece_color.replace("'", '')
    check_piece_in_pos(context, row, column, 'Pawn', piece_color)
    
    assert context.chess_board.highlighted_piece == context.chess_board.board[row][column], 'Highlighted piece not set correctly'
    assert context.chess_board.promotion_options, 'No promotion options available'
    assert context.chess_board.play_state == 'Promotion', f'Playstate not set to Promotion: {context.chess_board.playstate}'
    assert context.chess_board.player_turn == (piece_color == 'White'), f'Player turn not set correctly: {context.chess_board.player_turn}'
    print(f'Promotion options: {context.chess_board.promotion_options}')

@then("I should see a {piece_color} {promotion_piece} on the square {row} {column}")
def step_i_should_see_a_piece_on_square(context, piece_color, promotion_piece, row, column):
    row, column = int(row.replace("'", '')), int(column.replace("'", ''))
    promotion_piece = promotion_piece.replace("'", '')
    piece_color = piece_color.replace("'", '')

    print(f'Checking if the {piece_color} {promotion_piece} is on the square {row} {column}')
    check_piece_in_pos(context, row, column, promotion_piece, piece_color)

@then("it should no longer be {piece_color} turn to play")
def step_check_player_turn(context, piece_color):
    print(f'Checking if it is still {piece_color} turn to play')
    assert context.chess_board.player_turn != (piece_color == 'White'), f'Player turn not set correctly: {context.chess_board.player_turn}'
