from pico2d import load_image

class Start_back:
    def __init__(self):
        self.image = load_image('resource/back.png')

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
        self.image.clip_draw(80 * (self.frame // 120), 0, 90, 90, 500 + -20 * (self.frame // 120), 260, 200, 200)

    def update(self):
        self.frame = (self.frame + 1) % 240
        pass