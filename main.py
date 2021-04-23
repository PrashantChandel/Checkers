from os import terminal_size
import pygame   
from checkers.constants import  SQUARE_SIZE, WIDTH, HEIGHT,BLACK,WHITE,WINNER,BLUE
from checkers.board import Board
from checkers.game import Game



class TEXT:
    def __init__(self, show_me):
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf', 25)
        self.text = font.render(show_me, True, BLACK, WHITE)
        self.text_manual = font.render(show_me, True, BLACK)
        self.textshow = self.text.get_rect()
        self.textshow.center = (WIDTH//2, HEIGHT//2 - SQUARE_SIZE)
    def show_text(self, WIN):
        WIN.blit(self.text,self.textshow)  
    def show_text_manual(self,WIN, x, y):
        pos = x,y    
        WIN.blit(self.text_manual, pos)

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
        self.WIN.fill((254, 191, 195), ((800,500), (1000,800)))
        b_l = TEXT('Blue left '+str(b))
        w_l = TEXT('White left '+str(w))
        b_l.show_text_manual(self.WIN,800, 500)
        w_l.show_text_manual(self.WIN,800, 700)

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
    def declare(self,winner):
        if winner=="blue":
            self.WIN.blit(WINNER,(HEIGHT//4,WIDTH//2+100))
        elif winner=="black":
            self.WIN.blit(WINNER,(HEIGHT+HEIGHT//2,WIDTH//2+100))
        if winner!=None:
            crash=1
            while crash>0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        crash =0
                pygame.display.update()
            return 0
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
            check=self.declare(game.board.winner())
            if check==0:
                run=False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        run = False
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
        # pygame.quit()
        self.ON = True
        return False
