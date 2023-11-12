from pico2d import load_image, get_time, draw_rectangle

import game_world
import server


class Climbing_snow:
    image = None
    def __init__(self, x = 600 , y = 500):
        self.wait_time = get_time()
        if Climbing_snow.image == None:
            self.image= load_image('resource/Climbing/snow.png')
        self.x = x
        self.y = y

    def draw(self):
        # self.image.clip_draw(0, 0, 24, 80, self.x, self.y, 120,400)
        screen_x = self.x - server.background.window_left
        screen_y = self.y - server.background.window_bottom
        self.image.clip_draw(0, 0, 24, 80, screen_x, screen_y, 120,400)
        # draw_rectangle(*self.get_bb())  # 튜플을 풀어해쳐서 각각 인자로 전달

    def update(self):
        if get_time() - self.wait_time > 3:
            self.y -= 0.5
        if self.y < -50:
            game_world.remove_object(self)
        pass

    def get_bb(self):
        # return self.x - 20, self.y -25, self.x + 20, self.y + 25
        screen_x = self.x - server.background.window_left
        screen_y = self.y - server.background.window_bottom
        return screen_x - 50, screen_y + 100, screen_x + 50, screen_y + 200


    def handle_collision(self, group, other):
        # print("snow_collision!!")
        if group == 'snow:hero':
            # print("snow_collision!!")
            pass