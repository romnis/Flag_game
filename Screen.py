import pygame
import Consts
import random

x = random.randint(0, Consts.WINDOW_HEIGHT - Consts.GRASS_HEIGHT)
y = random.randint(0, Consts.WINDOW_WIDTH - Consts.GRASS_WIDTH)

pygame.display.set_caption('Flag Game')
screen = pygame.display.set_mode(
    (Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))


# grass = pygame.image.load = pygame.image.load('grass.png').convert_alpha()


def draw_grid():
    # for i in range(Consts.NUM_OF_ROWS):
    #     pygame.draw.line(screen, Consts.BLACK, start_pos=(0, 0, 0),
    #                      end_pos=Consts.WINDOW_WIDTH)
    pass


def create_grass(grass_img):
    grass = pygame.image.load(grass_img)
    sized_grass = pygame.transform.scale(grass, (
        Consts.GRASS_WIDTH, Consts.GRASS_HEIGHT))
    screen.blit(sized_grass, (x, y))


def create_flag(flag_img):
    flag = pygame.image.load(flag_img)
    sized_flag = pygame.transform.scale(flag,
                                        (Consts.FLAG_WIDTH, Consts.FLAG_HEIGHT))
    screen.blit(sized_flag, (Consts.WINDOW_WIDTH - Consts.FLAG_WIDTH,
                             Consts.WINDOW_HEIGHT - Consts.FLAG_HEIGHT))


def choose_random():
    x = random.randint(0, Consts.WINDOW_HEIGHT - Consts.GRASS_HEIGHT)
    y = random.randint(0, Consts.WINDOW_WIDTH - Consts.GRASS_WIDTH)
    return x, y


def place_all_grasses():
    for i in range(20):
        create_grass(Consts.GRASS_IMG)
        choose_random()


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


def draw_game(game_state):
    screen.fill(Consts.BACKGROUND_COLOR)
    place_all_grasses()
    create_flag(Consts.FLAG_IMG)
    pygame.display.flip()
