import pygame
import pygame_menu
from checkers.constants import  SQUARE_SIZE, WIDTH, HEIGHT
from checkers.board import Board
from checkers.game import Game
from main import Main
from checkers.data_handling import get_raw_board, get_name, get_raw_board, set_name, get_board, set_board
from checkers.sounds import Sounds



class MENU:
    def __init__(self):
        pygame.init()
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.VOICE = True
        self.sound = Sounds()
        self.MAIN = Main(self.WIN)
        self.VOICE = False
        self.menu = pygame_menu.Menu(HEIGHT, WIDTH, 'CHECKERS', theme = pygame_menu.themes.THEME_DARK)
        self.menu.add.text_input('NAME:', default = get_name(), onchange = set_name)
        self.menu.add.button('NEW GAME', self.start_the_game)
        self.menu.add.button('RESUME', self.resume_previous)
        self.menu.add.selector('Sound:', [('ON', True), ('OFF', False)], onchange = self.config_sound)
        self.menu.add.selector('Music:', [('OFF', False), ('ON', True)], onchange = self.config_music)

    def config_sound(self, obj, value):
        self.VOICE = value

        

    def resume_previous(self):
        set_board(get_board())
        self.MAIN.START_GAME(self.VOICE)

    def start_the_game(self):
        set_board(get_raw_board())
        self.MAIN.START_GAME(self.VOICE)

    def config_music(self, obj, value):
        if value:
            self.sound.play_music()
        else:
            self.sound.stop_music()

    def START(self):
        self.menu.mainloop(self.WIN)


MENU().START()