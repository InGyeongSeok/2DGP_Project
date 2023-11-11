from pico2d import load_image


class Pingpong_background:
    def __init__(self):
        self.image= load_image('resource/PingPong/background.png')

    def draw(self):
        self.image.clip_draw(0, 0, 1000, 600, 500, 300)

    def update(self):
        pass