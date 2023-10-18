from pico2d import load_image

class Archery_background:
    def __init__(self):
        self.image = load_image('resource/background.png')

    def draw(self):
        self.image.clip_draw(0, 0, 500, 250, 400, 300,800, 600)


    def update(self):
        pass

