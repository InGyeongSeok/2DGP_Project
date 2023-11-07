from pico2d import load_image, draw_rectangle, clamp
import random
import game_world
import archery_mode

class Target_50:
    image = None

    def __init__(self):
        if Target_50.image == None:
            Target_50.image = load_image('resource/Archery/50.png')

        self.x, self.y = random.randint(100, 900), random.randint(200, 300)
        self.frame = 0
        self.sizex = 45
        self.sizey = 55

    def draw(self):
        if self.frame < 15:
            self.image.clip_draw(1, 0, 7, 17, self.x , self.y, self.sizex, self.sizey)

        elif self.frame < 30:
            self.image.clip_draw(19, 0, 7, 20, self.x, self.y, self.sizex, self.sizey)

        elif self.frame < 45:
            self.image.clip_draw(36, 0, 7, 20, self.x, self.y, self.sizex, self.sizey)

        elif self.frame < 60:
            self.image.clip_draw(50, 0, 13, 20, self.x, self.y, self.sizex, self.sizey)

        elif self.frame < 75:
            self.image.clip_draw(65, 0, 17, 20, self.x, self.y, self.sizex, self.sizey)

        elif self.frame >= 75:
            self.image.clip_draw(83, 0, 17, 20, self.x, self.y, self.sizex, self.sizey)

        # draw_rectangle(*self.get_bb())  # 튜플을 풀어해쳐서 각각 인자로 전달

    def update(self):
        self.frame = self.frame + 0.3

    def get_bb(self):
        return self.x - 20, self.y - 30, self.x + 20, self.y + 30

    def handle_collision(self, group, other):

        if group == 's_score:arrow':
            game_world.remove_object(self)
            archery_mode.archery_score += 50
            # print(archery_mode.archery_score)
            # print("s_score")

        pass


class Target_100:
    image = None

    def __init__(self):
        if Target_100.image == None:
            Target_100.image = load_image('resource/Archery/100.png')

        self.x, self.y = random.randint(100, 900), random.randint(300, 500)
        self.dirx = random.choice([-1, 1])

    def draw(self):

        self.image.clip_draw(2, 0, 20, 30, self.x , self.y, 70, 90)
        # draw_rectangle(*self.get_bb())  # 튜플을 풀어해쳐서 각각 인자로 전달
    def update(self):
        # self.y += self.velocity
        # self.y = 200
        # self.frame = 30
        self.x = clamp(25, self.x, 1000-25)
        self.x += self.dirx * 0.25

        if self.x > 975:
            self.dirx = -1
        elif self.x <25:
            self.dirx = 1

    def get_bb(self):
        return self.x - 30, self.y - 45, self.x + 30, self.y + 45

    def handle_collision(self, group, other):

        if group == 'b_score:arrow':
            game_world.remove_object(self)
            archery_mode.archery_score += 100
            # print(archery_mode.archery_score)
            # print("b_score")
        pass