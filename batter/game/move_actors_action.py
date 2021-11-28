import pyray
from time import sleep
from game import constants
from game.action import Action
from game.point import Point
from game.audio_service import AudioService


class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        for group in cast.values():
            for actor in group:
                if not actor.get_velocity().is_zero():
                    self._move_actor(actor)

    def _move_actor(self, actor):
        """Moves the given actor to its next position according to its 
        velocity. Will wrap the position from one side of the screen to the 
        other when it reaches the edge in either direction.
        
        Args:
            actor (Actor): The actor to move.
        """
        audio_service = AudioService()

        position = actor.get_position()
        velocity = actor.get_velocity()

        x = position.get_x()
        y = position.get_y()
        dx = velocity.get_x()
        dy = velocity.get_y()

        x = (x + dx)
        y = (y + dy)
        
        position = Point(x, y)
        actor.set_position(position)

        right_x = actor.get_right_edge()
        bottom_y = actor.get_bottom_edge()

        if right_x == constants.MAX_X:
            dx = -dx
            dy = dy
            audio_service.play_sound(constants.SOUND_BOUNCE)

        elif x == 0:
            dx = -dx
            dy = dy
            audio_service.play_sound(constants.SOUND_BOUNCE)

        if bottom_y == 0:
            dx = dx
            dy = -dy
            audio_service.play_sound(constants.SOUND_BOUNCE)
        
        velocity = Point(dx,dy)
        
        if y > constants.MAX_Y - constants.BALL_HEIGHT:
            audio_service.play_sound(constants.SOUND_OVER)
            velocity = Point(0,0)
            sleep(5)

            pyray.close_window()

        actor.set_velocity(velocity)
        

    def _hit_block(self, actor):               
        
        velocity = actor.get_velocity()

        dx = velocity.get_x()
        dy = velocity.get_y()
        
        velocity = Point(dx, -dy)
        actor.set_velocity(velocity)