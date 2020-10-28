"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

File: breakout.py
Name: Elaine Yen
---------------------------
This program plays a game called
'breakout' in which players
moving the mouse to rebounce
the ball to delete bricks
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.


def main():
    """
    This program plays a Python game 'breakout'
    A ball will be bouncing around the GWindow to delete bricks.
    Players must use a paddle to rebounce the ball by moving the mouse.
    """
    graphics = BreakoutGraphics()
    graphics.set_ball_velocity()

    while True:
        # Check whether switch to start the game.
        if graphics.ball_start:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            graphics.ball.move(dx, dy)
            graphics.handle_object_collisions()
            graphics.handle_wall_collisions()
            if graphics.lives < 1 or graphics.brick_number == 0:
                break

        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
