import pygame
from pygame.locals import *

class Piece:
    def __init__(self, player: bool, name:str):
        self.player = not player
        self.name = name
        self.x = None
        self.y = None
        self.icon = None

    def set_piece_position(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_piece_position(self) -> tuple[int]:
        return self.x, self.y
    
    def get_possible_moves(self) -> tuple[int]:
        pass

    def get_possible_attacks(self) -> tuple[int]:
        pass

    def get_player(self) -> bool:
        return self.player
    
    def get_icon_name(self) -> str:
        return f"{self.name}_{'W' if not self.player else 'B'}"
    
    def load_icon(self):
        self.icon = pygame.image.load(f'icons/{self.get_icon_name()}.png')
        
    def get_icon(self) -> pygame.Surface:
        return self.icon
    
    def get_movement_type(self) -> str:
        pass


class Pawn(Piece):
    def __init__(self, player: bool):
        super().__init__(player, "Pawn")
        self.has_moved = False

    def get_possible_moves(self):
        moves = [1, 2] if not self.has_moved else [1]
        return [(self.x + (v if self.player else -v), self.y) for v in moves]

    def get_possible_attacks(self):
        return [(self.x + (1 if self.player else -1), self.y + 1), (self.x + (1 if self.player else -1), self.y - 1)]
    
    def set_piece_position(self, x, y):
        super().set_piece_position(x, y)
        self.has_moved = True

    def get_movement_type(self):
        return 'jump'


class Knight(Piece):
    def __init__(self, player: bool):
        super().__init__(player, "Knight")

    def get_possible_moves(self):
        moves = [(_x, _y) for _x in (-2, -1, 1, 2) for _y in (-2, -1, 1, 2) if abs(_x) != abs(_y)]
        return [(self.x + _x, self.y + _y) for _x, _y in moves]
    
    def get_possible_attacks(self):
        return self.get_possible_moves()

    def get_movement_type(self):
        return 'jump'
    

class Rook(Piece):
    def __init__(self, player: bool):
        super().__init__(player, "Rook")

    def get_possible_moves(self):
        return [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def get_possible_attacks(self):
        return self.get_possible_moves()

    def get_movement_type(self):
        return 'stream'


class Queen(Piece):
    def __init__(self, player: bool):
        super().__init__(player, "Queen")

    def get_possible_moves(self):
        return [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    def get_possible_attacks(self):
        return self.get_possible_moves()

    def get_movement_type(self):
        return 'stream'
    

class King(Piece):
    def __init__(self, player: bool):
        super().__init__(player, "King")

    def get_possible_moves(self):
        moves = [(_x, _y) for _x in range(-1, 2) for _y in range(-1, 2) if _x != 0 or _y != 0]
        return [(self.x + _x, self.y + _y) for _x, _y in moves if 0 <= self.x + _x < 8 and 0 <= self.y + _y < 8]
    
    def get_possible_attacks(self):
        return self.get_possible_moves()

    def get_movement_type(self):
        return 'jump'


class Bishop(Piece):
    def __init__(self, player: bool):
        super().__init__(player, "Bishop")

    def get_possible_moves(self):
        return [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    def get_possible_attacks(self):
        return self.get_possible_moves()

    def get_movement_type(self):
        return 'stream'
