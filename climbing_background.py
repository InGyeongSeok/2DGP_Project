from pico2d import load_image


class Climbing_background:
    def __init__(self):
        self.image= load_image('resource/Climbing/background.png')
        self.frame = 0

    def draw(self):
        self.image.clip_draw(0, 0, 435, 1000, 500, 300, 1000 , 1000)

    def update(self):
        pass
