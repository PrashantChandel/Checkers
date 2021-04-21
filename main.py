import pygame   
from checkers.constants import  SQUARE_SIZE, WIDTH, HEIGHT
from checkers.board import Board
from checkers.game import Game





class Main:
    def __init__(self, WIN):
        self.WIN = WIN
        self.FPS = 60

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    def START_GAME(self):
        run = True
        clock = pygame.time.Clock()
        game = Game(self.WIN)
        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_row_col_from_mouse(pos)
                    game.select(row, col)
            game.update()
        

        # saving the current state
        state_to_save = game.board
        state_to_save.store_database()

        pygame.quit()