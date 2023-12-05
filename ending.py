from pico2d import load_image, load_music, load_font

import game_framework


class Ending:
    def __init__(self):
        self.image = load_image('resource/back.png')
        self.bgm = load_music('resource/ending.mp3')
        self.bgm.set_volume(500)
        self.bgm.play()
        self.images = [load_image('resource/end/%d.jpg' % i) for i in range(1, 36 + 1)]
        self.frame = 0
        self.font = load_font('ENCR10B.TTF', 50)


    def draw(self):
        self.images[int(self.frame)].clip_draw(0, 0, 1000, 600, 500, 300)

        if int(self.frame) > 30:
            self.font.draw(430,90, f'{"The End"}', (255, 205,255))

        pass

    def update(self):
        if int(self.frame) < 35:
            self.frame = self.frame + 5 * game_framework.frame_time
        pass

