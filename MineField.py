import Consts


def initialize_flag():
    for i in range(21, 24):
        for j in range(46, 50):
            mine_field[i][j] = Consts.FLAG_SQUARE
import Consts

mine_field = []


def initialize_mine_field():
    for i in range(Consts.NUM_OF_ROWS):
        mine_field.append([])
        for j in range(Consts.NUM_OF_COLS):
            mine_field[i].append(Consts.EMPTY_SQUARE)