import pygame
import Consts
import MineField

soldier = pygame.image.load = pygame.image.load('soldier.png').convert_alpha()
soldier = pygame.transform.scale(soldier, (60, 120))


def initialize_soldier():
    for i in range(0, 4):
        for j in range(0, 2):
            MineField.mine_field[i][j] = Consts.SOLDIER_SQUARE

