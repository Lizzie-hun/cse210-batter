from game.actor import Actor
from game.point import Point
from game import constants

class Brick(Actor):
    def __init__(self):
        super().__init__()
        
        self.bricks = []


        self.set_image(constants.IMAGE_BRICK)
        self.set_width(constants.BRICK_WIDTH)
        self.set_height(constants.BRICK_HEIGHT)

    def create_bricks(self):

        add_x = 0
        add_y = 0
        x = 0
        y = 0

        for n in range(constants.BRICK_ROWS * constants.BRICK_COLUMNS):
            if x == 0:
                x = constants.BRICK_SPACE * 2
                y = constants.BRICK_SPACE * 2
            elif x < constants.MAX_X:
                if x > constants.MAX_X - (constants.BRICK_WIDTH + constants.BRICK_SPACE * 2):
                    x = constants.BRICK_SPACE * 2
                    y = y + constants.BRICK_HEIGHT + constants.BRICK_SPACE
                else:
                    x = x + constants.BRICK_WIDTH + constants.BRICK_SPACE

            position = Point(x, y)

            brick = Brick()
            brick.set_position(position)
            self.bricks.append(brick)


            
        