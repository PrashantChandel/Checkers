import pygame
from checkers.constants import WIDTH, HEIGHT
from main import Main
from menu import Menu

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

def do():
    clock = pygame.time.Clock()
    MENU = Menu(WIN)
    MAIN = Main(WIN)
    while True:
        clock.tick(FPS)
        voice = MENU.START()
        MAIN.START_GAME(voice)
        pygame.display.update()



do()
    

        