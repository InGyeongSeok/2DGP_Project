import random

from pico2d import *

import archery_mode
import climbing_hero
import game_framework
import game_world
import pingpong_mode
import title_mode
from climbing_background import Climbing_background
from climbing_hero import Climbing_cat
import server
from climbing_hold import Hold_pink, Hold_green
from climbing_snow import Climbing_snow
from game_timer import Gametimer
from score import Score

flag = 0

def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == pico2d.SDLK_1 and get_time() - wait_time > 34:
            game_framework.change_mode(archery_mode)
        elif event.type == SDL_KEYDOWN and event.key == pico2d.SDLK_3 and get_time() - wait_time > 34:
            game_framework.change_mode(pingpong_mode)
        elif get_time() - wait_time > 3 and get_time() - wait_time < 34:
            server.climbing_cat.handle_event(event)
        # else:
        #     server.climbing_cat.handle_event(event)




def init():
    global climbing_cat
    global wait_time
    global target_time
    global climb_time

    wait_time = get_time()
    target_time = 0
    climb_time = 30
    server.background = Climbing_background()
    game_world.add_object(server.background, 0)

    server.climbing_cat = Climbing_cat()
    game_world.add_object(server.climbing_cat, 1)

    gametimer = Gametimer(34)
    game_world.add_object(gametimer, 2)


    snow = [Climbing_snow(random.randint(0, 1000), random.randint(1200, 1600)) for i in range(3)]
    # snow.append(Climbing_snow())
    game_world.add_objects(snow, 1)

    for s in snow:
        game_world.add_collision_pair('snow:hero', None, s)
    game_world.add_collision_pair('snow:hero', server.climbing_cat, None)


    hold_green = [Hold_green() for i in range(10)]
    hold_pink = []
    for i in range(3):
        for j in range(13):
            hold_pink.append(Hold_pink(i * 400 + random.randint(50, 120), j * 80 + 200))

    hold_pink.append(Hold_pink(200, 1200))
    hold_pink.append(Hold_pink(350, 1250))
    hold_pink.append(Hold_pink(300, 1300))
    hold_pink.append(Hold_pink(400, 1350))
    hold_pink.append(Hold_pink(430, 1420))
    hold_pink.append(Hold_pink(390, 1500))
    hold_pink.append(Hold_pink(500, 1550))
    hold_pink.append(Hold_pink(620, 1550))
    hold_pink.append(Hold_pink(600, 1500))
    hold_pink.append(Hold_pink(700, 1420))

    hold_green.append(Hold_green(350, 1450))
    hold_green.append(Hold_green(550, 1400))
    hold_green.append(Hold_green(600, 1300))
    hold_green.append(Hold_green(680, 1500))

    for i in range(2):
        for j in range(3):
            hold_green.append(Hold_green(i * 800 + random.randint(50, 120), j * 100 + 1050))


    game_world.add_objects(hold_pink, 0)
    game_world.add_objects(hold_green, 0)

    for pink in hold_pink:
        game_world.add_collision_pair('pink:hero', None, pink)
    for green in hold_green:
        game_world.add_collision_pair('green:hero', None, green)

    game_world.add_collision_pair('pink:hero', server.climbing_cat, None)
    game_world.add_collision_pair('green:hero', server.climbing_cat, None)


def update():
    global target_time
    if get_time() - target_time > 10 and get_time() - wait_time < 34:
        snow = [Climbing_snow(random.randint(0, 1000), random.randint(1200, 1600)) for i in range(3)]
        # snow.append(Climbing_snow())
        game_world.add_objects(snow, 1)
        for s in snow:
            game_world.add_collision_pair('snow:hero', None, s)
        game_world.add_collision_pair('snow:hero', server.climbing_cat, None)
        target_time = get_time()
    game_world.update()
    game_world.handle_collision()

    if get_time() - wait_time > 30:
        score_screen = Score(2, server.climbing_cat.current_height_percent)
        game_world.add_object(score_screen, 2)

    # print(f'현재 높이: {server.climbing_cat.current_height_percent:.2f}%')

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
