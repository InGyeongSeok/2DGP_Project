from pico2d import *

import archery_mode
import climbing_mode
import game_framework
import game_world
import title_mode
from pingpong_ai import PingPong_ai
from pingpong_background import Pingpong_background
from pingpong_ball import Ball
from pingpong_hero import Pingpong_cat


def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == pico2d.SDLK_1:
            game_framework.change_mode(archery_mode)
        elif event.type == SDL_KEYDOWN and event.key == pico2d.SDLK_2:
            game_framework.change_mode(climbing_mode)
        else:
            pingpong_cat.handle_event(event)


def init():
    global pingpong_cat
    global pingpong_ai
    pingpong_background = Pingpong_background()
    game_world.add_object(pingpong_background, 0)

    pingpong_cat = Pingpong_cat()
    game_world.add_object(pingpong_cat, 0)


    pingpong_ai = PingPong_ai()
    game_world.add_object(pingpong_ai, 2)



    game_world.add_collision_pair('ai:ball', None, pingpong_ai)
    ball = Ball()
    game_world.add_object(ball, 1)

    game_world.add_collision_pair('hero:ball', ball, None)
    game_world.add_collision_pair('ai:ball', ball, None)

    game_world.add_collision_pair('hero:ball', None, pingpong_cat)
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
