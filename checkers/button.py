import pygame
from checkers.constants import SQUARE_SIZE, WIDTH, HEIGHT
NORMAL_SIZE = (SQUARE_SIZE, SQUARE_SIZE)
MIDDLE_POS = (WIDTH // 2 - SQUARE_SIZE, HEIGHT // 2 - SQUARE_SIZE)

class Button:
    def __init__(self, type, WIN, pos = MIDDLE_POS, size = NORMAL_SIZE):
        self.ON = False
        self.loc = "checkers/assets/" + type + ".png"
        self.button = pygame.transform.scale(pygame.image.load(self.loc), size)
        self.x, self.y = pos
        self.height, self.width = size
        self.WIN = WIN

    def toggle(self):
        self.ON = not self.ON
    
    def isON(self):
        return self.ON
    
    def ON(self):
        self.ON = True
    
    def OFF(self):
        self.ON = False
    
    def isClick(self, x, y):
        if x >= self.x and x <= self.x + SQUARE_SIZE and y >= self.y and y <= self.y + SQUARE_SIZE:
            return True
        return False
    
    def show(self):
        self.WIN.blit(self.button, (self.x, self.y))
    