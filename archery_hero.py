# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import load_image, get_time, load_font, clamp
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT, SDLK_a

import archery_mode
import game_framework
import game_world
from archery_arrow import Arrow

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


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


# time_out = lambda e : e[0] == 'TIME_OUT'
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0   # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6

class Idle:

    @staticmethod
    def enter(archery_cat, e):
        archery_cat.frame = 0
        # archery_cat.wait_time = get_time()  # pico2d import 필요

    @staticmethod
    def exit(archery_cat, e):
        if space_down(e):
            archery_cat.fire_arrow()

    @staticmethod
    def do(archery_cat):
        pass

    @staticmethod
    def draw(archery_cat):
        archery_cat.image_Idle.clip_draw(0, 0, 20, 28, archery_cat.x, archery_cat.y+2, 70, 70)


class Run:

    @staticmethod
    def enter(archery_cat, e):
        if right_down(e) or left_up(e):  # 오른쪽으로 RUN
            archery_cat.dir, archery_cat.action = 1, 0
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN
            archery_cat.dir, archery_cat.action = -1, 1
    @staticmethod
    def exit(archery_cat, e):
        pass

    @staticmethod
    def do(archery_cat):
        archery_cat.frame = (archery_cat.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        archery_cat.x += archery_cat.dir * RUN_SPEED_PPS * game_framework.frame_time
        archery_cat.x = clamp(50, archery_cat.x, 1000-50)
        pass

    @staticmethod
    def draw(archery_cat):
            archery_cat.image_Run.clip_draw(int(archery_cat.frame) * 22, archery_cat.action * 31, 21, 25, archery_cat.x,
                                            archery_cat.y, 60, 60)



class StateMachine:
    def __init__(self, archery_cat):
        self.archery_cat = archery_cat
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, space_down: Idle},
            Run: {right_down: Run, left_down: Run, right_up: Idle, left_up: Idle}
        }

    def start(self):
        self.cur_state.enter(self.archery_cat, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.archery_cat)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.archery_cat, e)
                self.cur_state = next_state
                self.cur_state.enter(self.archery_cat, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.archery_cat)


class Archery_cat:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 20)
        self.x, self.y = 400, 55
        self.frame = 0
        self.action = 0
        self.dir = 1
        self.image_Idle = load_image('resource/Archery/Idle.png')
        self.image_Run = load_image('resource/Archery/cat.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        
    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        # self.font.draw(self.x - 10, self.y + 48, f'{archery_mode.archery_score:02d}', (255, 255, 0))

    def fire_arrow(self):
        arrow = Arrow(self.x, self.y)
        game_world.add_object(arrow, 1)
        game_world.add_collision_pair('s_score:hero', None, arrow)
        game_world.add_collision_pair('b_score:hero', None, arrow)
        # game_world.add_collision_pair('bomb:arrow', None, arrow)




