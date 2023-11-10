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
# # RUN_SPEED_KMPH = 20.0  # Km / Hour
# # RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
# # RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
# # RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
# #
# # TIME_PER_ACTION = 0.5
# # ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
# # FRAMES_PER_ACTION = 4


class Idle:

    @staticmethod
    def enter(pingpong_cat, e):
        # pingpong_cat.frame = 0
        pass

    @staticmethod
    def exit(pingpong_cat, e):
        pass

    @staticmethod
    def do(pingpong_cat):
        pingpong_cat.frame = (pingpong_cat.frame + 1) % 360

    @staticmethod
    def draw(pingpong_cat):
        #수정 필요!
        if pingpong_cat.frame < 180:
            pingpong_cat.image_Idle.clip_draw(0, 0, 34, 40, pingpong_cat.x, pingpong_cat.y, 100, 115)
        else:
            pingpong_cat.image_Idle.clip_draw(30, 0, 60, 40, pingpong_cat.x, pingpong_cat.y, 180, 115)


class Run:

    @staticmethod
    def enter(pingpong_cat, e):
        # print("Run enter")
        if right_down(e) or left_up(e):  # 오른쪽으로 RUN
            pingpong_cat.dirx = 0.5
            pingpong_cat.diry = 0
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN
            pingpong_cat.dirx = -0.5
            pingpong_cat.diry = 0
        elif up_down(e) or down_up(e):  # 위로 RUN
            pingpong_cat.diry = 0.5
            pingpong_cat.dirx = 0
        elif down_down(e) or up_up(e):  # 아래로 RUN
            pingpong_cat.diry = -0.5
            pingpong_cat.dirx = 0

        pass

    @staticmethod
    def exit(pingpong_cat, e):
        pass

    @staticmethod
    def do(pingpong_cat):
        # archery_cat.frame = (archery_cat.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        # archery_cat.x += archery_cat.dir * RUN_SPEED_PPS * game_framework.frame_time
        pingpong_cat.x = clamp(50, pingpong_cat.x, 290)
        pingpong_cat.y = clamp(100, pingpong_cat.y, 600 - 100)

        pingpong_cat.frame = (pingpong_cat.frame + 1) % 360
        pingpong_cat.x += pingpong_cat.dirx
        pingpong_cat.y += pingpong_cat.diry

        pass

    @staticmethod
    def draw(pingpong_cat):
        # archery_cat.image_Run.clip_draw(int(archery_cat.frame) * 22, archery_cat.action * 31, 21, 25, archery_cat.x,
        #                                 archery_cat.y, 60, 60)
        if pingpong_cat.frame < 180:
            pingpong_cat.image_Idle.clip_draw(0, 0, 34, 40, pingpong_cat.x, pingpong_cat.y, 100, 115)
        else:
            pingpong_cat.image_Idle.clip_draw(30, 0, 60, 40, pingpong_cat.x, pingpong_cat.y, 180, 115)

        pass

class Smash:

    @staticmethod
    def enter(archery_cat, e):
        print("smash enter")

    @staticmethod
    def exit(archery_cat, e):
        pass

    @staticmethod
    def do(archery_cat):
        print("smash do")
        pass

    @staticmethod
    def draw(archery_cat):
        pass

class StateMachine:
    def __init__(self, pingpong_cat):
        self.pingpong_cat = pingpong_cat
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, space_down: Idle,
                   up_down: Run, up_up: Run, down_down: Run, down_up: Run},
            Run: {right_down: Run, left_down: Run, right_up: Idle, left_up: Idle,
                  up_down: Run, up_up: Idle, down_down: Run, down_up: Idle}
        }

    def start(self):
        self.cur_state.enter(self.pingpong_cat, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.pingpong_cat)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.pingpong_cat, e)
                self.cur_state = next_state
                self.cur_state.enter(self.pingpong_cat, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.pingpong_cat)


class Pingpong_cat:
    image = None
    def __init__(self):
        if Pingpong_cat.image == None:
            self.image_Idle = load_image('resource/PingPong/cat.png')
        # self.font = load_font('ENCR10B.TTF', 20)
        self.x, self.y = 200, 300
        self.frame = 0
        self.dirx = 0
        self.diry = 0
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):

        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()




