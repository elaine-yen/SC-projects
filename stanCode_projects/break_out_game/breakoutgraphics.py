"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

File: breakoutgraphics.py
Name: Elaine Yen
---------------------------
This program plays a game called
'breakout' in which players
moving the mouse to rebounce
the ball to delete bricks
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.

NUM_LIVES = 3          # Initial lives when player start the game.


class BreakoutGraphics:
    """
    Create a graphical window, a paddle,a filled ball in the graphical window.
    Default initial velocity for the ball, draw bricks, and initialize our mouse listeners.
    """
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        self.ball_radius = ball_radius
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(width=paddle_width, height=paddle_height,
                            x=(self.window.width-PADDLE_WIDTH)/2, y=self.window.height-paddle_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.ball = GOval(width=2*ball_radius, height=2*ball_radius,
                          x=(self.window.width - 2*self.ball_radius) / 2, y=(self.window.height - 2*self.ball_radius)/2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED

        # Draw bricks.
        color_set = int(brick_rows / 5)
        for i in range(0*color_set, 0*color_set+(color_set)):
            for j in range(brick_cols):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.fill = True
                self.window.add(self.brick, x=j * (brick_width + brick_spacing), y=i * (brick_height + brick_spacing))
                self.brick.fill_color = 'red'

        for i in range(1 * color_set, 1 * color_set + (color_set)):
            for j in range(brick_cols):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.fill = True
                self.window.add(self.brick, x=j * (brick_width + brick_spacing),
                                y=i * (brick_height + brick_spacing))
                self.brick.fill_color = 'orange'

        for i in range(2 * color_set, 2 * color_set + (color_set)):
            for j in range(brick_cols):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.fill = True
                self.window.add(self.brick, x=j * (brick_width + brick_spacing),
                                y=i * (brick_height + brick_spacing))
                self.brick.fill_color = 'yellow'

        for i in range(3 * color_set, 3 * color_set + (color_set)):
            for j in range(brick_cols):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.fill = True
                self.window.add(self.brick, x=j * (brick_width + brick_spacing),
                                y=i * (brick_height + brick_spacing))
                self.brick.fill_color = 'green'

        for i in range(4 * color_set, brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.fill = True
                self.window.add(self.brick, x=j * (brick_width + brick_spacing),
                                y=i * (brick_height + brick_spacing))
                self.brick.fill_color = 'blue'

        # Initialize our mouse listeners.
        onmousemoved(self.reset_paddle_position)
        self.ball_start = False
        onmouseclicked(self.click)

        self.lives = NUM_LIVES
        self.brick_number = brick_cols * brick_rows

    def get_dx(self):
        """
        set a getter for breakout.py to get ball x velocity.
        """
        return self.__dx

    def get_dy(self):
        """
        set a getter for breakout.py to get ball y velocity.
        """
        return self.__dy

    def set_ball_velocity(self):
        """
        Sets ball x velocity to random negative or positive number.
        Sets ball y velocity to random positive number.
        """
        self.__dx = random.randint(0, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def handle_object_collisions(self):
        """
        Updates dx and dy depending on whether or not ball has hit a object.
        """
        maybe_collisions = self.window.get_object_at(self.ball.x, self.ball.y)
        # check whether the ball hit a object
        if maybe_collisions is not None:
            # hit a brick
            if maybe_collisions is not self.paddle:
                self.window.remove(maybe_collisions)
                self.brick_number -= 1
            # hit the paddle
            else:
                self.ball.y = self.paddle.y-self.ball.height
            self.__dy *= -1
        else:
            maybe_collisions = self.window.get_object_at(self.ball.x+2*self.ball_radius, self.ball.y)
            if maybe_collisions is not None:
                # hit a brick
                if maybe_collisions is not self.paddle:
                    self.window.remove(maybe_collisions)
                    self.brick_number -= 1
                # hit the paddle
                else:
                    self.ball.y = self.paddle.y - self.ball.height
                self.__dy *= -1
            else:
                maybe_collisions = self.window.get_object_at(self.ball.x, self.ball.y+2*self.ball_radius)
                if maybe_collisions is not None:
                    # hit a brick
                    if maybe_collisions is not self.paddle:
                        self.window.remove(maybe_collisions)
                        self.brick_number -= 1
                    # hit the paddle
                    else:
                        self.ball.y = self.paddle.y - self.ball.height
                    self.__dy *= -1
                else:
                    maybe_collisions = self.window.get_object_at(self.ball.x+2*self.ball_radius, self.ball.y+2*self.ball_radius)
                    if maybe_collisions is not None:
                        # hit a brick
                        if maybe_collisions is not self.paddle:
                            self.window.remove(maybe_collisions)
                            self.brick_number -= 1
                        # hit the paddle
                        else:
                            self.ball.y = self.paddle.y - self.ball.height
                        self.__dy *= -1

    def reset_paddle_position(self, event):
        """
        Use campy mouse event to reset the position of the paddle.
        """
        self.paddle.x = event.x - self.paddle.width / 2
        if self.paddle.x <= 0:
            self.paddle.x = 0
        elif self.paddle.x >= self.window.width-self.paddle.width:
            self.paddle.x = self.window.width-self.paddle.width

    def click(self, event):
        """
        Starts the game if the mouse was clicked.
        Input:
            event (GMouseEvent): mouse clicked event
        """
        self.ball_start = True

    def handle_wall_collisions(self):
        """
        Updates dx and dy depending on whether or not ball has hit a wall
        """
        if self.ball.x <= 0 or self.ball.x >= self.window.width - self.ball.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy
        if self.ball.y >= self.window.height - self.ball.height:
            self.lives -= 1
            self.ball.x = (self.window.width - 2*self.ball_radius) / 2
            self.ball.y = (self.window.height - 2*self.ball_radius)/2
            self.ball_start = False









