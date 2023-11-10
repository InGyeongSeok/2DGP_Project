from pico2d import *

import game_framework
import game_world
import title_mode
from climbing_background import Climbing_background
from climbing_hero import Climbing_cat


def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        else:
            climbing_cat.handle_event(event)



def init():
    global climbing_cat

    climbing_background = Climbing_background()
    game_world.add_object(climbing_background, 0)

    climbing_cat = Climbing_cat()
    game_world.add_object(climbing_cat, 0)

def update():
    game_world.update()


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
