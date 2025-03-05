import pytest
from board_manager import BoardManager
from pieces import *

def test_is_board_size_correct():    
    board = BoardManager()
    assert board.board_length == 8
    assert board.board_width == 8

    board = BoardManager(10, 10)
    assert board.board_length == 10
    assert board.board_width == 10

def test_is_piece_added_in_position():
    board = BoardManager()

    pawn = Pawn(True)
    board.add_piece(pawn, 0, 0)
    assert board.board[0][0] == pawn

    knight = Knight(True)
    board.add_piece(knight, 1, 2)
    assert board.board[1][2] == knight

    bishop = Bishop(True)
    board.add_piece(bishop, 2, 3)
    assert board.board[2][3] == bishop

    rook = Rook(True)
    board.add_piece(rook, 3, 4)
    assert board.board[3][4] == rook

    queen = Queen(True)
    board.add_piece(queen, 4, 5)
    assert board.board[4][5] == queen

def test_are_pawn_movements_correct():
    board = BoardManager()

    pawn = Pawn(True)
    board.add_piece(pawn, 6, 6)
    assert set(pawn.get_possible_moves()) == {(5, 6), (4, 6)}
    assert set(pawn.get_possible_attacks()) == {(5, 5), (5, 7)}

    pawn = Pawn(False)
    board.add_piece(pawn, 1, 1)
    assert set(pawn.get_possible_moves()) == {(2, 1), (3, 1)}
    assert set(pawn.get_possible_attacks()) == {(2, 0), (2, 2)}

def test_are_knight_movements_correct():
    board = BoardManager()

    knight = Knight(True)
    board.add_piece(knight, 6, 6)
    assert set(knight.get_possible_moves()) == {(4, 5), (4, 7), (5, 4), (5, 8), (7, 4), (7, 8), (8, 5), (8, 7)}
    assert set(knight.get_possible_attacks()) == {(4, 5), (4, 7), (5, 4), (5, 8), (7, 4), (7, 8), (8, 5), (8, 7)}

    knight = Knight(False)
    board.add_piece(knight, 1, 1)
    assert set(knight.get_possible_moves()) == {(3, 0), (3, 2), (0, 3), (0, -1), (2, 3), (2, -1), (-1, 0), (-1, 2)}
    assert set(knight.get_possible_attacks()) == {(3, 0), (3, 2), (0, 3), (0, -1), (2, 3), (2, -1), (-1, 0), (-1, 2)}
