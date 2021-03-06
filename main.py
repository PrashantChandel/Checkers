from os import terminal_size
import pygame  
import time 
from checkers.constants import *
from checkers.board import Board
from checkers.game import Game

COLOR_SIDE_MENU = (220,220,220)
FIRST_ROW = 700
SECOND_ROW = 500
THIRD_ROW = 300
TOP_FIRST_ROW = 50
TOP_SECOND_ROW = 150

class TEXT:
    def __init__(self, show_me, color = BLACK, bg = None):
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf', 25)
        self.text = font.render(show_me, True, color, bg)
        self.textshow = self.text.get_rect()
        self.textshow.center = (WIDTH//2 - SQUARE_SIZE, HEIGHT//2 - SQUARE_SIZE)
    def show_text(self, WIN):
        WIN.blit(self.text,self.textshow)  
    def show_text_manual(self,WIN, x, y):
        pos = x,y    
        WIN.blit(self.text, pos)

class Main:
    def __init__(self, WIN):
        self.ON = True
        self.WIN = WIN
        self.FPS = 60
        self.pause_text = TEXT('GAME IS PAUSED! PRESS SPACE TO RESUME')
    
    def Score(self, game):
        # white left: w
        # blue left : b
        b = game.board.blue_left
        w = game.board.black_left
        self.WIN.fill(COLOR_SIDE_MENU, ((800,0), (1000,800)))
        b_l = TEXT('BLUE LEFT : ' + str(b), ORANGE)
        w_l = TEXT('WHITE LEFT: ' + str(w), ORANGE)
        b_l.show_text_manual(self.WIN,805, TOP_SECOND_ROW)
        w_l.show_text_manual(self.WIN,805, TOP_FIRST_ROW)
        if(game.board.winner() == "blue"):
            winner = TEXT('BLUE WON !!', ORANGE)
            winner.show_text_manual(self.WIN, 810, THIRD_ROW)
        elif(game.board.winner() == "black"):
            winner = TEXT('WHITE WON !!', ORANGE)
            winner.show_text_manual(self.WIN, 810, THIRD_ROW)


    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    def Pause(self):
        pause = 1
        self.pause_text.show_text(self.WIN)
        while pause > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pause = -1
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = 0
            pygame.display.update()
        return pause      
    def declare(self, winner):
        pause = -1
        if winner=="blue":
            self.WIN.blit(WINNER,(HEIGHT//4,WIDTH//2+WIDTH//16))
            pause = 1
        elif winner=="black":
            self.WIN.blit(WINNER,(HEIGHT//4,WIDTH//16))
            pause = 1
        else:
            return 0
        while pause > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pause = -1
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = -1
            pygame.display.update()
        return 1

    def START_GAME(self, voice = True):
        if(self.ON == False):
            self.ON = True
            return False
        run = True
        clock = pygame.time.Clock()
        game = Game(self.WIN, voice)
        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        status = self.Pause()
                        if(status == -1):
                            run = False
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_row_col_from_mouse(pos)
                    if(row<8 and col<8):
                        game.select(row, col)
                    else:
                        pass          
            game.update()
            self.Score(game)
            check = self.declare(game.board.winner())
            if check == 1:
                run = False
                break
        self.ON = True
        return False
