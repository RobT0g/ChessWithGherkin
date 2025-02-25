import pygame
from pygame.locals import *
from pieces import *

pygame.init()  

class BoardManager:
    def __init__(self):
        self.board = [[0 for i in range(8)] for j in range(8)]

    def set_initial_arrengement(self):
        self.board[0] = [1, 2, 3, 4, 5, 3, 2, 1]
        self.board[1] = [6, 6, 6, 6, 6, 6, 6, 6]
        self.board[6] = [-6, -6, -6, -6, -6, -6, -6, -6]
        self.board[7] = [-1, -2, -3, -4, -5, -3, -2, -1]