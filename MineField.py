import Consts


def initialize_flag():
    for i in range(21, 24):
        for j in range(46, 50):
            mine_field[i][j] = Consts.FLAG_SQUARE
