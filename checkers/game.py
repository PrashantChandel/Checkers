import pygame
from .constants import BLUE, WHITE, BLACK, SQUARE_SIZE, DARK_BLUE
from checkers.board import Board
from checkers.data_handling import get_board, set_board, get_raw_board
radius_allowed_moves = 15

class Game:
    def __init__(self, win, voice = True):
        self.selected = None
        self.board = Board(voice)
        self.turn = BLUE
        self.allowed_moves = {}
        self.win = win
        self.voice = voice
 
    # everytime to change anything on baord we update it

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.allowed_moves)
        set_board(self.board.board)
        pygame.display.update()


    # reset the game

    def reset(self):
        self.selected = None
        self.board = Board()
        self.turn = BLUE
        self.allowed_moves = {}

    def turn_change(self):
        self.allowed_moves = {}
        if self.turn == BLUE:
            self.turn = BLACK
        else:
            self.turn = BLUE


    # recursive function to handle the move selected by player
    def select(self, row, col):
        if self.selected:  # if selected is true
            result = self.move(row, col)  # try to move

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.allowed_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def move(self, row, col):
        position = self.board.get_piece(row, col)  # check if it is piece or not
        if self.selected and position == 0 and (
        row, col) in self.allowed_moves:  # the coordinates should be in allowed moves
            self.board.move(self.selected, row, col)  # move selected piece to coordinate
            skipped = self.allowed_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.turn_change()  # player succesfuly moved so change turn

        else:
            return False  # unsuccedful

        return True  # move possible and  accomplished

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, DARK_BLUE,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                               radius_allowed_moves)  # draw the circle showing possible moves for a piece