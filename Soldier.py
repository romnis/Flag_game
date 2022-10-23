import pygame

import Consts
import MineField

soldier = pygame.image.load = pygame.image.load('soldier.png').convert_alpha()
soldier = pygame.transform.scale(soldier, (60, 120))


def initialize_soldier():
    for i in range(4):
        MineField.mine_field[i][0] = Consts.SOLDIER_SQUARE
        MineField.mine_field[i][1] = Consts.SOLDIER_SQUARE

