import pygame
import pygame_menu
from checkers.constants import  SQUARE_SIZE, WIDTH, HEIGHT
from checkers.board import Board
from checkers.game import Game
from main import Main
from checkers.data_handling import get_raw_board, get_name, get_raw_board, get_raw_turn, get_turn, set_name, get_board, set_board, set_turn
from checkers.sounds import Sounds



class Menu:
    def __init__(self, WIN):
        pygame.init()
        self.WIN = WIN
        self.VOICE = True
        self.sound = Sounds()
        self.MAIN = Main(self.WIN)
        self.VOICE = True
        self.ON = True
        self.menu = pygame_menu.Menu(HEIGHT, WIDTH, 'CHECKERS', theme = pygame_menu.themes.THEME_DARK)
        self.menu.add.text_input('NAME:', default = get_name(), onchange = set_name)
        self.menu.add.button('NEW GAME', self.start_the_game)
        self.menu.add.button('RESUME', self.resume_previous)
        self.menu.add.selector('Sound:', [('ON', True), ('OFF', False)], onchange = self.config_sound)
        self.menu.add.selector('Music:', [('OFF', False), ('ON', True)], onchange = self.config_music)
        self.menu.add.button('EXIT', self.close)
    def config_sound(self, obj, value):
        self.VOICE = value

    def close(self):
        self.menu.disable()

    def resume_previous(self):
        set_board(get_board())
        set_turn(get_turn())
        self.ON = False

    def start_the_game(self):
        set_board(get_raw_board())
        set_turn(get_raw_turn())
        self.ON = False

    def config_music(self, obj, value):
        if value:
            self.sound.play_music()
        else:
            self.sound.stop_music()

    def START(self):
        while True:
            if(self.ON == False):
                self.ON = True
                return self.VOICE
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
            if self.menu.is_enabled():
                self.menu.update(events)
                self.menu.draw(self.WIN)
            pygame.display.update()
