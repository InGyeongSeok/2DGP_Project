from pico2d import load_image
import random
import game_world

class Target_50:
    image = None

    def __init__(self):
        if Target_50.image == None:
            Target_50.image = load_image('resource/Archery/50.png')

        self.x, self.y = random.randint(100, 900), random.randint(200, 300)
        self.frame = 0

    def draw(self):
        if self.frame < 15:
            self.image.clip_draw(1, 0, 7, 17, self.x , self.y, 40, 40)

        elif self.frame < 30:
            self.image.clip_draw(19, 0, 7, 20, self.x, self.y, 40, 40)

        elif self.frame < 45:
            self.image.clip_draw(36, 0, 7, 20, self.x, self.y, 40, 40)

        elif self.frame < 60:
            self.image.clip_draw(50, 0, 13, 20, self.x, self.y, 40, 40)

        elif self.frame < 75:
            self.image.clip_draw(65, 0, 17, 20, self.x, self.y, 40, 40)

        elif self.frame >= 75:
            self.image.clip_draw(83, 0, 17, 20, self.x, self.y, 40, 40)

    def update(self):
        self.frame = self.frame + 1

        #충돌처리 해야함!!

class Target_100:
    image = None

    def __init__(self):
        if Target_100.image == None:
            Target_100.image = load_image('resource/Archery/100.png')

        self.x, self.y = random.randint(100, 900), random.randint(300, 500)

        self.frame = 0

    def draw(self):

        self.image.clip_draw(2, 0, 20, 30, self.x , self.y, 70, 90)

    def update(self):
        # self.y += self.velocity
        # self.y = 200
        # self.frame = 30
        self.frame = (self.frame + 1)

        # if self.y > 500:
        #     game_world.remove_object(self)