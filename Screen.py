import pygame
import Consts
import Soldier
import MineField
import random

pygame.display.set_caption('Title of window')

screen = pygame.display.set_mode(
    (Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
pygame.display.set_caption('Title of window')


def draw_grid():
    for i in range(Consts.NUM_OF_ROWS):
        pygame.draw.line(screen, Consts.BLACK, start_pos=(0,
                         end_pos=Consts.WINDOW_WIDTH))


def draw_game(game_state):
    screen.fill(Consts.BACKGROUND_COLOR)
    pygame.display.flip()

def grass():
    print(random.randint(0,Consts.NUM_OF_COLS-3))

