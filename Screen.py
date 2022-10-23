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
    create_grass(Consts.GRASS_IMG)


def create_grass(grass_img):
    for i in range(20):
        y = random.randint(0, Consts.WINDOW_WIDTH - Consts.GRASS_WIDTH)
        x = random.randint(0, Consts.WINDOW_HEIGHT - Consts.GRASS_HEIGHT)
        grass = pygame.image.load(grass_img)
        sized_grass = pygame.transform.scale(grass, (
            Consts.GRASS_WIDTH, Consts.GRASS_HEIGHT))

        grass_box = pygame.Surface(
            (Consts.GRASS_WIDTH, Consts.GRASS_HEIGHT * 2), )
        grass_box.fill(Consts.BACKGROUND_COLOR)
        grass_box.blit(sized_grass, (x, y))
        # screen.blit(grass_box, (x, y))
        return grass_box


def draw_grass(grass):
    # grass_rect = grass.get_rect()
    # screen.blit(grass_box, (x, y))
    pass


def create_flag(flag_img):
    flag = pygame.image.load(flag_img)
    sized_grass = pygame.transform.scale(flag, (
        Consts.FLAG_WIDTH, Consts.FLAG_HEIGHT))
    flag_box = pygame.Surface(
        (Consts.GRASS_WIDTH, Consts.GRASS_HEIGHT * 2), )
    flag_box.fill(Consts.BACKGROUND_COLOR)
    flag_box.blit(sized_grass, (0, 0))



def draw_lose_message():
    draw_message(Consts.LOSE_MESSAGE, Consts.LOSE_FONT_SIZE,
                 Consts.LOSE_COLOR, Consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(Consts.WIN_MESSAGE, Consts.WIN_FONT_SIZE,
                 Consts.WIN_COLOR, Consts.WIN_LOCATION)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(Consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)



