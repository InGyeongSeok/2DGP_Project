# 이것은 각 상태들을 객체로 구현한 것임.
import climbing_mode
import server

from pico2d import load_image, get_time, load_font, clamp, get_canvas_height, get_canvas_width, draw_rectangle
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT, SDLK_a, SDLK_UP, SDLK_DOWN
import climbing_hold
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

def time_out(e):
    return e[0] == 'TIME_OUT'

def hold_out(e):
    return e[0] == 'Hold_out'

def hold(e):
    return e[0] == 'Hold'

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


class Idle:

    @staticmethod
    def enter(climbing_cat, e):
        climbing_cat.frame = 0

    @staticmethod
    def exit(climbing_cat, e):
        pass

    @staticmethod
    def do(climbing_cat):

        climbing_cat.x = clamp(45, climbing_cat.x, server.background.w -45)
        climbing_cat.y = clamp(45, climbing_cat.y, server.background.h - 275)
        climbing_cat.frame = (climbing_cat.frame + game_framework.frame_time) % 2


        if climbing_cat.y > 130 and climbing_cat.y < 1615:
            climbing_cat.y -= 1

        pass

    @staticmethod
    def draw(climbing_cat):
        sx, sy = climbing_cat.x - server.background.window_left, climbing_cat.y - server.background.window_bottom

        climbing_cat.image_Idle.clip_draw(32 * int(climbing_cat.frame // 1), 0, 20, 24, sx, sy , 90, 90)

class Hold:

    @staticmethod
    def enter(climbing_cat, e):
        climbing_cat.frame = 0

    @staticmethod
    def exit(climbing_cat, e):
        pass

    @staticmethod
    def do(climbing_cat):
        climbing_cat.x = clamp(45, climbing_cat.x, server.background.w-45)
        climbing_cat.y = clamp(45, climbing_cat.y, server.background.h - 275)
        climbing_cat.frame = (climbing_cat.frame + 5 * game_framework.frame_time) % 3

        climbing_cat.x = climbing_hold.holdx - 5
        climbing_cat.y = climbing_hold.holdy -55
        pass

    @staticmethod
    def draw(climbing_cat):
        sx, sy = climbing_cat.x - server.background.window_left, climbing_cat.y - server.background.window_bottom

        climbing_cat.image_jump.clip_draw(32 * int(climbing_cat.frame + 3) + 1, 0, 21, 35, sx, sy , 90, 120)

class Fall:

    @staticmethod
    def enter(climbing_cat, e):
        climbing_cat.frame = 0

        climbing_cat.wait_time = get_time()
    @staticmethod
    def exit(climbing_cat, e):
        pass

    @staticmethod
    def do(climbing_cat):

        climbing_cat.x = clamp(45, climbing_cat.x, server.background.w -45)
        climbing_cat.y = clamp(45, climbing_cat.y, server.background.h - 275)
        climbing_cat.frame = (climbing_cat.frame + 8 * game_framework.frame_time) % 2


        if climbing_cat.y > 130 and climbing_cat.y < 1615:
            climbing_cat.y -= RUN_SPEED_PPS * game_framework.frame_time
        if get_time() - climbing_cat.wait_time > 0.5:
            climbing_cat.state_machine.handle_event(('TIME_OUT', 0))
        pass

    @staticmethod
    def draw(climbing_cat):
        sx, sy = climbing_cat.x - server.background.window_left, climbing_cat.y - server.background.window_bottom
        climbing_cat.image_fall.clip_draw(39 * int(climbing_cat.frame), 0, 22, 32, sx, sy , 90, 90)

class Jump:

    @staticmethod
    def enter(climbing_cat, e):
        climbing_cat.frame = 0
        climbing_cat.wait_time = get_time()

    @staticmethod
    def exit(climbing_cat, e):
        pass

    @staticmethod
    def do(climbing_cat):
        climbing_cat.x = clamp(45, climbing_cat.x, server.background.w-45)
        climbing_cat.y = clamp(45, climbing_cat.y, server.background.h - 275)
        if get_time() - climbing_cat.wait_time <= 0.5:
            climbing_cat.y += RUN_SPEED_PPS * game_framework.frame_time
        elif get_time() - climbing_cat.wait_time <= 1:
            climbing_cat.y -= RUN_SPEED_PPS * game_framework.frame_time
        if get_time() - climbing_cat.wait_time > 1:
            climbing_cat.state_machine.handle_event(('TIME_OUT', 0))
        # print(climbing_cat.y )
        pass

    @staticmethod
    def draw(climbing_cat):
        sx, sy = climbing_cat.x - server.background.window_left, climbing_cat.y - server.background.window_bottom

        climbing_cat.image_jump.clip_draw(0, 0, 25, 35, sx, sy, 100, 100)


class Run:

    @staticmethod
    def enter(climbing_cat, e):
        climbing_cat.wait_time = get_time()

        if right_down(e) or left_up(e):  # 오른쪽으로 RUN
            climbing_cat.dirx = 1
            climbing_cat.diry = 0
            climbing_cat.action = 1
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN
            climbing_cat.dirx = -1
            climbing_cat.diry = 0
            climbing_cat.action = 2
        elif up_down(e) or down_up(e):  # 위로 RUN
            climbing_cat.diry = 1
            climbing_cat.dirx = 0
            climbing_cat.action = 3
        elif down_down(e) or up_up(e):  # 아래로 RUN
            climbing_cat.diry = -1
            climbing_cat.dirx = 0
            climbing_cat.action = 4

    @staticmethod
    def exit(climbing_cat, e):
        pass

    @staticmethod
    def do(climbing_cat):
        climbing_cat.x = clamp(45, climbing_cat.x, server.background.w- 45 )
        climbing_cat.y = clamp(45, climbing_cat.y, server.background.h-275)

        climbing_cat.frame = (climbing_cat.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

        climbing_cat.x += climbing_cat.dirx * RUN_SPEED_PPS * game_framework.frame_time
        climbing_cat.y += climbing_cat.diry * RUN_SPEED_PPS * game_framework.frame_time
        if get_time() - climbing_cat.wait_time > 0.5:
            climbing_cat.state_machine.handle_event(('TIME_OUT', 0))


        pass

    @staticmethod
    def draw(climbing_cat):
        sx, sy = climbing_cat.x - server.background.window_left, climbing_cat.y - server.background.window_bottom

        if climbing_cat.action == 1:
            climbing_cat.image_right.clip_draw(32* int(climbing_cat.frame) , 0, 24, 23, sx, sy, 90, 90)
        elif climbing_cat.action == 2:
            climbing_cat.image_left.clip_draw(35* int(climbing_cat.frame ), 0, 24, 23, sx, sy, 90, 90)
        elif climbing_cat.action == 4:
            climbing_cat.image_down.clip_draw(20 * int(climbing_cat.frame ), 0, 20, 23, sx,
                                              sy, 90, 90)
        elif climbing_cat.action == 3:
            climbing_cat.image_up.clip_draw(20 * int(climbing_cat.frame), 0, 20, 25, sx,
                                              sy, 90, 90)






class StateMachine:
    def __init__(self, climbing_cat):

        self.climbing_cat = climbing_cat
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, space_down: Jump,
                   up_down: Run, down_down: Run, hold:Hold ,  hold_out : Fall},
            Run: {right_down: Run, left_down: Run, right_up: Idle, left_up: Idle,
                  up_down: Run, up_up: Idle, down_down: Run, down_up: Idle, hold: Hold
                  ,time_out: Idle,  hold_out : Fall},
            Jump: {right_down: Run, left_down: Run, left_up: Run, right_up: Run,
                   up_down: Run, up_up: Run, down_down: Run, down_up: Run,
                   time_out: Idle,  hold_out : Fall},
            Hold: {right_down: Run, left_down: Run, space_down: Jump, hold_out : Fall},
            Fall:{right_down: Run, left_down: Run, space_down: Jump, time_out : Idle}
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
        self.x, self.y =500, 45
        self.frame = 0
        self.dirx = 0
        self.diry = 0
        self.action = 0
        self.image_Idle = load_image('resource/Climbing/Idle.png')
        self.image_right = load_image('resource/Climbing/right.png')
        self.image_left = load_image('resource/Climbing/left.png')
        self.image_up = load_image('resource/Climbing/back.png')
        self.image_down = load_image('resource/Climbing/front.png')
        self.image_jump = load_image('resource/Climbing/climb.png')
        self.image_fall = load_image('resource/Climbing/fall.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.font = load_font('ENCR10B.TTF', 50)
        self.font2 = load_font('ENCR10B.TTF', 30)
        self.collision_timer = 0.0  # 충돌 후 경과 시간
        self.collision_duration = 1.0  # 충돌이 무시될 시간 (초)
        self.current_height_percent = 0

    def update(self):
        if get_time() - climbing_mode.wait_time > 4 and get_time() - climbing_mode.wait_time < 64:
            if  climbing_mode.climb_time > 0:
                climbing_mode.climb_time -= game_framework.frame_time

        if self.collision_timer > 0:
            self.collision_timer -= game_framework.frame_time

        self.state_machine.update()


    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.font.draw(465, 565, f'{int(climbing_mode.climb_time):02d}', (255, 255, 255))
        self.state_machine.draw()
        # draw_rectangle(*self.get_bb()) #튜플을 풀어해쳐서 각각 인자로 전달
        self.current_height_percent = max(0, (self.y - 125) / (1625 - 125) * 100)

        self.font2.draw(900, 565, f'{int(self.current_height_percent):d}%', (255, 255, 255))


    def get_bb(self):
        screen_x = self.x - server.background.window_left
        screen_y = self.y - server.background.window_bottom
        return screen_x - 10, screen_y , screen_x + 20, screen_y + 35


    def handle_collision(self, group, other):
        # if group == 'hold:hero':
        #     self.state_machine.handle_event(('Hold', 0))
        if group == 'pink:hero':
            self.state_machine.handle_event(('Hold', 0))

        if group == 'green:hero':
            self.state_machine.handle_event(('Hold', 0))
        if self.collision_timer <= 0:
            if group == 'snow:hero':
                self.state_machine.handle_event(('Hold_out', 0))
            self.collision_timer = self.collision_duration


