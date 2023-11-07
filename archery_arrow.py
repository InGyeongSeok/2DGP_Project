from pico2d import load_image, draw_rectangle

import game_world


class Arrow:
    image_green = None
    image_red = None
    def __init__(self, x = 400, y = 300):
        if Arrow.image_green == None:
            Arrow.image_green = load_image('resource/Archery/arrow.png')
            Arrow.image_red = load_image('resource/Archery/arrow.png')

        self.x, self.y = x, y

    def draw(self):
        self.image_green.clip_draw(0, 0, 15, 20, self.x + 5, self.y, 30, 30)
        # self.image_red.clip_draw(19, 0, 15, 20, self.x + 5, self.y, 30, 30)
        # draw_rectangle(*self.get_bb())  # 튜플을 풀어해쳐서 각각 인자로 전달

    def update(self):
        self.y += 2
        # self.y = 200

        if self.y > 500:
            game_world.remove_object(self)


    def get_bb(self):
        return self.x - 8, self.y - 10, self.x + 8, self.y + 10

    def handle_collision(self, group, other):
        if group == 's_score:arrow':
            game_world.remove_object(self)
        if group == 'b_score:arrow':
            game_world.remove_object(self)