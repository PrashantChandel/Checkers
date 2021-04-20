import pygame   
from checkers.constants import  SQUARE_SIZE, WIDTH, HEIGHT,BLACK,WHITE
from checkers.board import Board
from checkers.game import Game

class Main:
    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf',25)
    text = font.render('GAME IS PAUSED! PRESS SPACE TO RESUME',True,BLACK,WHITE)
    textshow = text.get_rect()
    textshow.center=(WIDTH//2,HEIGHT//2)

    def __init__(self, WIN):
        self.WIN = WIN
        self.FPS = 60

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    def Pause(self):
        pause = 1
        self.WIN.blit(self.text,self.textshow)
        while pause > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pause = -1
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = 0
            pygame.display.update()
        return pause  

    def START_GAME(self):
        run = True
        clock = pygame.time.Clock()
        game = Game(self.WIN)
        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        status = self.Pause()
                        if(status == -1):
                            run = False
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_row_col_from_mouse(pos)
                    game.select(row, col)
            game.update()
            
        pygame.quit()