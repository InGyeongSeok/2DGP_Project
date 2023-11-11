from pico2d import load_image
from pico2d import *
import server

class Climbing_background:
    def __init__(self):
        self.image= load_image('resource/Climbing/3.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h


    def draw(self):
        self.image.clip_draw_to_origin(
            self.window_left, self.window_bottom,
            self.canvas_width, self.canvas_height,
            0, 0)

    def update(self):
        self.window_left = clamp(0,
                                 int(server.climbing_cat.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width - 50)
        self.window_bottom = clamp(0,
                                   int(server.climbing_cat.y) - self.canvas_height // 2,
                                   self.h - self.canvas_height - 50)
        pass
