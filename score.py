from pico2d import load_image, get_time, load_font



class Score:
    def __init__(self, flag = 0, hero_score = 0, ai_score = 0):

        self.image_background = load_image('resource/score.png')
        self.image_low = load_image('resource/score1.png')
        self.image_middle = load_image('resource/score2.png')
        self.image_high = load_image('resource/score3.png')
        self.font = load_font('ENCR10B.TTF', 120)
        self.image_archery = load_image('resource/archery_icon.png')
        self.image_climb = load_image('resource/climb_icon.png')
        self.image_pingpong = load_image('resource/pingpong_icon.png')
        self.flag = flag

        self.hero_score = hero_score
        self.ai_score = ai_score

        self.score = hero_score

    def draw(self):
        self.image_background.clip_draw(0, 0, 1000, 600, 500, 300)
        if self.flag == 1:
            if self.hero_score > self.ai_score:
                self.score = self.ai_score + 1000

            if self.score <= 100:
                self.image_background.clip_draw(0, 0, 1000, 600, 500, 300)
                self.font.draw(460, 400, f'{int(self.score):d}', (255, 255, 255))


            elif self.score > 100 and self.score <= 500:
                self.image_low.clip_draw(0, 0, 1000, 600, 500, 300)
                self.font.draw(450, 400, f'{int(self.score):d}', (255, 255, 255))


            elif self.score > 500 and self.score < 1000:
                self.image_middle.clip_draw(0, 0, 1000, 600, 500, 300)
                self.font.draw(450, 400, f'{int(self.score):d}', (255, 255, 255))

            else:
                self.image_high.clip_draw(0, 0, 1000, 600, 500, 300)
                self.font.draw(350, 400, f'{int(self.score):d}', (255, 255, 255))

            self.image_archery.clip_draw(0, 0, 1000, 600, 500, 300)

        if self.flag >= 2:

            self.image_archery.clip_draw(0, 0, 1000, 600, 500, 300)
            self.image_climb.clip_draw(0, 0, 1000, 600, 500, 300)
        if self.flag >= 3:
            self.image_archery.clip_draw(0, 0, 1000, 600, 500, 300)
            self.image_climb.clip_draw(0, 0, 1000, 600, 500, 300)
            self.image_pingpong.clip_draw(0, 0, 1000, 600, 500, 300)





    def update(self):
        print(self.score)
        # if get_time() - self.wait_time > 90:
        #     print("Timeout!!")
        pass