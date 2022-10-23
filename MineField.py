import Consts

mine_field = []


def initialize_mine_field():
    for i in range(Consts.NUM_OF_ROWS):
        mine_field.append([])
        for j in range(Consts.NUM_OF_COLS):
            mine_field[i].append(Consts.EMPTY_SQUARE)