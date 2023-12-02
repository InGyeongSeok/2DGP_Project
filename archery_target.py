from pico2d import load_image, draw_rectangle, clamp, get_time
import random

import game_framework
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

        draw_rectangle(*self.get_bb())  # 튜플을 풀어해쳐서 각각 인자로 전달

    def update(self):
        self.frame = self.frame + 100 *game_framework.frame_time

    def get_bb(self):
        return self.x - 20, self.y - 30, self.x + 20, self.y + 30

    def handle_collision(self, group, other):

        if group == 's_score:hero' and other.flag == 1:
            game_world.remove_object(self)
            archery_mode.archery_score += 50
            # print(archery_mode.archery_score)
            # print("s_score")
        elif group == 's_score:ai'and other.flag == 0:
            game_world.remove_object(self)
            archery_mode.ai_score += 50
            # print(archery_mode.archery_score)
            # print("s_score")

        pass


class Target_100:
    image = None

    def __init__(self):
        if Target_100.image == None:
            Target_100.image = load_image('resource/Archery/100.png')

        self.x, self.y = random.randint(100, 900), random.randint(350, 500)
        self.dirx = random.choice([-1, 1])

    def draw(self):

        self.image.clip_draw(2, 0, 20, 30, self.x , self.y, 70, 90)
        draw_rectangle(*self.get_bb())  # 튜플을 풀어해쳐서 각각 인자로 전달
    def update(self):
        # self.y += self.velocity
        # self.y = 200
        # self.frame = 30
        if get_time() - archery_mode.wait_time > 4 and get_time() - archery_mode.wait_time <64:
            self.x = clamp(25, self.x, 1000-25)
            self.x += self.dirx * 50 *game_framework.frame_time

        if self.x > 975:
            self.dirx = -1
        elif self.x <25:
            self.dirx = 1

    def get_bb(self):
        return self.x - 30, self.y - 45, self.x + 30, self.y + 45

    def handle_collision(self, group, other):

        if group == 'b_score:ai' and other.flag == 0:
            game_world.remove_object(self)
            archery_mode.ai_score += 100
            # print(archery_mode.archery_score)
            # print("b_score")
        elif group == 'b_score:hero' and other.flag == 1:
            game_world.remove_object(self)
            archery_mode.archery_score += 100
            # print(archery_mode.archery_score)
            # print("b_score")
        pass


# class Target_bomb:
#     image = None
#     bomb_image = None
#     bomb_image1 = None
#     bomb_image2 = None
#     bomb_image3 = None
#     bomb_image4 = None
#     bomb_image5 = None
#     def __init__(self):
#         if Target_bomb.image == None:
#             Target_bomb.image = load_image('resource/Archery/bomb_boat.png')
#         if Target_bomb.bomb_image == None:
#             Target_bomb.bomb_image = load_image('resource/Archery/bomb0.png')
#             Target_bomb.bomb_image1 = load_image('resource/Archery/bomb1.png')
#             Target_bomb.bomb_image2 = load_image('resource/Archery/bomb2.png')
#             Target_bomb.bomb_image3 = load_image('resource/Archery/bomb3.png')
#             Target_bomb.bomb_image4 = load_image('resource/Archery/bomb4.png')
#             Target_bomb.bomb_image5 = load_image('resource/Archery/bomb5.png')
#
#         self.x, self.y = random.randint(100, 900), random.randint(350,500 )
#         self.frame = 0
#         self.sizex = 150
#         self.sizey = 150
#         self.flag = 0
#         self.dirx = random.choice([-1, 1])
#     def draw(self):
#
#         if self.flag > 0:
#             if self.flag < 5:
#                 self.bomb_image.clip_draw(0, 0, 38, 36, self.x, self.y, self.sizex, self.sizey)
#             elif self.flag < 20:
#                 self.bomb_image1.clip_draw(0, 0, 62, 62, self.x, self.y, self.sizex, self.sizey)
#             elif self.flag < 30:
#                 self.bomb_image2.clip_draw(0, 0, 65, 62, self.x, self.y, self.sizex, self.sizey)
#             elif self.flag < 40:
#                 self.bomb_image3.clip_draw(0, 0, 62, 57, self.x, self.y, self.sizex, self.sizey)
#             elif self.flag < 50:
#                 self.bomb_image4.clip_draw(0, 0, 63, 61, self.x, self.y, self.sizex, self.sizey)
#             elif self.flag < 60:
#                 self.bomb_image5.clip_draw(0, 0, 55, 59, self.x, self.y, self.sizex, self.sizey)
#
#         elif self.frame < 100:
#             self.image.clip_draw(30, 0, 20, 30, self.x , self.y , 60, 75)
#         else:
#             self.image.clip_draw(60, 0, 20, 30, self.x , self.y,60, 75)
#         draw_rectangle(*self.get_bb())  # 튜플을 풀어해쳐서 각각 인자로 전달
#
#     def update(self):
#         if self.flag == 0:
#             self.x = clamp(25, self.x, 1000 - 25)
#             self.x += self.dirx * 50 *game_framework.frame_time
#             if self.x > 975:
#                 self.dirx = -1
#             elif self.x < 25:
#                 self.dirx = 1
#
#             self.frame = (self.frame +200 *game_framework.frame_time) % 200
#         if self.flag > 0:
#             self.flag += 0.5
#         if self.flag == 80:
#             game_world.remove_object(self)
#
#
#     def get_bb(self):
#         return self.x - 25, self.y - 40, self.x + 25, self.y + 30
#
#     def handle_collision(self, group, other):
#
#         if group == 'bomb:arrow':
#             self.flag = 1
#             # print(archery_mode.archery_score)
#             # print("bomb")
#
#             pass