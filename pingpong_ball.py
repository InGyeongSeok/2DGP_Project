import math
import random
import time
from pico2d import load_image

class Ball:
    image = None

    def __init__(self, x=0, y=0):
        if Ball.image is None:
            Ball.image = load_image('resource/Pingpong/ball2.png')
        self.index = 0
        self.x, self.y = 200, 200
        self.target_x, self.target_y = 600, 300
        self.sizex = 30
        self.sizey = 30
        self.collide_time = 0
        self.divisions = 100  # 싸이클로이드를 몇 등분으로 나눌지 결정
        self.cycloid_coordinates = self.calculate_cycloid_coordinates()
        self.updates_per_index_increment = 10
        self.update_count = 0
    def draw(self):
        print("DRAW")
        print(self.x)
        print(self.y)
        self.image.clip_draw(0, 0, 8, 8, self.x, self.y, self.sizex, self.sizey)

    def update(self):
        # 10번의 update가 발생할 때마다 index를 1씩 증가
        self.update_count += 1
        if self.update_count >= self.updates_per_index_increment:
            self.index += 1
            self.update_count = 0  # 카운터 초기화

        # 현재 index에 해당하는 싸이클로이드 좌표와 목표 좌표로 선형 보간
        if self.index < self.divisions:
            t = self.index / self.divisions
            cycloid_x, cycloid_y = self.cycloid_coordinates[self.index]
            interpolated_x = (1 - t) * self.x + t * cycloid_x
            interpolated_y = (1 - t) * self.y + t * cycloid_y
            self.x, self.y = interpolated_x, interpolated_y


    def cycloid(self, t):
        r = 45  # 싸이클로이드 반지름
        x = r * (t - math.sin(t)) + self.x
        y = r * (1 - math.cos(t)) + self.y
        return x, y

    def calculate_cycloid_coordinates(self):
        # 싸이클로이드를 미리 계산하여 배열에 저장
        coordinates = []
        for i in range(self.divisions):
            t = i / self.divisions * 10 + 2  # 10초 동안 등분
            coordinates.append(self.cycloid(t))
        return coordinates



    def get_bb(self):
        return self.x - 20, self.y - 25, self.x + 20, self.y + 25
