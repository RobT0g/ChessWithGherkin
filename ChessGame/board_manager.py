import pygame
from pygame.locals import *
from pieces import *

pygame.init()  

class BoardManager:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]
        self.tile_size = 75
        self.border_size = 15
        self.screen_size = self.tile_size*8 + self.border_size*2 + 9*2
        self.display = pygame.display.set_mode((self.screen_size, self.screen_size))
        pygame.display.set_caption('Chess Game')
        self.generate_board()
        self.player_turn = False

        self.highlighted_piece = None
        self.highlighted_moves = []
        self.highlighted_attacks = []

    def generate_board(self):
        self.board_surface = pygame.Surface((self.tile_size*8+9*2, self.tile_size*8+9*2))
        for i in range(8):
            for j in range(8):
                color = (222, 184, 135) if (i+j)%2 == 0 else (139, 69, 19)
                pygame.draw.rect(self.board_surface, color, (i*self.tile_size + (i+1)*2, j*self.tile_size + (j+1)*2, self.tile_size, self.tile_size))

    def set_initial_arrengement(self):
        for i in range(8):
            self.board[1][i] = Pawn(False)
            self.board[6][i] = Pawn(True)
        self.board[0][0] = Rook(False)
        self.board[0][7] = Rook(False)
        self.board[7][0] = Rook(True)
        self.board[7][7] = Rook(True)
        self.board[0][1] = Knight(False)
        self.board[0][6] = Knight(False)
        self.board[7][1] = Knight(True)
        self.board[7][6] = Knight(True)
        self.board[0][2] = Bishop(False)
        self.board[0][5] = Bishop(False)
        self.board[7][2] = Bishop(True)
        self.board[7][5] = Bishop(True)
        self.board[0][3] = Queen(False)
        self.board[7][3] = Queen(True)
        self.board[0][4] = King(False)
        self.board[7][4] = King(True)

        for i in range(8):
            for j in range(8):
                if self.board[i][j]:
                    self.board[i][j].set_piece_position(i, j)

    def draw_pieces(self):
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece:
                    piece.load_icon()
                    icon = piece.get_icon()
                    self.display.blit(icon, (j*self.tile_size + self.border_size + (j+1)*2, i*self.tile_size + self.border_size + (i+1)*2))

    def on_click(self):
        x, y = pygame.mouse.get_pos()
        col = (x - self.border_size) // (self.tile_size + 2)
        row = (y - self.border_size) // (self.tile_size + 2)
        print(f"Clicked on row: {row}, col: {col}")

        if row < 0 or row >= 8 or col < 0 or col >= 8:
            return

        if (row, col) in self.highlighted_moves or (row, col) in self.highlighted_attacks:
            self.move_piece(self.highlighted_piece, row, col)
            self.highlighted_piece = None
            self.highlighted_moves = []
            self.highlighted_attacks = []
            self.player_turn = not self.player_turn
            return

        if not self.board[row][col]:
            return
        
        if self.board[row][col].player != self.player_turn:
            return
        
        self.highlighted_piece = self.board[row][col]
        self.highlighted_moves = []
        self.highlighted_attacks = []

        moves = self.highlighted_piece.get_possible_moves()
        attacks = self.highlighted_piece.get_possible_attacks()
        print(f"Possible moves: {moves}")
        print(f"Possible attacks: {attacks}")

        if self.highlighted_piece.get_movement_type() == 'jump':
            self.highlight_possible_jump_moves(self.highlighted_piece)

        else:
            self.highlight_possible_stream_moves(self.highlighted_piece)

    def move_piece(self, piece:Piece, row:int, col:int):
        self.board[piece.x][piece.y] = None
        self.board[row][col] = piece
        piece.set_piece_position(row, col)

    def highlight_possible_jump_moves(self, piece:Piece):
        moves = piece.get_possible_moves()
        attacks = piece.get_possible_attacks()
        for move in moves:
            if self.board[move[0]][move[1]]:
                continue
            
            self.highlighted_moves.append(move)
            
        for attack in attacks:
            if not self.board[attack[0]][attack[1]]:
                continue
            
            if self.board[attack[0]][attack[1]].player == piece.player:
                continue

            self.highlighted_attacks.append(attack)
        
    def highlight_possible_stream_moves(self, piece:Piece):
        moves = piece.get_possible_moves()
        attacks = piece.get_possible_attacks()

        for move in moves:
            x, y = piece.get_piece_position()
            x += move[0]
            y += move[1]

            while 0 <= x < 8 and 0 <= y < 8:
                if self.board[x][y] and self.board[x][y].player == piece.player:
                    break

                if self.board[x][y]:
                    self.highlighted_attacks.append((x, y))
                    break
                
                self.highlighted_moves.append((x, y))
                x += move[0]
                y += move[1]
    
    def display_board(self):
        self.display.blit(self.board_surface, (self.border_size, self.border_size))
        pygame.draw.rect(self.display, (139, 69, 19), (0, 0, self.screen_size, self.screen_size), self.border_size)

        for move in self.highlighted_moves:
            pygame.draw.rect(self.display, (0, 255, 0, 100), (move[1]*self.tile_size + self.border_size + (move[1]+1)*2, move[0]*self.tile_size + self.border_size + (move[0]+1)*2, self.tile_size, self.tile_size))

        for attack in self.highlighted_attacks:
            pygame.draw.rect(self.display, (255, 0, 0, 100), (attack[1]*self.tile_size + self.border_size + (attack[1]+1)*2, attack[0]*self.tile_size + self.border_size + (attack[0]+1)*2, self.tile_size, self.tile_size))

        self.draw_pieces()
        pygame.display.flip()


if __name__ == '__main__':
    board_manager = BoardManager()
    board_manager.set_initial_arrengement()
    board_manager.display_board()

    print(board_manager.board)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                running = False

            elif event.type == MOUSEBUTTONDOWN:
                board_manager.on_click()
                board_manager.display_board()

