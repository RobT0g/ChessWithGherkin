class Piece:
    def __init__(self, player: bool, name:str):
        self.player = player
        self.name = name
        self.x = None
        self.y = None

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
    
    def get_name(self) -> str:
        return self.name + f'_{"B" if self.player else "W"}'
    

class Pawn(Piece):
    def __init__(self, player: bool, has_moved: bool=False):
        super().__init__(player, "Pawn")
        self.has_moved = has_moved

    def get_possible_moves(self):
        moves = [1, 2] if not self.has_moved else [1]
        return [(self.x + (1 if self.player else -1), self.y) for _ in moves]

    def get_possible_attacks(self):
        return [(self.x + (1 if self.player else -1), self.y + 1), (self.x + (1 if self.player else -1), self.y - 1)]


class Knight(Piece):
    def __init__(self, player: bool):
        super().__init__(player, "Knight")

    def get_possible_moves(self):
        moves = [(_x, _y) for _x in (-2, -1, 1, 2) for _y in (-2, -1, 1, 2) if abs(_x) != abs(_y)]
        return [(self.x + _x, self.y + _y) for _x, _y in moves]
    
    def get_possible_attacks(self):
        return self.get_possible_moves()
    

class Rook(Piece):
    def __init__(self, player: bool, board_length: int):
        super().__init__(player, "Rook")
        self.board_length = board_length

    def get_possible_moves(self):
        moves = [(_x, _y) for _x in range(-self.board_length, self.board_length + 1) for _y in range(-self.board_length, self.board_length + 1) if _x == 0 or _y == 0]
        return [(self.x + _x, self.y + _y) for _x, _y in moves if 0 <= self.x + _x < self.board_length and 0 <= self.y + _y < self.board_length]


    