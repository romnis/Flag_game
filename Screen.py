import pygame
import Consts
import random

screen = pygame.display.set_mode(
    (Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
pygame.display.set_caption('Flag Game')


# grass = pygame.image.load = pygame.image.load('grass.png').convert_alpha()


def draw_grid():
    # for i in range(Consts.NUM_OF_ROWS):
    #     pygame.draw.line(screen, Consts.BLACK, start_pos=(0, 0, 0),
    #                      end_pos=Consts.WINDOW_WIDTH)
    pass


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
        screen.blit(grass_box, (x, y))
        return grass_box


def draw_grass(grass):
    pass


# grass_rect = grass.get_rect()
# screen.blit(grass_box, (x, y))


def create_flag(flag_img):
    pygame.display.set_caption(flag_img)
    imp = pygame.image.load("C:/Users/masha/PycharmProjects/pythonProject7/flag.png").convert()
    sized_flag = pygame.transform.scale(imp, (
        Consts.FLAG_WIDTH, Consts.FLAG_HEIGHT))
    screen.blit(sized_flag, (Consts.WINDOW_WIDTH - Consts.FLAG_WIDTH, Consts.WINDOW_HEIGHT - Consts.FLAG_HEIGHT))
    pygame.display.flip()


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
    create_grass(Consts.GRASS_IMG)
    pygame.display.flip()
    create_flag(Consts.FLAG_IMG)
