from pico2d import get_events, load_image, clear_canvas, update_canvas, get_time
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE, SDL_MOUSEBUTTONDOWN

import game_framework
import archery_mode
from title import Start_back, Start_screen, Start_play


def init():
    # global image
    #
    # image = load_image('title.png')
    global start_back
    global start_screen
    global start_play
    start_back = Start_back()
    start_screen = Start_screen()
    start_play = Start_play()


    pass

def finish():
    pass


def update():
    start_play.update()
    pass

def draw():
    clear_canvas()
    # image.draw(400,300)
    start_back.draw()
    start_screen.draw()
    start_play.draw()
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            game_framework.change_mode(play_mode)


def pause():
    pass

def resume():
    pass