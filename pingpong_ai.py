from time import time

from pico2d import *

import random
import math
import game_framework
import game_world
from behavior_tree import BehaviorTree, Action, Sequence, Condition, Selector

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10.0


class PingPong_ai:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 20)
        self.x = 800
        self.y = 500
        self.frame = 0
        self.action = 0
        self.dir = 1
        self.targetx = 0
        self.state = 'Idle'
        self.tx, self.ty = 1000, 1000
        self.build_behavior_tree()
        self.image_Run = load_image('resource/PingPong/tengu.png')
        self.target_index = 0
        self.arrow_start_time = 0
        self.arrow_duration = 3.0
        self.collide_time = 0



    def get_bb(self):
        return self.x - 150, self.y -40, self.x - 30 , self.y +40

    def update(self):
        # self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        # fill here
        self.frame = (self.frame + 0.01) % 4
        self.bt.run()

    def draw(self):
        if self.state == 'Run' :
            self.image_Run.clip_draw(int(self.frame) * 80 , 0, 80, 89, self.x , self.y, 300, 300)

            pass
        # elif self.state == 'Run':
        #     self.image_Run.clip_draw(int(self.frame) * 80 , 0, 80, 89, self.x, self.y, 300, 300)

            pass

        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def handle_collision(self, group, other):
        pass

    def distance_less_than(self, x1, y1, x2, y2, r):
        distance2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
        return distance2 < (PIXEL_PER_METER * r) ** 2

    def move_slightly_to(self, tx, ty):
        self.dir = math.atan2(ty - self.y, tx - self.x)
        self.speed = RUN_SPEED_PPS
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time

    def move_to(self, r=5):
        self.state = 'Run'
        # print(self.y)

        self.move_slightly_to(self.tx, self.ty)
        if self.distance_less_than(self.tx, self.ty, self.x, self.y, r):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING


    def set_random_location(self):
        self.tx, self.ty = 800, random.randint(0, 600),
        # print(self.ty)
        # if self.ty < 100:
        #     self.ty = self.ty * 100
        return BehaviorTree.SUCCESS

    def is_target_nearby(self, r):
        pass
        #         return BehaviorTree.SUCCESS
        # return BehaviorTree.FAIL


    def move_to_target(self, r=0.5):
        self.state = 'Run'
        self.move_slightly_to(self.targetx, 55)
        if self.distance_less_than(self.targetx,self.x,r):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING




    def build_behavior_tree(self):
        a2 = Action('Move to', self.move_to)
        a3 = Action('Set random location', self.set_random_location)

        root = SEQ_wander = Sequence('Wander', a3, a2)

        c1 = Condition('목표가 근처에 있는가?', self.is_target_nearby, 7)  # 7미터
        a4 = Action('목표한테 접근', self.move_to_target)

        SEQ_chase_boy = Sequence('목표을 추적', c1, a4)

        # root = SEL_chase_or_wander = Selector('추적 또는 배회', SEQ_chase_boy, SEQ_wander)


        self.bt = BehaviorTree(root)

    def handle_collision(self, group, other):
        if group == 'ai:ball':
            if self.collide_time == 0:
                self.collide_time = get_time()
            elif get_time() - self.collide_time > 0.8:

                self.collide_time = 0
            print("여기 들어옴?")
        pass