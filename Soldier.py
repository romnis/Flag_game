import Consts
import MineField


# soldier = pygame.image.load = pygame.image.load('soldier.png').convert_alpha()
# pygame.display.flip()
# soldier = pygame.transform.scale(soldier, (60, 120))


def move_right(state):
    if state["soldier_col"] < 48:
        state["soldier_col"] += 1


def move_left(state):
    if state["soldier_col"] > 0:
        state["soldier_col"] -= 1


def move_up(state):
    if state["soldier_row"] > 0:
        state["soldier_row"] += 1


def move_down(state):
    if state["soldier_row"] < 23:
        state["soldier_row"] -= 1


def touched_mine(soldier_col, soldier_row):
    soldier_left_leg = (soldier_row + 2, soldier_col)
    soldier_right_leg = (soldier_row + 2, soldier_col + 1)

    if MineField.mine_field[soldier_left_leg[0]][soldier_left_leg[1]] == Consts.MINE_SQUARE or \
            MineField.mine_field[soldier_right_leg[0]][soldier_right_leg[1]] == Consts.MINE_SQUARE:
        return True
    return False


def touched_flag(soldier_col, soldier_row):
    soldier_right_up_corner = (soldier_row, soldier_col + 1)
    soldier_left_middle_corner = (soldier_row + 1, soldier_col)
    soldier_right_middle_corner = (soldier_row + 1, soldier_col + 1)

    if MineField.mine_field[soldier_right_up_corner[0]][soldier_right_up_corner[1]] \
        == Consts.FLAG_SQUARE or \
            MineField.mine_field[soldier_left_middle_corner[0]][soldier_left_middle_corner[1]] \
        == Consts.FLAG_SQUARE or \
            MineField.mine_field[soldier_right_middle_corner[0]][soldier_right_middle_corner[1]] \
        == Consts.FLAG_SQUARE or \
            MineField.mine_field[soldier_col][soldier_row] == Consts.FLAG_SQUARE:
        return True
    return False


