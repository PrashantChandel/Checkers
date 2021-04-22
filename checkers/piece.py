import pygame
from .constants import BLACK, SQUARE_SIZE, PIECE_BLACK, PIECE_BLUE, PADDING, CROWN, BLUE

class Piece:
	def __init__(self, row, col, color, king = False):
		self.row = row
		self.col = col
		self.color = color
		self.king = king
		if self.color == BLUE:
			self.direction = -1
		else:
			self.direction = 1
		self.x = 0
		self.y = 0
		self.calc_pos()
 
	def calc_pos(self):
		self.x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
		self.y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2
	def make_king(self):
		self.king = True

	def draw(self, win):
		if self.color == BLUE:
			win.blit(PIECE_BLUE, (self.x - PIECE_BLUE.get_width()//2, self.y - PIECE_BLUE.get_height()//2))
		else:
			win.blit(PIECE_BLACK, (self.x - PIECE_BLACK.get_width()//2, self.y - PIECE_BLACK.get_height()//2))
		if self.king == True:
			win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

	def move(self, row, col):
		self.row = row
		self.col = col
		self.calc_pos()