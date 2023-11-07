from pico2d import load_image


class Archery_background:
    def __init__(self):
        self.image_sand = load_image('resource/Archery/sand.png')
        self.image_sunset = load_image('resource/Archery/sunset.png')
        self.image_wave = load_image('resource/Archery/wave.png')
        self.image_ocean = load_image('resource/Archery/ocean.png')
        self.frame = 0

    def draw(self):
        for i in range(15):

            for j in range(2): #맨 아래 모래
                self.image_sand.clip_draw(0, 0, 48, 48, 24 + 72 * i, 24 + 72 * j, 100, 100)

        for i in range(20): #맨 위 배
            self.image_sunset.clip_draw(0, 0, 48, 48, 48 + 72 * i, 550, 100, 100)


        for i in range(20):
            for j in range(5):
                if self.frame < 120:
                    self.image_ocean.clip_draw(0, 0, 48, 48, 24 + 72 * i, 160 + 72 * j, 100, 100)
                else:
                    self.image_ocean.clip_draw(61, 0, 48, 48, 24 + 72 * i, 160 + 72 * j, 100, 100)

        for i in range(22):
                if self.frame <120:
                    self.image_wave.clip_draw(0, 0, 16, 17, 24 + 48 * i, 100, 50, 50)
                else:
                    self.image_wave.clip_draw(19, 0, 16, 17, 24 + 48 * i, 100, 50, 50)

    def update(self):
        self.frame = (self.frame + 1) % 240
        pass
