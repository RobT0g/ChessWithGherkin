import pygame
from pygame.locals import *
from pieces import *
import re

pygame.init()  

class BoardManager:
    def __init__(self, board_length=8, board_width=8):
        self.board_length = board_length
        self.board_width = board_width
        self.board = [[None for i in range(board_length)] for j in range(board_width)]

        self.tile_size = 75
        self.border_size = 15
        self.screen_size = [self.tile_size*size + self.border_size*2 + (size+1)*2 for size in [self.board_length, self.board_width]]
        self.display = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('Chess Game')
        
        self.generate_board()
        self.player_turn = True
        self.play_state = 'Playing'
        self.promotion_options = []

        self.highlighted_piece = None
        self.highlighted_moves = []
        self.highlighted_attacks = []

    def generate_board(self):
        self.board_surface = pygame.Surface([size-2*self.border_size for size in self.screen_size])
        for i in range(self.board_length):
            for j in range(self.board_width):
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
                    self.board[i][j].x = i
                    self.board[i][j].y = j

    def draw_pieces(self):
        for i in range(self.board_length):
            for j in range(self.board_width):
                piece = self.board[i][j]
                if piece:
                    piece.load_icon()
                    icon = piece.get_icon()
                    self.display.blit(icon, (j*self.tile_size + self.border_size + (j+1)*2, i*self.tile_size + self.border_size + (i+1)*2))

    def convert_board_coords_to_list_coords(self, x:int, y:int):
        return ((y - self.border_size) // (self.tile_size + 2), (x - self.border_size) // (self.tile_size + 2))

    def on_click(self, mouse_pos:tuple[int], convert_coord:bool=True):
        row, col = mouse_pos
        if convert_coord:
            row, col = self.convert_board_coords_to_list_coords(row, col)

        print(f"Clicked on row: {row}, col: {col}")

        if self.play_state == 'Promotion':
            print("Promoting pawn")
            self.select_pawn_promotion()
            return

        if row < 0 or row >= self.board_length or col < 0 or col >= self.board_width:
            return

        if (row, col) in self.highlighted_moves or (row, col) in self.highlighted_attacks:
            moved_piece = self.highlighted_piece
            self.move_piece(self.highlighted_piece, row, col)
            
            if self.check_game_finished():
                return
            
            if not self.check_pawn_promotion(moved_piece):
                self.player_turn = not self.player_turn
                self.highlighted_piece = None

            self.highlighted_moves = []
            self.highlighted_attacks = []
            
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
            self.define_possible_jump_moves(self.highlighted_piece)

        else:
            self.define_possible_stream_moves(self.highlighted_piece)

    def check_pawn_promotion(self, piece:Piece) -> bool:
        if not re.match(r'^Pawn', piece.get_icon_name()):
            return False
        
        if piece.player and piece.x != 0:
            return False
        
        if not piece.player and piece.x != 7:
            return False
        
        self.promotion_options = [Queen(piece.player), Rook(piece.player), Bishop(piece.player), Knight(piece.player)]
        self.play_state = 'Promotion'
        return True

    def check_game_finished(self) -> bool:
        return False

    def select_pawn_promotion(self):
        # Range on x: mid-175 to mid, mid to mid+175
        # Range on y: mid-105 to mid+20, mid+20 to mid+145
        x, y = pygame.mouse.get_pos()
        
        if x < self.screen_size[0]//2 - 175 or x > self.screen_size[0]//2 + 175:
            return
        
        if y < self.screen_size[1]//2 - 105 or y > self.screen_size[1]//2 + 145:
            return
        
        x = 0 if x < self.screen_size[0]//2 else 1
        y = 0 if y < self.screen_size[1]//2 + 20 else 1
        promoted_piece = self.promotion_options[x*2 + y]

        print(f"Promoted piece: {promoted_piece.get_icon_name()}")

        self.board[self.highlighted_piece.x][self.highlighted_piece.y] = promoted_piece
        promoted_piece.set_piece_position(self.highlighted_piece.x, self.highlighted_piece.y)
        self.play_state = 'Playing'

    def move_piece(self, piece:Piece, row:int, col:int):
        self.board[piece.x][piece.y] = None
        self.board[row][col] = piece
        piece.set_piece_position(row, col)

    def define_possible_jump_moves(self, piece:Piece):
        moves = piece.get_possible_moves()
        attacks = piece.get_possible_attacks()

        try:
            if not piece.has_moved and any([self.board[m[0]][m[1]] for m in moves]):
                moves.pop(1)
        except: pass

        for move in moves:
            if move[0] < 0 or move[0] >= self.board_length or move[1] < 0 or move[1] >= self.board_width:
                continue

            if self.board[move[0]][move[1]]:
                continue
            
            self.highlighted_moves.append(move)
            
        for attack in attacks:
            if attack[0] < 0 or attack[0] >= self.board_length or attack[1] < 0 or attack[1] >= self.board_width:
                continue

            if not self.board[attack[0]][attack[1]]:
                continue
            
            if self.board[attack[0]][attack[1]].player == piece.player:
                continue

            self.highlighted_attacks.append(attack)
        
    def define_possible_stream_moves(self, piece:Piece):
        moves = piece.get_possible_moves()
        attacks = piece.get_possible_attacks()

        for move in moves:
            x, y = piece.get_piece_position()
            x += move[0]
            y += move[1]

            while 0 <= x < self.board_length and 0 <= y < self.board_width:
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
        pygame.draw.rect(self.display, (139, 69, 19), (0, 0, *self.screen_size), self.border_size)

        if self.highlighted_piece:
            pygame.draw.rect(self.display, (255, 255, 0, 100), (self.highlighted_piece.y*self.tile_size + self.border_size + (self.highlighted_piece.y+1)*2, self.highlighted_piece.x*self.tile_size + self.border_size + (self.highlighted_piece.x+1)*2, self.tile_size, self.tile_size))

        for move in self.highlighted_moves:
            pygame.draw.rect(self.display, (0, 255, 0, 100), (move[1]*self.tile_size + self.border_size + (move[1]+1)*2, move[0]*self.tile_size + self.border_size + (move[0]+1)*2, self.tile_size, self.tile_size))

        for attack in self.highlighted_attacks:
            pygame.draw.rect(self.display, (255, 0, 0, 100), (attack[1]*self.tile_size + self.border_size + (attack[1]+1)*2, attack[0]*self.tile_size + self.border_size + (attack[0]+1)*2, self.tile_size, self.tile_size))

        self.draw_pieces()

        if self.play_state == 'Promotion':
            pygame.draw.rect(self.display, (128, 0, 128, 128), (self.screen_size[0]//2 - 200, self.screen_size[1]//2 - 125, 400, 250))
            font = pygame.font.Font(None, 24)
            text = font.render("Pick which piece to promote the pawn to:", True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.screen_size[0]//2, self.screen_size[1]//2 - 100))
            self.display.blit(text, text_rect)

            for i, piece in enumerate(self.promotion_options):
                piece.load_icon()
                icon = piece.get_icon()
                piece_pos = [self.screen_size[0]//2, self.screen_size[1]//2 - 80 + (i//2)*100]
                
                if i % 2 == 0:
                    piece_pos[0] -= 50 + icon.get_width()
                
                else:
                    piece_pos[0] += 50

                self.display.blit(icon, piece_pos)
            pass

        pygame.display.flip()


if __name__ == '__main__':
    board_manager = BoardManager()
    board_manager.set_initial_arrengement()
    board_manager.display_board()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                running = False

            elif event.type == MOUSEBUTTONDOWN:
                board_manager.on_click(pygame.mouse.get_pos())
                board_manager.display_board()

