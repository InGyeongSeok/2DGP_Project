from pico2d import load_image, load_font

import archery_mode
import game_framework


class Archery_background:
    def __init__(self):
        self.image_sand = load_image('resource/Archery/sand.png')
        self.image_sunset = load_image('resource/Archery/sunset.png')
        self.image_wave = load_image('resource/Archery/wave.png')
        self.image_ocean = load_image('resource/Archery/ocean.png')
        self.image_ocean = load_image('resource/Archery/ocean.png')
        self.image_score = load_image('resource/Archery/score2.png')
        self.font = load_font('ENCR10B.TTF', 50)
        self.font2 = load_font('ENCR10B.TTF', 35)
        self.font3 = load_font('ENCR10B.TTF', 35)


        self.frame = 0

    def draw(self):

        for i in range(15):
            for j in range(2): #맨 아래 모래
                self.image_sand.clip_draw(0, 0, 48, 48, 24 + 72 * i, 24 + 72 * j, 100, 100)

        for i in range(20): #맨 위 배
            self.image_sunset.clip_draw(0, 0, 48, 48, 48 + 72 * i, 550, 100, 100)

        for i in range(20):
            for j in range(5):
                self.image_ocean.clip_draw(61 * int(self.frame //1), 0, 48, 48, 24 + 72 * i, 160 + 72 * j, 100, 100)

        for i in range(22):
            self.image_wave.clip_draw(19 * int(self.frame // 1), 0, 16, 17, 24 + 48 * i, 100, 50, 50)

        self.image_score.clip_draw(0, 0, 200, 50, 500, 555, 400, 95)
        self.font.draw(465, 565, f'{int(archery_mode.archery_time):02d}', (255, 255, 255))
        self.font2.draw(340, 555, f'{archery_mode.archery_score:02d}', (0, 255, 0))
        self.font3.draw(620, 555, f'{archery_mode.ai_score:02d}', (255, 0, 0))
    def update(self):
        global archery_time

        self.frame = (self.frame + game_framework.frame_time) % 2
        archery_mode.archery_time -= game_framework.frame_time

        pass
