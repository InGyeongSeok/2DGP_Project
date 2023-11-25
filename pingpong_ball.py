import math
import random
import time
from pico2d import load_image

class Ball:
    image = None

    def __init__(self, x=0, y=0):
        if Ball.image is None:
            Ball.image = load_image('resource/Pingpong/ball2.png')

        self.x, self.y = 200, 200
        self.target_x, self.target_y = 400, 200
        self.sizex = 30
        self.sizey = 30
        self.collide_time = 0
        self.divisions = 100  # 싸이클로이드를 몇 등분으로 나눌지 결정
        self.cycloid_coordinates = self.calculate_cycloid_coordinates()

    def draw(self):
        print("DRAW")
        print(self.x)
        print(self.y)
        self.image.clip_draw(0, 0, 8, 8, self.x, self.y, self.sizex, self.sizey)

    def update(self):
        # 싸이클로이드 곡선으로 이동
        elapsed_time = time.time() - self.collide_time
        if elapsed_time < 3:
            # elapsed_time을 이용하여 배열의 인덱스 증가
            index = int(elapsed_time / 3* self.divisions)
            if index < self.divisions:
                # 현재 목표 좌표를 사용
                self.x, self.y = self.cycloid_coordinates[index]
        else:
            # 목표 지점에 도달하면 초기화
            self.collide_time = time.time()

    def cycloid(self, t):
        r = 30  # 싸이클로이드 반지름
        x = r * (t - math.sin(t)) + self.target_x
        y = r * (0.5 - math.cos(t)) + self.target_y
        return x, y

    def calculate_cycloid_coordinates(self):
        # 싸이클로이드를 미리 계산하여 배열에 저장
        coordinates = []
        for i in range(self.divisions):
            t = i / self.divisions * 10 # 10초 동안 등분
            coordinates.append(self.cycloid(t))
        return coordinates

    def get_bb(self):
        return self.x - 20, self.y - 25, self.x + 20, self.y + 25

    def calculate_cycloid_from_current(self, elapsed_time):
        # 현재 위치부터 목표 지점까지의 싸이클로이드 계산
        t = elapsed_time  # elapsed_time을 그대로 사용
        return self.cycloid(t)
