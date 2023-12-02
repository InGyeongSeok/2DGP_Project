from pico2d import load_image

import pingpong_mode


class Pingpong_background:
    def __init__(self):
        self.image= load_image('resource/PingPong/background.png')
        self.smash = load_image('resource/PingPong/0.png')
        self.smash1 = load_image('resource/PingPong/1.png')
        self.smash2= load_image('resource/PingPong/2.png')
        self.smash3 = load_image('resource/PingPong/3.png')
        self.smash4 = load_image('resource/PingPong/4.png')
        self.smash5 = load_image('resource/PingPong/5.png')


    def draw(self):
        self.image.clip_draw(0, 0, 1000, 600, 500, 300)

        if pingpong_mode.pingpong_cat.smash == 0:
            self.smash.clip_draw(0, 0, 1000, 600, 500, 300)
        elif pingpong_mode.pingpong_cat.smash == 1:
            self.smash1.clip_draw(0, 0, 1000, 600, 500, 300)
        elif pingpong_mode.pingpong_cat.smash == 2:
            self.smash2.clip_draw(0, 0, 1000, 600, 500, 300)
        elif pingpong_mode.pingpong_cat.smash == 3:
            self.smash3.clip_draw(0, 0, 1000, 600, 500, 300)
        elif pingpong_mode.pingpong_cat.smash == 4:
            self.smash4.clip_draw(0, 0, 1000, 600, 500, 300)
        elif pingpong_mode.pingpong_cat.smash == 5:
            self.smash5.clip_draw(0, 0, 1000, 600, 500, 300)

    def update(self):
        pass


