import arcade
import math
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

RIFLE_WIDTH = 100
RIFLE_HEIGHT = 20
RIFLE_COLOR = arcade.color.DARK_RED

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

LASER_RADIUS = 6
LASER_COLOR = arcade.color.AZURE_MIST

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE
TARGET_SAFE_RADIUS = 15
BOMB_COLOR = arcade.color.BLACK
BOMB_RADIUS = 25


class Point:
    def __init__(self):
        self.x = float()
        self.y = float()


class Velocity:
    def __init__(self):
        self.dx = float()
        self.dy = float()


class FlyingObject:
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.alive = True

    def is_off_screen(self, screen_width, screen_height):
        if (self.center.x >= screen_width) or \
                (self.center.x < 0) or \
                (self.center.y >= screen_height) or \
                (self.center.y < 0):
            return True

    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def draw(self):
        pass


class Target(FlyingObject):
    def __init__(self):
        self.radius = TARGET_RADIUS
        super().__init__()
        self.center.x = 0
        self.center.y = random.randint(SCREEN_HEIGHT/2, SCREEN_HEIGHT)
        self.velocity.dx = random.uniform(1, 5)
        self.velocity.dy = random.uniform(-4, 3)
            #changed velocity.dy because too many targets fly off upper left corner

    def draw(self):
        pass

    def hit(self):
        self.alive = False
        return 1


class StandardTarget(Target):

    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, TARGET_COLOR)


class StrongTarget(Target):
    def __init__(self):
        self.lives = 3
        super().__init__()
        self.velocity.dx = random.uniform(1, 3)
        self.velocity.dy = random.uniform(-2, 3)

    def draw(self):
        arcade.draw_circle_outline(self.center.x, self.center.y, self.radius, TARGET_COLOR)
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        arcade.draw_text(repr(self.lives), text_x, text_y, TARGET_COLOR, font_size=20)

    def hit(self):
        if self.lives > 1:
            self.lives -= 1
            return 1
        if self.lives == 1:
            self.alive = False
            return 5


class SafeTarget(Target):
    def __init__(self):
        super().__init__()
        self.radius = TARGET_SAFE_RADIUS

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y,
                                     self.radius*2, self.radius*2, TARGET_SAFE_COLOR)

    def hit(self):
        self.alive = False
        return -10


class Bomb(Target):
    def init(self):
        super().__init__()

    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, BOMB_COLOR)


class Bullet(FlyingObject):
    def __init__(self):
        self.radius = BULLET_RADIUS
        super().__init__()
        self.center.x = 0
        self.center.y = 0

    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, BULLET_COLOR)

    def fire(self, angle: float):
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED


class Laser(Bullet):
    def __init__(self):
        self.radius = LASER_RADIUS
        super().__init__()

    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, LASER_COLOR)

    def fire(self, angle: float):
        self.velocity.dx = math.cos(math.radians(angle)) * 2*BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * 2*BULLET_SPEED


class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """

    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0

        self.angle = 45

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, RIFLE_WIDTH,
                                     RIFLE_HEIGHT, RIFLE_COLOR, self.angle)


def main():
    bombs = []
    bomb = Bomb()
    bombs.append(bomb)
    for bomb in bombs:
        if bomb == Bomb():
            print("True")
    print("also print this")
main()

