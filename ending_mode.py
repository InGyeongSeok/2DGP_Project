import random

from pico2d import *

import game_framework
import game_world
from ending import Ending


# Game object class here


def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif  (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE) and get_time() - wait_time > 10:
            game_framework.quit()
        # else:
        #     archery_cat.handle_event(event)


def init():


    global wait_time

    wait_time = get_time()

    ending = Ending()

    game_world.add_object(ending, 0)


def update():

    game_world.update()
    game_world.handle_collision()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()
    pass

def pause():

    pass

def resume():

    pass
