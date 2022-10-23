import Consts
import random

mine_field = []


def initialize_flag():
    for i in range(21, 24):
        for j in range(46, 50):
            mine_field[i][j] = Consts.FLAG_SQUARE


def initialize_mine_field():
    for i in range(Consts.NUM_OF_ROWS):
        mine_field.append([])
        for j in range(Consts.NUM_OF_COLS):
            mine_field[i].append(Consts.EMPTY_SQUARE)


def place_mines():
    for i in range(Consts.NUM_OF_MINES):
        row = random.randint(0, Consts.NUM_OF_ROWS - 1)
        col = random.randint(0, Consts.NUM_OF_COLS - 1)
        mine_field[row][col] = Consts.MINE_SQUARE
