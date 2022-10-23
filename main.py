import pygame
import Consts
import MineField
import Screen
import Soldier
import time

state = {
    "is_window_open": True,
    "state": Consts.RUNNING_STATE,
    "soldier_col": 0,
    "soldier_row": 0
}


def main():
    pygame.init()
    MineField.initialize_mine_field()
    MineField.place_mines()

    while state["is_window_open"]:
        handle_user_events()

        if Soldier.touched_flag():
            Screen.draw_win_message()
            time.sleep(3)
            state["is_window_open"] = False

        if Soldier.touched_mine(state["soldier_col"], state["soldier_row"]):
            Screen.draw_lose_message()
            time.sleep(3)
            state["is_window_open"] = False

        Screen.draw_game(state)
    # Screen.draw_grid()


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != Consts.RUNNING_STATE:
            continue

        elif event.type == pygame.K_RIGHT:
            Soldier.move_right(state)

        elif event.type == pygame.K_LEFT:
            Soldier.move_left(state)

        elif event.type == pygame.K_UP:
            Soldier.move_up(state)

        elif event.type == pygame.K_DOWN:
            Soldier.move_down(state)

        elif event.type == pygame.K_KP_ENTER:
            pass


main()
