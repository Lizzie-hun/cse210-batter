from game.actor import Actor
from game.point import Point
from game import constants

class Ball(Actor):
    def __init__(self):
        super().__init__()

        x = int(constants.BALL_X)
        y = int(constants.BALL_Y)
        position = Point(x, y)

        dx = constants.BALL_DX
        dy = constants.BALL_DY
        velocity = Point(dx, dy)
        
        self.set_image(constants.IMAGE_BALL)
        self.set_position(position)
        self.set_velocity(velocity)
        self.set_width(constants.BALL_WIDTH)
        self.set_height(constants.BALL_HEIGHT)
        
