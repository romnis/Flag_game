import pygame
import Consts
import Soldier
import MineField
import random

# import sklearn
# from skimage import io


pygame.display.set_caption('Title of window')

screen = pygame.display.set_mode(
    (Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
pygame.display.set_caption('Title of window')

# grass = pygame.image.load = pygame.image.load('grass.png').convert_alpha()


def draw_grid():
    # for i in range(Consts.NUM_OF_ROWS):
    #     pygame.draw.line(screen, Consts.BLACK, start_pos=(0, 0, 0),
    #                      end_pos=Consts.WINDOW_WIDTH)
    pass


def draw_game(game_state):
    screen.fill(Consts.BACKGROUND_COLOR)
    pygame.display.flip()


def grass(grass_img):
    for i in range(20):
        y = random.randint(0, Consts.NUM_OF_COLS - 3)
        x = random.randint(0, Consts.NUM_OF_ROWS)
        grass = pygame.image.load(grass_img)
        sized_grass = pygame.transform.scale(grass, (
            Consts.GRASS_WIDTH, Consts.GRASS_HEIGHT))

        grass_box = pygame.Surface(
            (Consts.GRASS_WIDTH, Consts.GRASS_HEIGHT * 2), )
        grass_box.fill(Consts.BACKGROUND_COLOR)
        grass_box.blit(sized_grass, (x, y))
        screen.blit(grass_box)
def draw_grass
