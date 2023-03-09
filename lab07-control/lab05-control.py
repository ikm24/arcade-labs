""" Lab 7 - User Control """

import arcade
import random

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

class Tree:
    def __init__(self,position_x,position_y):

        self.position_x = position_x
        self.position_y = position_y


    def draw(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y + 25, 10, 50, arcade.color.DONKEY_BROWN)
        arcade.draw_triangle_filled(self.position_x - 25, self.position_y + 75, self.position_x, self.position_y + 125, self.position_x + 25, self.position_y + 75, arcade.color.AO)
        arcade.draw_triangle_filled(self.position_x - 25, self.position_y + 50, self.position_x, self.position_y + 100, self.position_x + 25, self.position_y + 50, arcade.color.AO)
        arcade.draw_triangle_filled(self.position_x - 25, self.position_y + 25, self.position_x, self.position_y + 75, self.position_x + 25, self.position_y + 25, arcade.color.AO)

class Ball:
    def __init__(self, position_x, position_y,change_x,change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")


        self.set_mouse_visible(True)


        self.ball = Ball(50,50,0,0,15,arcade.color.FLORAL_WHITE)

        self.tree1 = Tree(750,200)
        self.tree2 = Tree(750,75)
        self.tree3 = Tree(625,50)
        self.tree4 = Tree(685, 145)
        self.tree5 = Tree(700,35)


    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.BABY_BLUE)

        # Sol
        arcade.draw_circle_filled(800, 580, 100, arcade.color.ICTERINE)

        # Montaña centro
        arcade.draw_triangle_filled(100, 100, 400, 700, 700, 100, arcade.color.AUROMETALSAURUS)
        arcade.draw_triangle_filled(350, 600, 400, 700, 450, 600, arcade.color.WHITE_SMOKE)
        # Montaña derecha
        arcade.draw_triangle_filled(300, 0, 600, 600, 900, 0, arcade.color.ASH_GREY)
        arcade.draw_triangle_filled(550, 500, 600, 600, 650, 500, arcade.color.GHOST_WHITE)
        # Montaña izquierda
        arcade.draw_triangle_filled(-100, 0, 200, 600, 500, 0, arcade.color.ASH_GREY)
        arcade.draw_triangle_filled(150, 500, 200, 600, 250, 500, arcade.color.GHOST_WHITE)

        # Lago
        arcade.draw_rectangle_filled(600, 100, 1200, 300, arcade.color.BLEU_DE_FRANCE)

        self.ball.draw()

        # Cosa verde
        arcade.draw_circle_filled(1400, -500, 1000, arcade.color.DOLLAR_BILL)

        self.tree1.draw()
        self.tree2.draw()
        self.tree3.draw()
        self.tree4.draw()
        self.tree5.draw()


    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """

        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.position_x = x
            self.ball.position_y = y


def main():
    window = MyGame()
    arcade.run()


main()