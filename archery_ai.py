from time import time

from pico2d import *

import random
import math
import game_framework
import game_world
from archery_arrow import Arrow
from behavior_tree import BehaviorTree, Action, Sequence, Condition, Selector
import archery_mode

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10.0


class Archery_ai:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 20)
        self.x = 400
        self.y = 55
        self.frame = 0
        self.action = 0
        self.dir = 1
        self.targetx = 0
        self.state = 'Idle'
        self.tx, self.ty = 1000, 1000
        self.build_behavior_tree()
        self.image_Run = load_image('resource/Archery/ai_run.png')
        self.target_index = 0
        self.arrow_start_time = 0
        self.arrow_duration = 3.0
    def get_bb(self):
        return self.x - 40, self.y - 35, self.x + 50, self.y + 40

    def update(self):
        # self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        # fill here
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7
        self.bt.run()

    def draw(self):
        if self.state == 'Run' and self.dir > 0:
            self.image_Run.clip_draw(int(self.frame) * 56 + 8, 66, 56, 54, self.x , self.y, 80, 80)

            pass
        elif self.state == 'Run':
            self.image_Run.clip_draw(int(self.frame) * 56 + 8, 0, 56, 54, self.x , self.y, 80, 80)

            pass

        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def handle_collision(self, group, other):
        pass

    def distance_less_than(self, x1, x2, r):
        distance2 = abs(x2 - x1)
        return distance2 < r

    def move_slightly_to(self, tx, ty):
        self.dir = tx - self.x
        self.speed = RUN_SPEED_PPS
        if self.dir > 0:
            self.x += self.speed * game_framework.frame_time
        else:
            self.x -= self.speed * game_framework.frame_time

    def move_to(self, r=0.5):  # 0.5 미터
        self.state = 'Run'
        self.move_slightly_to(self.tx, self.ty)
        if self.distance_less_than(self.tx, self.x, r):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING

    def set_random_location(self):
        self.tx, self.ty = random.randint(100, 900), 55
        # print(self.tx)
        if self.tx < 100:
            self.tx = self.tx * 100
        return BehaviorTree.SUCCESS

    def is_target_nearby(self, r):

        for i in archery_mode.target_100:
            if self.distance_less_than(self.x, i.x, r):
                self.targetx = i.x
                self.target_index = i
                return BehaviorTree.SUCCESS
        return BehaviorTree.FAIL


    def move_to_target(self, r=0.5):
        self.state = 'Run'
        self.move_slightly_to(self.targetx, 55)
        if self.distance_less_than(self.targetx,self.x,r):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING


    def arrow(self):
        arrow = Arrow(self.x, self.y, 0)
        game_world.add_object(arrow, 1)
        game_world.add_collision_pair('s_score:ai', None, arrow)
        game_world.add_collision_pair('b_score:ai', None, arrow)
        # game_world.add_collision_pair('bomb:arrow', None, arrow)
        archery_mode.target_100.remove(self.target_index)
        return BehaviorTree.FAIL


    def build_behavior_tree(self):
        a2 = Action('Move to', self.move_to)
        a3 = Action('Set random location', self.set_random_location)

        SEQ_wander = Sequence('Wander', a3, a2)

        c1 = Condition('목표가 근처에 있는가?', self.is_target_nearby, 7)  # 7미터
        a4 = Action('목표한테 접근', self.move_to_target)
        a5 = Action('화살 쏘기', self.arrow)

        SEQ_chase_boy = Sequence('목표을 추적', c1, a4, a5)

        root = SEL_chase_or_wander = Selector('추적 또는 배회', SEQ_chase_boy, SEQ_wander)


        self.bt = BehaviorTree(root)
