from pico2d import load_image, draw_rectangle

import game_framework
import game_world


class Arrow:
    image_green = None
    image_red = None
    def __init__(self, x = 400, y = 300, flag = 1):
        if Arrow.image_green == None:
            Arrow.image_green = load_image('resource/Archery/arrow.png')
            Arrow.image_red = load_image('resource/Archery/arrow.png')

        self.x, self.y = x, y
        self.flag = flag
    def draw(self):
        if self.flag == 1:
            self.image_green.clip_draw(0, 0, 15, 20, self.x + 5, self.y, 45, 45)
        else:
            self.image_red.clip_draw(18, 0, 15, 20, self.x + 5, self.y, 45, 45)

        # draw_rectangle(*self.get_bb())  # 튜플을 풀어해쳐서 각각 인자로 전달

    def update(self):
        self.y += 350 * game_framework.frame_time
        # self.y = 200

        if self.y > 500:
            game_world.remove_object(self)


    def get_bb(self):
        return self.x -10, self.y - 18, self.x + 10, self.y + 18

    def handle_collision(self, group, other):
        if group == 's_score:arrow':
            game_world.remove_object(self)
        if group == 'b_score:arrow':
            game_world.remove_object(self)
        pass
