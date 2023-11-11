from pico2d import load_image, get_time


class Gametimer:
    def __init__(self, set_time = 0):
        self.wait_time = get_time()
        self.time = set_time
        self.image1 = load_image('resource/1.png')
        self.image2 = load_image('resource/2.png')
        self.image3 = load_image('resource/3.png')
        self.imagego = load_image('resource/go.png')
        self.imagetime = load_image('resource/time.png')

    def draw(self):
        if get_time() - self.wait_time < 1:
            self.image3.clip_draw(0, 0, 140, 175, 500, 300)
        elif get_time() - self.wait_time < 2:
            self.image2.clip_draw(0, 0, 125, 175, 500, 300)
        elif get_time() - self.wait_time < 3:
            self.image1.clip_draw(0, 0, 125, 180, 500, 300)
        elif get_time() - self.wait_time < 4:
            self.imagego.clip_draw(0, 0, 552, 336, 500, 300)
        elif get_time() - self.wait_time > self.time:
            self.imagetime.clip_draw(0, 0, 1000, 600, 500, 300, 800, 500)

    def update(self):
        # if get_time() - self.wait_time > 90:
        #     print("Timeout!!")
        pass