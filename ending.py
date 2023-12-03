from pico2d import load_image, load_music

import game_framework


class Ending:
    def __init__(self):
        self.image = load_image('resource/back.png')
        self.bgm = load_music('resource/ending.mp3')
        self.bgm.set_volume(500)
        self.bgm.repeat_play()

    def draw(self):
        self.image.clip_draw(0, 0, 1000, 600, 500, 300)


    def update(self):
        pass

class Start_screen:
    def __init__(self):
        self.image = load_image('resource/start.png')

    def draw(self):
        self.image.clip_draw(0, 0, 500, 300, 500, 300, 800, 450)


    def update(self):
        pass

class Start_play:
    def __init__(self):
        self.frame = 0
        self.image = load_image('resource/play.png')

    def draw(self):
        self.image.clip_draw(80 * int(self.frame // 20), 0, 90, 90, 500 + -20 * int(self.frame // 20), 260, 200, 200)

    def update(self):
        self.frame = (self.frame + 50 *game_framework.frame_time) % 40
        pass