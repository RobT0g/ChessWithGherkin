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
        self.generate_board()
        self.display_board()

    def draw_pieces(self):
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece:
                    piece.load_icon()
                    icon = piece.get_icon()
                    self.display.blit(icon, (j*self.tile_size + self.border_size + (j+1)*2, i*self.tile_size + self.border_size + (i+1)*2))

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
                board_manager.display_board()

