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

        self.visited = {}
        self.moves = [[[1, 1], [1, -1], [-1, 1], [-1, -1]], [[1, -1], [1, 1]], [[-1, 1], [-1, -1]]]   
    def draw_squares(self, win):
        win.fill(WHITE, ((0,0),(800,800)))
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
        for p in pieces:
            piece=self.get_piece(p[0], p[1])
            if piece != 0:
                self.board[piece.row][piece.col] = 0
                if piece.color == BLUE:
                    self.blue_left -= 1
                elif piece.color == BLACK:
                    self.black_left -= 1
    
    def winner(self):
        if self.blue_left <= 0:
            return "black"
        elif self.black_left <= 0:
            return "blue"
        return None

    
    def isValid(self, x, y):
        return x >=0 and y >=0 and x < ROWS and y < COLS   

    def get_valid_moves(self, piece):
        x = piece.row
        y = piece.col
        nowPiece = self.get_piece(x, y)
        d={}

        typeOfPiece = 2
        if self.get_piece(x, y).king:
            typeOfPiece = 0
        elif self.get_piece(x, y).color == BLACK:
            typeOfPiece = 1

        # double steps
        for i in self.moves[typeOfPiece]:
            if self.isValid(x + i[0], y + i[1]) and self.get_piece(x + i[0], y + i[1]) != 0 and self.get_piece(x + i[0], y + i[1]).color != nowPiece.color:
                if self.isValid(x + 2 * i[0], y + 2 * i[1]) and self.get_piece(x + 2 * i[0], y + 2 * i[1]) == 0:
                    self.visited = {}
                    self.visited[(x, y)] = []
                    d.update(self.find_allowed_moves(
                        x + 2 * i[0], y + 2 * i[1], typeOfPiece,  self.get_piece(x, y).color, [[x + i[0], y + i[1]]]))

        # single steps
        for i in self.moves[typeOfPiece]:
            if self.isValid(x + i[0], y + i[1]) and self.get_piece(x + i[0], y + i[1]) == 0:
                d[(x+i[0], y+i[1])] = []

        print(d)

        return d

    def find_allowed_moves(self, x, y, typeOfPiece, nowPiece, skipped_pieces):
        print(x, y, skipped_pieces)
        print('visited',self.visited)
        d={}
        d[(x, y)]=[]
        #d[(x, y)]=skipped_pieces
        if (x, y) in self.visited:
            return self.visited[(x, y)]
        for i in skipped_pieces:
            d[(x, y)].append(i)
        for i in self.moves[typeOfPiece]:
            if self.isValid(x + i[0], y + i[1]) and self.get_piece(x + i[0], y + i[1]) != 0 and self.get_piece(x + i[0], y + i[1]).color != nowPiece:
                if self.isValid(x + 2 * i[0], y + 2 * i[1]) and self.get_piece(x + 2 * i[0], y + 2 * i[1]) == 0:
                    self.visited[(x, y )]=[]
                    d.update(self.find_allowed_moves(x + 2 * i[0], y + 2 * i[1], typeOfPiece, nowPiece,skipped_pieces + [[x + i[0], y + i[1]]]))
                    self.visited[(x, y)]=d
        #print(d)
        return d