"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others - Modified by: Bryce Kaline
This program implements the asteroids game.
"""
import arcade
import math
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_BRAKE_AMOUNT = 0.95
SHIP_RADIUS = 30
SHIP_RELOAD_TIME = 150

SHIELD_RADIUS = 70
SHIELD_LIFE = 200

LEVEL_TIMER = 200
INITIAL_LIVES = 5

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15
BIG_ROCK_POINTS = 10

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5
MEDIUM_ROCK_POINTS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2
SMALL_ROCK_POINTS = 3


class Point:
    def __init__(self):
        self.x = float()
        self.y = float()


class Velocity:
    def __init__(self):
        self.dx = float()
        self.dy = float()

        # This is angular velocity
        # included here because I may decide to give the ship angular inertia
        self.spin = float()


class FlyingObject:
    def __init__(self, img):
        self.center = Point()
        self.velocity = Velocity()
        self.radius = float()
        self.angle = float()

        self.img = img
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.alpha = 1

        self.alive = True

    def wrap(self):
        if (self.center.x >= SCREEN_WIDTH + self.radius) and self.velocity.dx > 0:
            self.center.x = -self.radius
        if (self.center.x <= -self.radius) and self.velocity.dx < 0:
            self.center.x = SCREEN_WIDTH + self.radius
        if (self.center.y >= SCREEN_HEIGHT + self.radius) and self.velocity.dy > 0:
            self.center.y = -self.radius
        if (self.center.y <= -self.radius) and self.velocity.dy < 0:
            self.center.y = SCREEN_HEIGHT + self.radius

    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        self.angle += self.velocity.spin
        self.wrap()

    def draw(self):
        pass


class Ship(FlyingObject):
    def __init__(self):
        super().__init__("images/playerShip1_orange.png")
        self.center.x = SCREEN_WIDTH / 2
        self.center.y = SCREEN_HEIGHT / 2
        self.radius = SHIP_RADIUS
        self.angle = 90
        self.reload_timer = SHIP_RELOAD_TIME

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width,
                                      self.height, self.texture, self.angle, self.alpha)


class Shield(FlyingObject):
    def __init__(self, x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2, dx=0, dy=0):
        super().__init__("images/shipShield_blue.png")
        self.center.x = x
        self.center.y = y
        self.velocity.dx = dx
        self.velocity.dy = dy

        self.radius = SHIELD_RADIUS
        self.life = SHIELD_LIFE
        self.alive = False

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width,
                                      self.height, self.texture, 0, self.alpha)

    def d_alpha(self, var):
        self.alpha += math.sin(math.radians(var))

    def trace(self, x, y, angle):
        self.center.x = x
        self.center.y = y
        self.angle = angle


class Bullet(FlyingObject):
    def __init__(self, x, y, dx, dy, angle):  # we will pass the ship's position & velocity to the bullet
        super().__init__("images/laserBlue01.png")
        self.center.x = x
        self.center.y = y
        self.velocity.dx = dx
        self.velocity.dy = dy

        self.radius = BULLET_RADIUS
        self.angle = angle
        self.life = BULLET_LIFE

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width,
                                      self.height, self.texture, self.angle, self.alpha)

    def fire(self, angle):
        self.velocity.dx += math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy += math.sin(math.radians(angle)) * BULLET_SPEED


class Asteroid(FlyingObject):
    def __init__(self, img, life=1):
        super().__init__(img)
        self.life = life  # the amount of shots required to kill a rock is set to the current game level
        self.point_value = int()

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width,
                                      self.height, self.texture, self.angle, self.alpha)


class LargeRock(Asteroid):
    def __init__(self, life=1):
        super().__init__("images/meteorGrey_big1.png", life=life)
        self.center.x = random.randint(*random.choice([(0, SCREEN_WIDTH / 2 - 100),
                                                       (SCREEN_WIDTH / 2 + 100, SCREEN_WIDTH)]))
        self.center.y = random.randint(*random.choice([(0, SCREEN_HEIGHT / 2 - 100),
                                                       (SCREEN_HEIGHT / 2 + 100, SCREEN_HEIGHT)]))

        self.direction = random.uniform(0, 2 * math.pi)  # aids in calculating random starting direction
        self.velocity.dx = BIG_ROCK_SPEED * math.cos(self.direction)
        self.velocity.dy = BIG_ROCK_SPEED * math.sin(self.direction)

        self.velocity.spin = BIG_ROCK_SPIN
        self.radius = BIG_ROCK_RADIUS

        self.point_value = BIG_ROCK_POINTS


class MediumRock(Asteroid):
    def __init__(self, x, y, dx, dy, life=1):
        super().__init__("images/meteorGrey_med1.png", life=life)
        self.center.x = x
        self.center.y = y
        self.velocity.dx = dx
        self.velocity.dy = dy

        self.velocity.spin = MEDIUM_ROCK_SPIN
        self.radius = MEDIUM_ROCK_RADIUS

        self.point_value = MEDIUM_ROCK_POINTS


class SmallRock(Asteroid):
    def __init__(self, x, y, dx, dy, life=1):
        super().__init__("images/meteorGrey_small1.png", life=life)
        self.center.x = x
        self.center.y = y
        self.velocity.dx = dx
        self.velocity.dy = dy

        self.velocity.spin = SMALL_ROCK_SPIN
        self.radius = SMALL_ROCK_RADIUS

        self.point_value = SMALL_ROCK_POINTS


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.level_timer = LEVEL_TIMER
        # self.timer = 60  # this is for debugging

        self.held_keys = set()

        self.level = 1
        self.ship = Ship()
        self.shield = Shield()
        self.bullets = []
        self.asteroids = [LargeRock(life=self.level) for i in range(INITIAL_ROCK_COUNT)]

        self.lives = INITIAL_LIVES
        self.score = 0

    def draw_texts(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}\n Level: {}".format(self.score, self.level)
        lives_text = "Lives: {}".format(self.lives)
        start_score_x = 10
        start_score_y = SCREEN_HEIGHT - 20
        start_lives_x = SCREEN_WIDTH - 75
        start_lives_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_score_x, start_y=start_score_y,
                         font_size=14, color=arcade.color.TEAL_BLUE)
        arcade.draw_text(lives_text, start_x=start_lives_x, start_y=start_lives_y,
                         font_size=14, color=arcade.color.TEAL_BLUE)

        # poor code, it will do for now
        game_over = "               GAME OVER \n YOU HAVE FAILED SO MUCH \n \
              your score: {}".format(self.score)
        if self.lives <= 0:
            for rock in self.asteroids:
                rock.alive = False
            self.ship.alive = False
            arcade.draw_text(game_over, start_x=50, start_y=400,
                             font_size=36, color=arcade.color.RED)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        if self.ship.alive:
            self.ship.draw()

        if self.shield.alive:
            self.shield.draw()

        for bullet in self.bullets:
            bullet.draw()

        for rock in self.asteroids:
            rock.draw()

        self.draw_texts()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()
        self.ship.advance()

        for bullet in self.bullets:
            bullet.advance()
            bullet.life -= 1
            if bullet.life <= 0:
                bullet.alive = False

        for rock in self.asteroids:
            rock.advance()

        if self.shield.alive:
            self.shield.trace(self.ship.center.x, self.ship.center.y, self.ship.angle)
            self.shield.d_alpha(delta_time)
            self.shield.life -= 1
            if self.shield.life <= 0:
                self.shield.alive = False
                self.shield.life = SHIELD_LIFE

        if len(self.asteroids) == 0:
            if len(self.asteroids) == 0:
                self.level_timer -= 1
            if self.level_timer <= 0:
                self.level += 1
                self.lives += 1
                self.asteroids = [LargeRock(life=self.level) for i in range(INITIAL_ROCK_COUNT)]
                self.shield.alive = True
                self.level_timer = LEVEL_TIMER

        self.valar_morghulis()

        # Check for collisions
        for rock in self.asteroids:
            for bullet in self.bullets:
                if rock.alive and bullet.alive:
                    too_close = rock.radius + bullet.radius

                    if abs(rock.center.x - bullet.center.x) <= too_close and \
                            abs(rock.center.y - bullet.center.y) <= too_close:
                        bullet.alive = False
                        rock.life -= 1
                        if rock.life <= 0:
                            self.score += rock.point_value
                            rock.alive = False
                            self.split_rocks(rock)

            if rock.alive and self.ship.alive:
                too_close = rock.radius + self.ship.radius
                if abs(rock.center.x - self.ship.center.x) <= too_close and \
                        abs(rock.center.y - self.ship.center.y) <= too_close:
                    rock.life -= 1
                    if rock.life <= 0:
                        self.score += rock.point_value
                        rock.alive = False
                        self.split_rocks(rock)
                    self.ship.alive = False

            if rock.alive and self.shield.alive:
                too_close = rock.radius + self.shield.radius
                if abs(rock.center.x - self.shield.center.x) <= too_close and \
                        abs(rock.center.y - self.shield.center.y) <= too_close:
                    rock.alive = False  # the shield destroys rocks on impact
                    self.split_rocks(rock)

    def split_rocks(self, rock: Asteroid):
        if isinstance(rock, LargeRock):
            medium_rock1 = MediumRock(rock.center.x, rock.center.y,
                                      rock.velocity.dx, rock.velocity.dy + 2, rock.life)
            medium_rock2 = MediumRock(rock.center.x, rock.center.y,
                                      rock.velocity.dx, rock.velocity.dy - 2, rock.life)
            small_rock = SmallRock(rock.center.x, rock.center.y,
                                   rock.velocity.dx + 5, rock.velocity.dy, rock.life)
            self.asteroids.append(medium_rock1)
            self.asteroids.append(medium_rock2)
            self.asteroids.append(small_rock)
        elif isinstance(rock, MediumRock):
            small_rock1 = SmallRock(rock.center.x, rock.center.y,
                                    rock.velocity.dx + 1.5, rock.velocity.dy + 1.5, rock.life)
            small_rock2 = SmallRock(rock.center.x, rock.center.y,
                                    rock.velocity.dx - 1.5, rock.velocity.dy - 1.5, rock.life)
            self.asteroids.append(small_rock1)
            self.asteroids.append(small_rock2)

    def valar_morghulis(self):
        """
        All [flying objects] must die.
        Checks whether flying objects are alive, and if not, removes them from the game.
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for rock in self.asteroids:
            if not rock.alive:
                self.asteroids.remove(rock)

        if not self.ship.alive:
            self.ship.reload_timer -= 1
            if self.ship.reload_timer <= 0:
                self.ship = Ship()
                self.shield.alive = True
                self.lives -= 1

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.angle += SHIP_TURN_AMOUNT

        if arcade.key.RIGHT in self.held_keys:
            self.ship.angle -= SHIP_TURN_AMOUNT

        if arcade.key.UP in self.held_keys:
            self.ship.velocity.dx += SHIP_THRUST_AMOUNT * math.cos(math.radians(self.ship.angle))
            self.ship.velocity.dy += SHIP_THRUST_AMOUNT * math.sin(math.radians(self.ship.angle))

        # The DOWN key is designed as a brake
        if arcade.key.DOWN in self.held_keys:
            self.ship.velocity.dx *= SHIP_BRAKE_AMOUNT
            self.ship.velocity.dy *= SHIP_BRAKE_AMOUNT

        # Machine gun mode...
        # if arcade.key.SPACE in self.held_keys:
        #    pass

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # Fires the bullet
                bullet = Bullet(self.ship.center.x, self.ship.center.y,
                                self.ship.velocity.dx, self.ship.velocity.dy, self.ship.angle)
                bullet.fire(self.ship.angle)
                self.bullets.append(bullet)

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)

    # This is for debugging
    # def print_info(self):
    #     self.timer -= 1
    #     if self.timer == 0:
    #         print(math.sqrt(self.asteroids[0].velocity.dx ** 2 + self.asteroids[0].velocity.dy ** 2))
    #         self.timer = 60


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
