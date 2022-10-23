import pygame
import Consts
import MineField

soldier = pygame.image.load = pygame.image.load('soldier.png').convert_alpha()
soldier = pygame.transform.scale(soldier, (60, 120))


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
