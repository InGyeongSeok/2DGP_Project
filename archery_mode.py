import random

from pico2d import *

import climbing_mode
import game_framework
import game_world
import pingpong_mode
import title_mode
from archery_ai import Archery_ai

from archery_background import Archery_background
from archery_target import Target_50, Target_100
from archery_hero import Archery_cat
from game_timer import Gametimer
from score import Score


# Game object class here


def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif get_time() - wait_time > 3 and get_time() - wait_time < 64:
            archery_cat.handle_event(event)
        elif event.type == SDL_KEYDOWN and event.key == pico2d.SDLK_2 and get_time() - wait_time > 64:
            game_framework.change_mode(climbing_mode)
        elif event.type == SDL_KEYDOWN and event.key == pico2d.SDLK_3 and get_time() - wait_time > 64:
            game_framework.change_mode(pingpong_mode)
        # else:
        #     archery_cat.handle_event(event)


def init():
    global archery_cat
    global archery_score
    global ai_score

    global wait_time
    global target_50
    global target_100
    global archery_time
    global target_time
    # global target_bomb

    wait_time = get_time()
    archery_time = 60
    archery_score = 0
    ai_score = 0

    archery_background = Archery_background()
    game_world.add_object(archery_background, 0)

    archery_cat = Archery_cat()
    game_world.add_object(archery_cat, 0)

    target_50 = [Target_50() for i in range(8)]
    game_world.add_objects(target_50, 0)

    target_100 = [Target_100() for i in range(10)]
    game_world.add_objects(target_100, 0)

    # target_bomb = [Target_bomb() for i in range(3)]
    # game_world.add_objects(target_bomb, 0)

    gametimer = Gametimer(64)
    game_world.add_object(gametimer, 2)



    for s_score in target_50:
        game_world.add_collision_pair('s_score:hero', s_score, None)
        game_world.add_collision_pair('s_score:ai', s_score, None)


    for b_score in target_100:
        game_world.add_collision_pair('b_score:hero', b_score, None)
        game_world.add_collision_pair('b_score:ai', b_score, None)


    # for bomb in target_bomb:
    #     game_world.add_collision_pair('bomb:arrow', bomb, None)

    archery_ai = Archery_ai()
    game_world.add_object(archery_ai, 2)
    # game_world.add_collision_pair('zombie:ball', zombie, None)

    target_time = get_time()




def update():
    global archery_score
    global ai_score
    global target_50
    global target_100
    global target_time
    if get_time() - target_time > 15:
        target_50 = [Target_50() for _ in range(8)]
        game_world.add_objects(target_50, 0)
        for s_score in target_50:
            game_world.add_collision_pair('s_score:hero', s_score, None)
            game_world.add_collision_pair('s_score:ai', s_score, None)
        target_100 = [Target_100() for _ in range(5)]
        game_world.add_objects(target_100, 0)
        for b_score in target_100:
            game_world.add_collision_pair('b_score:hero', b_score, None)
            game_world.add_collision_pair('b_score:ai', b_score, None)
        target_time = get_time()
    game_world.update()
    game_world.handle_collision()

    if get_time() - wait_time > 64:
        score_screen = Score(1, archery_score, ai_score)
        game_world.add_object(score_screen, 2)


    # if get_time() - wait_time > 5:
    #     score_screen = Score(1, archery_score, ai_score)
    #     game_world.add_object(score_screen, 2)

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()
    pass

def pause():
    archery_cat.wait_time = 100000000000000000000000000000000000.0
    pass

def resume():
    archery_cat.wait_time = get_time()
    pass
