from pico2d import *

from archery_cat import Archery_cat
from start_screen import Start_screen
from start_screen import Start_back
from archery_background import Archery_background


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

def reset_world():
    global running
    global world
    global archery_cat

    running = True
    world = []

    # start_back = Start_back()
    # world.append(start_back)
    #
    # start_screen = Start_screen()
    # world.append(start_screen)
    #
    archery_background = Archery_background()
    world.append(archery_background)

    archery_cat = Archery_cat()
    world.append(archery_cat)
def update_world():
    for o in world:
        o.update()
    pass


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas(1000,600)
reset_world()
hide_lattice() # 격자 숨기기

# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
