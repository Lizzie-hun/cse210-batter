from game import constants
from game.action import Action
from game.point import Point

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction()
        paddle = cast["paddle"][0] # there's only one in the cast

        position = paddle.get_position()
        velocity = paddle.get_velocity()

        x = position.get_x()
        y = position.get_y()
        dx = velocity.get_x()
        dy = velocity.get_y()

        x = (x + dx)
        y = (y + dy)

        right_x = paddle.get_right_edge()


        if right_x > constants.MAX_X:
            x = constants.MAX_X - 100
    
        elif x < 0:
            x = 0
        

        position = Point(x, y)
        paddle.set_position(position)

        paddle.set_velocity(direction.scale(constants.PADDLE_SPEED))

    def remove_actor(self,cast):
        cast = cast["brick"]
        #brick.pop
