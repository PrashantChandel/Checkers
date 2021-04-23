# from os import sched_get_priority_max
import pygame
import json
from checkers.piece import Piece
from checkers.constants import BLACK, BLUE, WHITE, DARK_BLUE
def get_name():
    with open('checkers/data.json') as DB:
        data_dict = json.loads(DB.read())
        return data_dict["Name"]
    
def set_name(name):
    data_dict = []
    with open('checkers/data.json', 'r') as DB:
        data_dict = json.loads(DB.read())
    with open('checkers/data.json', 'w') as DB:
        data_dict["Name"] = str(name)
        json.dump(data_dict, DB)

def rgb_to_color(lst):
    if lst == [0, 0, 0]:
        return BLACK
    elif lst == [255, 255, 255]:
        return WHITE
    elif lst == [0, 195, 255]:
        return BLUE
    elif lst == [179, 0, 255]:
        return DARK_BLUE

def get_raw_board():
    false = False # to make js and python compatible
    clean_board = [[0, [0, 1, [0, 0, 0], false], 0, [0, 3, [0, 0, 0], false], 0, [0, 5, [0, 0, 0], false], 0, [0, 7, [0, 0, 0], false]], [[1, 0, [0, 0, 0], false], 0, [1, 2, [0, 0, 0], false], 0, [1, 4, [0, 0, 0], false], 0, [1, 6, [0, 0, 0], false], 0], [0, [2, 1, [0, 0, 0], false], 0, [2, 3, [0, 0, 0], false], 0, [2, 5, [0, 0, 0], false], 0, [2, 7, [0, 0, 0], false]], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [[5, 0, [0, 195, 255], false], 0, [5, 2, [0, 195, 255], false], 0, [5, 4, [0, 195, 255], false], 0, [5, 6, [0, 195, 255], false], 0], [0, [6, 1, [0, 195, 255], false], 0, [6, 3, [0, 195, 255], false], 0, [6, 5, [0, 195, 255], false], 0, [6, 7, [0, 195, 255], false]], [[7, 0, [0, 195, 255], false], 0, [7, 2, [0, 195, 255], false], 0, [7, 4, [0, 195, 255], false], 0, [7, 6, [0, 195, 255], false], 0]]
    board_to_return = []
    for row in clean_board:
        new_row = []
        for cell in row:
            if(cell == 0):
                new_row.append(0)
            else:
                new_row.append(Piece(cell[0], cell[1], rgb_to_color(cell[2]), cell[3]))
        board_to_return.append(new_row)
    return board_to_return

def set_board(board_state):
    data_dict = []
    with open('checkers/data.json', 'r') as DB:
        data_dict = json.loads(DB.read())
    with open('checkers/data.json', 'w') as DB:
        board = []
        for row in board_state:
            new_row = []
            for piece in row:
                if(piece == 0):
                    new_row.append(piece)
                else:
                    new_row.append([piece.row, piece.col, piece.color, piece.king])
            board.append(new_row)
        data_dict["Board"] = board
        json.dump(data_dict, DB)

def get_board():
    with open('checkers/data.json', 'r') as DB:
        data_dict = json.loads(DB.read())
        board = data_dict["Board"]
        state_board = []
        for row in board:
            new_row = []
            for cell in row:
                if(cell == 0):
                    new_row.append(0)
                else:
                    new_row.append(Piece(cell[0], cell[1], rgb_to_color(cell[2]), cell[3]))
            state_board.append(new_row)
        return state_board
