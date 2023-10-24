from pico2d import *

import game_world
from archery_cat import Archery_cat
from start_screen import Start_screen
from start_screen import Start_back
from archery_background import Archery_background
from target import Target_50, Target_100


# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            archery_cat.handle_event(event)

def create_world():
    global running
    global archery_cat

    running = True

    #스타트 화면
    # start_back = Start_back()
    # world.append(start_back)
    #
    # start_screen = Start_screen()
    # world.append(start_screen)

    archery_background = Archery_background()
    game_world.add_object(archery_background)

    archery_cat = Archery_cat()
    game_world.add_object(archery_cat)

    # target_50 = [Target_50 for i in range(11)]
    # target_50 = Target_50()
    # for i in range(11):
    #     game_world.add_object(target_50[i])
    # game_world.add_object(target_50)


    target_50 = Target_50()
    game_world.add_object(target_50)

    target_100 = Target_100()
    game_world.add_object(target_100)

def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas(1000,600)
create_world()
hide_lattice() # 격자 숨기기

# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
