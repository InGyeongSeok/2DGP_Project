import math
import random
import time
from pico2d import load_image, draw_rectangle, get_time

import game_framework
import game_world
import pingpong_mode


class Ball:
    image = None

    def __init__(self, x=0, y=0):
        if Ball.image is None:
            Ball.image = load_image('resource/Pingpong/ball2.png')
        self.index = 0
        self.x, self.y = pingpong_mode.pingpong_ai.x - 100, pingpong_mode.pingpong_ai.y
        self.target_x, self.target_y = -50, pingpong_mode.pingpong_cat.y
        self.inity =  self.target_y - self.y
        self.sizex = 30
        self.sizey = 30
        self.flag = -1
        self.divisions = 100  # 싸이클로이드를 몇 등분으로 나눌지 결정
        self.cycloid_coordinates = self.calculate_cycloid_coordinates()
        self.updates_per_index_increment = 10
        self.update_count = 0
        self.ignore_collision_time = 0
        self.ignore_duration = 1.0  # 1초 동안 충돌 무시
        self.still_time = 0
        self.move_time = 0
        self.testx, self.testy = 0,0
        self.enter = 1
        self.speed = 1




    def draw(self):
        if get_time() - pingpong_mode.wait_time > 4 and get_time() - pingpong_mode.wait_time < 64:
            self.image.clip_draw(0, 0, 8, 8, self.x, self.y, self.sizex, self.sizey)
            # draw_rectangle(*self.get_bb())  # 튜플을 풀어해쳐서 각각 인자로 전달

    def update(self):
        # print(self.speed)
        # 10번의 update가 발생할 때마다 index를 1씩 증가
        if get_time() - pingpong_mode.wait_time > 4 and get_time() - pingpong_mode.wait_time < 64:

            if self.x < 0 or self.x > 1000:  # to_do 테이블 범위 y 넘어가면 새로 생성!
                # 새로운 공 생성 로직 추가
                self.speed = 1
                if self.x < 0:
                    pingpong_mode.ai_score += 10
                else:
                    pingpong_mode.hero_score += 10

                self.flag = -1
                # print("새로운 공 생성")
                self.x, self.y = pingpong_mode.pingpong_ai.x - 100, pingpong_mode.pingpong_ai.y
                self.target_x, self.target_y = pingpong_mode.pingpong_cat.x, pingpong_mode.pingpong_cat.y - 50
                self.inity = self.target_y - self.y
                self.cycloid_coordinates = self.calculate_cycloid_coordinates()
                self.index = 0
                self.enter = 1

            if self.flag == 1:
                self.update_count +=  200 * game_framework.frame_time
                if self.update_count >= self.updates_per_index_increment:
                    self.index += 1
                    self.update_count = 0  # 카운터 초기화

                    self.index = self.index + int(self.speed)


                # 현재 index에 해당하는 싸이클로이드 좌표와 목표 좌표로 선형 보간
                if self.index < self.divisions:
                    t = self.index / self.divisions
                    cycloid_x, cycloid_y = self.cycloid_coordinates[self.index]
                    self.testx = cycloid_x
                    self.testy = cycloid_y + self.inity // 100 * self.index

                    self.x, self.y = self.testx, self.testy

                if self.index >= self.divisions:
                    self.x, self.y = self.x, self.y
                    self.target_x, self.target_y = 1100, 300
                    self.inity = self.target_y - self.y
                    self.cycloid_coordinates = self.calculate_cycloid_coordinates()
                    self.index = 0

            elif self.flag == -1:
                self.update_count += 200 * game_framework.frame_time
                if self.update_count >= self.updates_per_index_increment:
                    self.index += 1
                    self.update_count = 0  # 카운터 초기화

                    self.index = self.index + int(self.speed)

                # 현재 index에 해당하는 싸이클로이드 좌표와 목표 좌표로 선형 보간
                if self.index < self.divisions:
                    t = self.index / self.divisions
                    cycloid_x, cycloid_y = self.cycloid_coordinates[self.index]
                    self.testx = cycloid_x
                    self.testy = cycloid_y + self.inity // 100 * self.index

                    self.x, self.y = self.testx, self.testy
                if self.index >= self.divisions:
                    self.x, self.y = self.x, self.y
                    self.target_x, self.target_y = -100, 300
                    self.inity = self.target_y - self.y
                    self.cycloid_coordinates = self.calculate_cycloid_coordinates()
                    self.index = 0

            elif pingpong_mode.pingpong_cat.flag == 1:
                self.update_count += 1
                if self.update_count >= self.updates_per_index_increment:
                    self.index += 1
                    self.update_count = 0  # 카운터 초기화

                    self.index = self.index + int(self.speed)

                # 현재 index에 해당하는 싸이클로이드 좌표와 목표 좌표로 선형 보간
                if self.index < self.divisions:
                    t = self.index / self.divisions
                    cycloid_x, cycloid_y = self.cycloid_coordinates[self.index]
                    self.testx = cycloid_x
                    self.testy = cycloid_y + self.inity // 100 * self.index

                    self.x, self.y = self.testx, self.testy

                if self.index == self.divisions:
                    self.x, self.y = self.x, self.y
                    self.target_x, self.target_y = 1100, 300
                    self.inity = self.target_y - self.y
                    self.cycloid_coordinates = self.calculate_cycloid_coordinates()
                    self.index = 0

    def cycloid(self, t):
        if self.flag == 1 :
            r = 55  # 싸이클로이드 반지름
            x = r * (t - math.sin(t)) + self.x
            y = r * ( - math.cos(t)) + self.y
            return x, y
        elif self.flag == -1:
            r =55  # 싸이클로이드 반지름
            x = -r * (t - math.sin(t)) + self.x
            y = r * (1 - math.cos(t)) + self.y
            return x, y

    def calculate_cycloid_coordinates(self):
        # 싸이클로이드를 미리 계산하여 배열에 저장
        coordinates = []
        for i in range(self.divisions):
            t = i / self.divisions * 10 + 2
            coordinates.append(self.cycloid(t))
        return coordinates

    def get_bb(self):
        return self.x - 10, self.y - 15, self.x + 10, self.y + 15

    def handle_collision(self, group, other):
        current_time = time.time()

        # 충돌 무시 중이라면 무시
        if current_time - self.ignore_collision_time < self.ignore_duration:
            return
        if group == 'hero:ball':
            self.flag = 1
            self.speed = self.speed + 20 * game_framework.frame_time

            self.target_x, self.target_y = pingpong_mode.pingpong_ai.x - 100, pingpong_mode.pingpong_ai.y
            self.inity = self.target_y - self.y
            self.cycloid_coordinates = self.calculate_cycloid_coordinates()
            self.index = 0
            pingpong_mode.pingpong_cat.smash += 1
        elif group == 'ai:ball':
            if get_time() - pingpong_mode.wait_time > 4 and get_time() - pingpong_mode.wait_time < 64:
                if pingpong_mode.pingpong_cat.flag == 0:
                    self.flag = -1
                    self.target_x, self.target_y = pingpong_mode.pingpong_cat.x, pingpong_mode.pingpong_cat.y - 50
                    self.inity = self.target_y - self.y
                    self.cycloid_coordinates = self.calculate_cycloid_coordinates()
                    self.index = 0
                    self.speed = self.speed + 20 * game_framework.frame_time

        self.ignore_collision_time = current_time  # 충돌 무시 시작 시간 기록
        self.still_time = current_time  # 움직임 기록 시간 초기화

