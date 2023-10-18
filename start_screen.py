from pico2d import load_image

class Start_back:
    def __init__(self):
        self.image = load_image('resource/background.png')

    def draw(self):
        self.image.clip_draw(0, 0, 500, 250, 400, 300,800, 600)


    def update(self):
        pass

class Start_screen:
    def __init__(self):
        self.image = load_image('resource/start.png')

    def draw(self):
        self.image.clip_draw(0, 5, 250, 100, 400, 300, 400, 300)


    def update(self):
        pass
