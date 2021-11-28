import random
from game.move_actors_action import MoveActorsAction
from game import constants
from game.action import Action
from game.audio_service import AudioService

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
        self._move_actors_action = MoveActorsAction()

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        audio_service = AudioService()

        bricks = cast["brick"]
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0]
        
        if self._physics_service.is_collision(ball,paddle):
                self._move_actors_action._hit_block(ball)
                
        for brick in bricks:
            
            if self._physics_service.is_collision(ball,brick):
                self._move_actors_action._hit_block(ball)
                audio_service.play_sound(constants.SOUND_BOUNCE)
                bricks.remove(brick)
           