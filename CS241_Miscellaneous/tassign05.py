import arcade
from random import randint

screen_width = 400
screen_height = 300


class Paddle:
    """
    Geometry, location, and movement of the paddle
    """

    def __init__(self, width=10, height=50, color=arcade.color.WHITE):
        self.width = width
        self.height = height
        self.x = 385
        self.y = 150
        self.color = color
        self.delta_y = 5

    def draw(self):
        """
        Draw the paddle
        """
        arcade.draw_commands.draw_rectangle_filled(self.x, self.y, self.width,
                                                   self.height, self.color)

    def move(self):
        """
        Move the paddle
        """
        self.y += self.delta_y


class Ball:
    """
    Geometry, location, and movement of the ball
    """

    def __init__(self, x=10, y=randint(10, 290), r=10,
                 delta_x=randint(100, 500), delta_y=randint(0, 350),
                 color=arcade.color.WHITE):
        self.x = x
        self.y = y
        self.r = r
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.color = color

    def draw(self):
        # Draws the ball
        arcade.draw_circle_filled(self.x, self.y, self.r, self.color)

    def move(self, paddle):
        # Move the ball
        self.x += self.delta_x
        self.y += self.delta_y

        # Did the ball hit the right side of the screen while moving right?
        if self.x > screen_width + self.r:
            self.__init__()

        # Did the ball hit the left side of the screen while moving left?
        if self.x <= self.r and self.delta_x < 0:
            self.delta_x *= -1

        # Did the ball hit the top side of the screen?
        if self.y >= screen_height - self.r and self.delta_y > 0:
            self.delta_y *= -1

        # Did the ball hit the bottom side of the screen?
        if self.y <= self.r and self.delta_y < 0:
            self.delta_y *= -1

        # Did the ball hit the paddle?
        if abs(self.x - paddle.x) <= 15 \
                and abs(self.y - paddle.y) <= 25 \
                and self.delta_x > 0:
            self.delta_x *= -1


class Pong(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)
        self.ball = None
        self.paddle = None

    def setup(self):
        self.paddle = Paddle()
        self.ball = Ball()

    def on_draw(self):
        # Render the screen.
        arcade.start_render()
        self.ball.draw()
        self.paddle.draw()

    def update(self, delta_t):
        """
        All the logic to move, and the game logic goes here.
        """
        # Move the ball
        self.ball.move(self.paddle)


def main():
    """ Main method """
    pong = Pong(screen_width, screen_height)
    pong.setup()
    arcade.run()


if __name__ == "__main__":
    main()
