import pygame
import pygame_menu
from checkers.constants import  SQUARE_SIZE, WIDTH, HEIGHT
from checkers.board import Board
from checkers.game import Game
from main import Main
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def set_mode(value, difficulty):
    # upcoming feature
    pass

def start_the_game():
	GAME = Main(WIN)
	GAME.START_GAME()
    
def do_nothing():
	pass


menu = pygame_menu.Menu(WIDTH, HEIGHT, 'CHECKERS', theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='Ding_Dong_Dino')
menu.add.button('Play', start_the_game)
menu.add.selector('Mode:', [('1 Vs 1', 1), ('ONLINE', 2)], onchange=set_mode)
menu.add.button('QUIT', do_nothing)

menu.mainloop(WIN)