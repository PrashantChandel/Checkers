import pygame

WIDTH, HEIGHT = 800, 800
HEIGHT_BOARD = 800
WIDTH_BOARD = WIDTH 
HEIGHT_BELOW_MENU = 0
ROWS, COLS = 8, 8
SQUARE_SIZE = HEIGHT_BOARD // ROWS
PADDING = 15

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 195, 255)
DARK_BLUE = (179, 0, 255)

PIECE_BLUE = pygame.transform.scale(pygame.image.load('checkers/assets/blue_piece.png'), (SQUARE_SIZE - PADDING, SQUARE_SIZE - PADDING))
PIECE_BLACK = pygame.transform.scale(pygame.image.load('checkers/assets/black_piece.png'), (SQUARE_SIZE - PADDING, SQUARE_SIZE - PADDING))
CROWN = pygame.transform.scale(pygame.image.load('checkers/assets/crown.png'), (SQUARE_SIZE // 2 + PADDING, SQUARE_SIZE // 2 + PADDING))