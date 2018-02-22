
import arcade
from random import randint

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BALL_RADIUS = 10
RECT_WIDTH = 10
RECT_HEIGHT = 50


class Pong(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        self.paddle_x_position = 385
        self.paddle_y_position = 150
        self.spawn_ball()

        arcade.set_background_color(arcade.color.BLACK)

        # Note:
        # You can change how often the animate() method is called by using the
        # set_update_rate() method in the parent class.
        # The default is once every 1/80 of a second.
        # self.set_update_rate(1/80)


    def spawn_ball(self):
        """Sets or resets the location and velocity of the ball"""
        self.ball_x_position = 10
        self.ball_y_position = randint(10, 290)
        self.ball_x_pixels_per_second = randint(100, 600)
        self.ball_y_pixels_per_second = randint(0, 300)


    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Draw the pong ball
        arcade.draw_circle_filled(self.ball_x_position, self.ball_y_position,
                                  BALL_RADIUS, arcade.color.WHITE)

        # Draw the paddle
        arcade.draw_commands.draw_rectangle_filled(self.paddle_x_position, self.paddle_y_position,
                                                   RECT_WIDTH, RECT_HEIGHT, arcade.color.WHITE)


    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        # Move the ball
        self.ball_x_position += self.ball_x_pixels_per_second * delta_time
        self.ball_y_position += self.ball_y_pixels_per_second * delta_time



        # Did the ball hit the right side of the screen while moving right?
        if self.ball_x_position > SCREEN_WIDTH + BALL_RADIUS:
            self.spawn_ball()

        # Did the ball hit the left side of the screen while moving left?
        if self.ball_x_position <= BALL_RADIUS \
                and self.ball_x_pixels_per_second < 0:
            self.ball_x_pixels_per_second *= -1

        # Did the ball hit the top side of the screen?
        if self.ball_y_position >= SCREEN_HEIGHT - BALL_RADIUS \
                and self.ball_y_pixels_per_second > 0:
            self.ball_y_pixels_per_second *= -1

        # Did the ball hit the bottom side of the screen?
        if self.ball_y_position <= BALL_RADIUS \
                and self.ball_y_pixels_per_second < 0:
            self.ball_y_pixels_per_second *= -1

        # Did the ball hit the paddle?
        if self.paddle_x_position - self.ball_x_position <= 15 \
                and abs(self.ball_y_position - self.paddle_y_position) <= 35 \
                and self.ball_x_pixels_per_second > 0:
            self.ball_x_pixels_per_second *= -1


    #def paddle_move(self, value):
        #if value == TRUE:



    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://pythonhosted.org/arcade/arcade.key.html
        """

        # See if the user hit Shift-Space
        # (Key modifiers are in powers of two, so you can detect multiple
        # modifiers by using a bit-wise 'and'.)
        if key == arcade.key.SPACE and key_modifiers == arcade.key.MOD_SHIFT:
            print("You pressed shift-space")

        # See if the user just hit space.
        elif key == arcade.key.SPACE:
            print("You pressed the space bar.")

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.SPACE:
            print("You stopped pressing the space bar.")

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        # if button == arcade.MOUSE_BUTTON_LEFT:
          #  self.ball_x_pixels_per_second += 1

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        # if button == arcade.MOUSE_BUTTON_LEFT:
          #  self.ball_x_pixels_per_second += 1


def main():
    """ Main method """
    Pong(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()