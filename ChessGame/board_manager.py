import pygame
from pygame.locals import *
from pieces import *

pygame.init()  

class BoardManager:
    def __init__(self):
        self.board = [[0 for i in range(8)] for j in range(8)]
        self.tile_size = 75
        self.screen_size = self.tile_size*8 + 60 + 9*2
        self.display = pygame.display.set_mode((self.screen_size, self.screen_size))
        pygame.display.set_caption('Chess Game')

    def set_initial_arrengement(self):
        self.board[0] = [1, 2, 3, 4, 5, 3, 2, 1]
        self.board[1] = [6, 6, 6, 6, 6, 6, 6, 6]
        self.board[6] = [-6, -6, -6, -6, -6, -6, -6, -6]
        self.board[7] = [-1, -2, -3, -4, -5, -3, -2, -1]





if __name__ == '__main__':
    board_manager = BoardManager()
    board_manager.set_initial_arrengement()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        pygame.time.Clock().tick(60)

