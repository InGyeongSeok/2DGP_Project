from pico2d import load_image

import game_world


class Arrow:
    image_green = None
    image_red = None
    def __init__(self, x = 400, y = 300, velocity = 1):
        if Arrow.image_green == None:
            Arrow.image_green = load_image('resource/Archery/arrow.png')
            Arrow.image_red = load_image('resource/Archery/arrow.png')

        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image_green.clip_draw(0, 0, 15, 20, self.x + 5, self.y, 30, 30)
        # self.image_red.clip_draw(19, 0, 15, 20, self.x + 5, self.y, 30, 30)


    def update(self):
        self.y += self.velocity
        # self.y = 200

        if self.y > 500:
            game_world.remove_object(self)

