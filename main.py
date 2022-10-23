import pygame
import Consts

state = {
    "is_window_open": True,
    "state": Consts.RUNNING_STATE,

}


def main():
    pygame.init()

    while state["is_window_open"]:
        handle_user_events()


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != Consts.RUNNING_STATE:
            continue
