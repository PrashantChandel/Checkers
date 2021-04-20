import pygame
import pygame_menu
from checkers.constants import  SQUARE_SIZE, WIDTH, HEIGHT
from checkers.board import Board
from checkers.game import Game
from main import Main
from checkers.data_handling import get_name, set_name

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def set_mode(value, difficulty):
    # upcoming feature
    pass
GAME = Main(WIN)

def start_the_game():
	GAME.START_GAME()

menu = pygame_menu.Menu(HEIGHT, WIDTH, 'CHECKERS', theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default = get_name(), onchange = set_name)
menu.add.button('Play', start_the_game)
menu.add.selector('Mode:', [('1 Vs 1', 1), ('ONLINE', 2)], onchange=set_mode)
menu.add.button('SAVE')

menu.mainloop(WIN)