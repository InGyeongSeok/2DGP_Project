# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import load_image, get_time, load_font, clamp, draw_rectangle
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT, SDLK_a, SDLK_UP, SDLK_DOWN

import game_framework
import game_world
import pingpong_mode


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
def space_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_SPACE

# time_out = lambda e : e[0] == 'TIME_OUT'
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 1


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
        pingpong_cat.frame = (pingpong_cat.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

    @staticmethod
    def draw(pingpong_cat):
        pingpong_cat.image_Idle.clip_draw(int(pingpong_cat.frame) * 50, 0, 40, 45, pingpong_cat.x, pingpong_cat.y, 150,150)


class Run:

    @staticmethod
    def enter(pingpong_cat, e):
        # print("Run enter")
        if right_down(e) or left_up(e):  # 오른쪽으로 RUN
            pingpong_cat.dirx = 1
            pingpong_cat.diry = 0
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN
            pingpong_cat.dirx = -1
            pingpong_cat.diry = 0
        elif up_down(e) or down_up(e):  # 위로 RUN
            pingpong_cat.diry = 1
            pingpong_cat.dirx = 0
        elif down_down(e) or up_up(e):  # 아래로 RUN
            pingpong_cat.diry = -1
            pingpong_cat.dirx = 0

        pass

    @staticmethod
    def exit(pingpong_cat, e):
        pass

    @staticmethod
    def do(pingpong_cat):
        # archery_cat.frame = (archery_cat.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        # archery_cat.x += archery_cat.dir * RUN_SPEED_PPS * game_framework.frame_time
        pingpong_cat.x = clamp(125, pingpong_cat.x, 270)
        pingpong_cat.y = clamp(100, pingpong_cat.y, 500)

        pingpong_cat.frame = (pingpong_cat.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        pingpong_cat.x += pingpong_cat.dirx * RUN_SPEED_PPS * game_framework.frame_time
        pingpong_cat.y += pingpong_cat.diry * RUN_SPEED_PPS * game_framework.frame_time

        pass

    @staticmethod
    def draw(pingpong_cat):
        pingpong_cat.image_Idle.clip_draw(int(pingpong_cat.frame) * 50, 0, 40, 45, pingpong_cat.x, pingpong_cat.y, 150,150)
        pass

class Smash:

    @staticmethod
    def enter(pingpong_cat, e):
        pass
    @staticmethod
    def exit(pingpong_cat, e):
        pingpong_cat.flag = 0
        pass

    @staticmethod
    def do(pingpong_cat):
        if pingpong_cat.smash >= 5:
            pingpong_cat.flag = 1
            pingpong_cat.smash = 0
        pingpong_cat.frame = (pingpong_cat.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        pass

    @staticmethod
    def draw(pingpong_cat):
        pingpong_cat.image_Idle.clip_draw(int(pingpong_cat.frame) * 50, 0, 40, 45, pingpong_cat.x, pingpong_cat.y, 150,150)

        pass

class StateMachine:
    def __init__(self, pingpong_cat):
        self.pingpong_cat = pingpong_cat
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, space_down: Smash,
                   up_down: Run, down_down: Run},
            Run: {right_down: Run, left_down: Run, right_up: Idle, left_up: Idle,
                  up_down: Run, up_up: Idle, down_down: Run, down_up: Idle, space_down: Smash},
            Smash:{right_down: Idle, left_down: Idle, up_down: Idle, down_down: Idle, space_up: Idle}
        }

    def start(self):
        self.cur_state.enter(self.pingpong_cat, ('NONE', 0))

    def update(self):
        if get_time() - pingpong_mode.wait_time > 4 and get_time() - pingpong_mode.wait_time < 64:
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
        self.font = load_font('ENCR10B.TTF', 20)
        self.smash = 0
        self.flag = 0

    def update(self):
        # print(self.y)
        self.state_machine.update()

    def handle_event(self, event):

        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        # draw_rectangle(*self.get_bb())  # 튜플을 풀어해쳐서 각각 인자로 전달
        # self.font.draw(self.x - 10, self.y + 50, f'{self.smash:02d}', (255, 255, 0))

    def handle_collision(self, group, other):
        pass


    def get_bb(self):

        return self.x + 10 , self.y - 50, self.x + 40, self.y


