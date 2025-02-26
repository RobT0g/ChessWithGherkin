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
        self.board[0][0] = Rook(False, 8)
        self.board[0][7] = Rook(False, 8)
        self.board[7][0] = Rook(True, 8)
        self.board[7][7] = Rook(True, 8)
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

        if not self.board[row][col]:
            return
        
        piece = self.board[row][col]
        print(f"Moves: {moves}")
        print(f"Attacks: {attacks}")

        self.highlight_possible_moves(moves, attacks, piece.name == "Pawn")

    def highlight_possible_jump_moves(self, piece:Piece):
        moves = piece.get_possible_moves()
        attacks = piece.get_possible_attacks()
        for move in moves:
            if self.board[move[0]][move[1]]:
                continue
            
            pygame.draw.rect(self.display, (0, 255, 0), (move[1]*self.tile_size + self.border_size + (move[1]+1)*2, move[0]*self.tile_size + self.border_size + (move[0]+1)*2, self.tile_size, self.tile_size))

        for attack in attacks:
            if not self.board[attack[0]][attack[1]]:
                continue
            
            pygame.draw.rect(self.display, (255, 0, 0), (attack[1]*self.tile_size + self.border_size + (attack[1]+1)*2, attack[0]*self.tile_size + self.border_size + (attack[0]+1)*2, self.tile_size, self.tile_size))
        
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
                    pygame.draw.rect(self.display, (255, 0, 0), (y*self.tile_size + self.border_size + (y+1)*2, x*self.tile_size + self.border_size + (x+1)*2, self.tile_size, self.tile_size))
                    break
                
                pygame.draw.rect(self.display, (0, 255, 0), (y*self.tile_size + self.border_size + (y+1)*2, x*self.tile_size + self.border_size + (x+1)*2, self.tile_size, self.tile_size))
                x += move[0]
                y += move[1]

    
    def display_board(self):
        self.display.blit(self.board_surface, (self.border_size, self.border_size))
        pygame.draw.rect(self.display, (139, 69, 19), (0, 0, self.screen_size, self.screen_size), self.border_size)
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

