from game.actor import Actor
from game.point import Point
from game import constants

class Paddle(Actor):
    def __init__(self):
        super().__init__()

        x = int(constants.PADDLE_X)
        y = int(constants.PADDLE_Y)
        position = Point(x, y)

        
        self.set_image(constants.IMAGE_PADDLE)
        self.set_height(constants.PADDLE_HEIGHT)
        self.set_width(constants.PADDLE_WIDTH)
        self.set_position(position)
        #self.set_velocity()
