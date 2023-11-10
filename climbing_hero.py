# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import load_image, get_time, load_font, clamp
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT, SDLK_a, SDLK_UP, SDLK_DOWN

import game_framework
import game_world


# state event check
# ( state event type, event value )

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def up_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP


def up_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP


def down_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN


def down_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


# time_out = lambda e : e[0] == 'TIME_OUT'
# PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
# RUN_SPEED_KMPH = 20.0  # Km / Hour
# RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
# RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
# RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
#
# TIME_PER_ACTION = 0.5
# ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
# FRAMES_PER_ACTION = 6


class Idle:

    @staticmethod
    def enter(climbing_cat, e):
        climbing_cat.frame = 0
        # archery_cat.wait_time = get_time()  # pico2d import 필요

    @staticmethod
    def exit(climbing_cat, e):
        pass

    @staticmethod
    def do(climbing_cat):
        climbing_cat.frame = (climbing_cat.frame + 1) % 200
        pass

    @staticmethod
    def draw(climbing_cat):
        climbing_cat.image_Idle.clip_draw(32 * (climbing_cat.frame // 100), 0, 20, 24, climbing_cat.x, climbing_cat.y , 70, 70)



class Run:

    @staticmethod
    def enter(climbing_cat, e):
        if right_down(e) or left_up(e):  # 오른쪽으로 RUN
            climbing_cat.dirx = 0.5
            climbing_cat.diry = 0
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN
            climbing_cat.dirx = -0.5
            climbing_cat.diry = 0
        elif up_down(e) or down_up(e):  # 위로 RUN
            climbing_cat.diry = 0.5
            climbing_cat.dirx = 0
        elif down_down(e) or up_up(e):  # 아래로 RUN
            climbing_cat.diry = -0.5
            climbing_cat.dirx = 0


    @staticmethod
    def exit(climbing_cat, e):
        pass

    @staticmethod
    def do(climbing_cat):
        # archery_cat.frame = (archery_cat.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        # archery_cat.x += archery_cat.dir * RUN_SPEED_PPS * game_framework.frame_time
        climbing_cat.x = clamp(50, climbing_cat.x, 1000 - 50)
        climbing_cat.frame = (climbing_cat.frame + 1) % 200
        climbing_cat.x += climbing_cat.dirx
        climbing_cat.y += climbing_cat.diry


        pass

    @staticmethod
    def draw(climbing_cat):
        if climbing_cat.dirx == 0.5:
               climbing_cat.image_right.clip_draw(32* (climbing_cat.frame // 50), 0, 24, 23, climbing_cat.x, climbing_cat.y, 70, 70)
        elif climbing_cat.dirx == -0.5:
               climbing_cat.image_left.clip_draw(35* (climbing_cat.frame // 50), 0, 24, 23, climbing_cat.x, climbing_cat.y, 70, 70)
        elif climbing_cat.diry == -0.5:
            climbing_cat.image_down.clip_draw(20 * (climbing_cat.frame // 50), 0, 20, 23, climbing_cat.x,
                                              climbing_cat.y, 70, 70)
        elif climbing_cat.diry == 0.5:
            climbing_cat.image_up.clip_draw(20 * (climbing_cat.frame //50), 0, 20, 25, climbing_cat.x,
                                              climbing_cat.y, 70, 70)





class StateMachine:
    def __init__(self, climbing_cat):
        self.climbing_cat = climbing_cat
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, space_down: Idle,
                   up_down: Run, up_up: Run, down_down: Run, down_up: Run},
            Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle,
                  up_down: Run, up_up: Idle, down_down: Run, down_up: Idle}
        }

    def start(self):
        self.cur_state.enter(self.climbing_cat, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.climbing_cat)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.climbing_cat, e)
                self.cur_state = next_state
                self.cur_state.enter(self.climbing_cat, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.climbing_cat)


class Climbing_cat:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 20)
        self.x, self.y = 400, 300
        self.frame = 0
        self.dirx = 0
        self.diry = 0
        self.image_Idle = load_image('resource/Climbing/Idle.png')
        self.image_right = load_image('resource/Climbing/right.png')
        self.image_left = load_image('resource/Climbing/left.png')
        self.image_up = load_image('resource/Climbing/back.png')
        self.image_down = load_image('resource/Climbing/front.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        # self.font.draw(self.x - 10, self.y + 48, f'{archery_mode.archery_score:02d}', (255, 255, 0))





