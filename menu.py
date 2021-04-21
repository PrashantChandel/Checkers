import pygame
import pygame_menu
from checkers.constants import  SQUARE_SIZE, WIDTH, HEIGHT
from checkers.board import Board
from checkers.game import Game
from main import Main
from checkers.data_handling import get_raw_board, get_name, get_raw_board, set_name, get_board, set_board
from checkers.sounds import Sounds

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
VOICE = True

sound = Sounds()

def config_sound(obj, value):
    global VOICE
    VOICE = value
    print(VOICE)

MAIN = Main(WIN)

def resume_previous():
    set_board(get_board())
    MAIN.START_GAME(VOICE)

def start_the_game():
    set_board(get_raw_board())
    MAIN.START_GAME(VOICE)

def config_music(obj, value):
    if value:
        sound.play_music()
    else:
        sound.stop_music()

menu = pygame_menu.Menu(HEIGHT, WIDTH, 'CHECKERS', theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('NAME:', default = get_name(), onchange = set_name)
menu.add.button('NEW GAME', start_the_game)
menu.add.button('RESUME', resume_previous)
menu.add.selector('Sound:', [('ON', True), ('OFF', False)], onchange = config_sound)
menu.add.selector('Music:', [('OFF', False), ('ON', True)], onchange = config_music)


menu.mainloop(WIN)