import pygame
import pygame_menu
from checkers.constants import  SQUARE_SIZE, WIDTH, HEIGHT
from checkers.board import Board
from checkers.game import Game
from main import Main
from checkers.data_handling import get_raw_board, get_name, get_raw_board, set_name, get_board, set_board

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def set_mode(value, difficulty):
    # upcoming feature
    pass
GAME = Main(WIN)

def resume_previous():
    set_board(get_board())
    GAME.START_GAME()

def start_the_game():
    set_board(get_raw_board())
    GAME.START_GAME()


menu = pygame_menu.Menu(HEIGHT, WIDTH, 'CHECKERS', theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('NAME:', default = get_name(), onchange = set_name)
menu.add.button('NEW GAME', start_the_game)
menu.add.selector('Mode:', [('1 Vs 1', 1), ('ONLINE', 2)], onchange=set_mode)

menu.add.button('RESUME', resume_previous)

menu.mainloop(WIN)