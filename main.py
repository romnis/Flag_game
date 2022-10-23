import pygame
import Consts
import Screen

state = {
    "is_window_open": True,
    "state": Consts.RUNNING_STATE,


}


def main():
    pygame.init()

    while state["is_window_open"]:
        handle_user_events()

    Screen.draw_game(state)


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != Consts.RUNNING_STATE:
            continue

        elif event.type == pygame.K_RIGHT:
            pass

        elif event.type == pygame.K_LEFT:
            pass

        elif event.type == pygame.K_UP:
            pass

        elif event.type == pygame.K_DOWN:
            pass
