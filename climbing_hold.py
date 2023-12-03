import random

from pico2d import load_image, draw_rectangle, get_time

import climbing_mode
import game_world
import server

class Hold_pink:
    image = None

    def __init__(self, x= 0, y= 0):
        if Hold_pink.image == None:
            Hold_pink.image = load_image('resource/Climbing/hold.png')

        self.x = x
        self.y = y
        if self.x ==0 and self.y == 0:
            self.x ,self.y= random.randint(100, 900), random.randint(200, 1500)

        self.sizex = 45
        self.sizey = 45

    def draw(self):
        screen_x = self.x - server.background.window_left
        screen_y = self.y - server.background.window_bottom
        self.image.clip_draw(0, 0, 13, 13, screen_x, screen_y, self.sizex, self.sizey)

        draw_rectangle(*self.get_bb())  # 튜플을 풀어해쳐서 각각 인자로 전달

    def update(self):
        pass

    def get_bb(self):
        # return self.x - 20, self.y -25, self.x + 20, self.y + 25
        screen_x = self.x - server.background.window_left
        screen_y = self.y - server.background.window_bottom
        return screen_x - 10, screen_y -20, screen_x + 10, screen_y +10
    def handle_collision(self, group, other):
        # print("hold_pink!!")
        global holdx, holdy
        holdx = self.x
        holdy = self.y

        pass


class Hold_green:
    image = None

    def __init__(self, x= 0, y= 0):
        if Hold_green.image == None:
            Hold_green.image = load_image('resource/Climbing/hold.png')

        self.x = x
        self.y = y
        if self.x == 0 and self.y == 0:
            self.x ,  self.y= random.randint(100, 700), random.randint(500, 1300)

        self.sizex = 45
        self.sizey = 45
        self.collide_time = 0

    def draw(self):
        screen_x = self.x - server.background.window_left
        screen_y = self.y - server.background.window_bottom
        self.image.clip_draw(0, 15, 13, 13, screen_x, screen_y, self.sizex, self.sizey)

        draw_rectangle(*self.get_bb())  # 튜플을 풀어해쳐서 각각 인자로 전달

    def update(self):
        pass

    def get_bb(self):
        # return self.x - 20, self.y -25, self.x + 20, self.y + 25
        screen_x = self.x - server.background.window_left
        screen_y = self.y - server.background.window_bottom
        return screen_x - 10, screen_y -20, screen_x + 10, screen_y + 10
    def handle_collision(self, group, other):
        # print("hold_green!!")
        if get_time() - climbing_mode.wait_time > 4 and get_time() - climbing_mode.wait_time < 34:
            if group == 'green:hero':
                if self.collide_time == 0:
                    self.collide_time = get_time()
                else:
                    if get_time() - self.collide_time > 0.8:
                        game_world.remove_object(self)
                        self.collide_time = 0
                global holdx, holdy
                holdx = self.x
                holdy = self.y
        pass