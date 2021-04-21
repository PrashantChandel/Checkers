from .piece import Piece
import pygame
import json
from .constants import BLACK, ROWS, COLS, BLUE, SQUARE_SIZE, WHITE
from checkers.data_handling import get_board, set_board
from checkers.sounds import Sounds

sound = Sounds()

class Board:
    def __init__(self, voice = True):
        self.board = []
        self.blue_left = self.black_left = 12
        self.blue_kings = self.black_kings = 0
        self.retreive_board()
        self.voice = voice
     
    def draw_squares(self, win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, BLACK, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def get_piece(self, row, col):
        return self.board[row][col]

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        sound.make_jump_sound(self.voice)
        if row == ROWS - 1 or row == 0:
            piece.make_king()
            sound.make_king_sound(self.voice)
            if piece.color ==  BLACK:
                self.black_kings += 1
            else:
                self.blue_kings += 1

    def retreive_board(self):
        self.board = get_board()
        cntblue = cntblack = 0
        blueking = blackking = 0
        for row in self.board:
            for cell in row:
                if cell == 0:
                    pass
                elif cell.color == BLUE:
                    cntblue += 1
                    if cell.king:
                        blueking += 1
                elif cell.color == BLACK:
                    cntblack += 1
                    if cell.king:
                        blackking += 1
        self.black_left = cntblack
        self.blue_left = cntblue
        self.black_kings = blackking
        self.blue_kings = blueking
    
    #currently no need of this below function but still may be
    # helful if raw_board gets deleted from data.json
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, BLACK))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLUE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0) 
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
    
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == BLUE:
                    self.blue_left -= 1
                elif piece.color == BLACK:
                    self.black_left -= 1
    
    def winner(self):
        if self.blue_left <= 0:
            return BLACK
        elif self.black_left <= 0:
            return BLUE
        return None

    
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        if piece.color == BLUE or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == BLACK or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))
        return moves        

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        if piece.color == BLUE or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == BLACK or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))
        print(len(moves))
        return moves        
    
    def _traverse_left(self, start, stop, step, color, left, skipped = []):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                row = 0
                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped = last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped = last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped = []):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last
                row = 0
                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped = last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped = last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            right += 1
        return moves