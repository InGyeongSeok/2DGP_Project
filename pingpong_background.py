from pico2d import load_image, load_music, get_time, load_font

import game_framework
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
        self.start = load_music('resource/start3.mp3')
        self.start.set_volume(60)
        self.start.play()
        self.bgm = load_music('resource/pingpong.mp3')
        self.bgm.set_volume(60)
        self.bgm_started = False
        self.font = load_font('ENCR10B.TTF', 50)
        self.font2 = load_font('ENCR10B.TTF', 35)
        self.font3 = load_font('ENCR10B.TTF', 35)

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
        elif pingpong_mode.pingpong_cat.smash >= 5:
            self.smash5.clip_draw(0, 0, 1000, 600, 500, 300)

        self.font.draw(455, 565, f'{int(pingpong_mode.pingpong_time):02d}', (255, 255, 255))
        self.font2.draw(305, 565, f'{pingpong_mode.hero_score:02d}', (0, 255, 0))
        self.font3.draw(605, 565, f'{pingpong_mode.ai_score:02d}', (255, 0, 0))
    def update(self):
        if get_time() - pingpong_mode.wait_time > 4 and not self.bgm_started:
            self.bgm_started = True
            self.bgm.repeat_play()

        if get_time() - pingpong_mode.wait_time > 4 and get_time() - pingpong_mode.wait_time < 64:
            if  pingpong_mode.pingpong_time > 0:
                pingpong_mode.pingpong_time -= game_framework.frame_time
        pass


