""" Lab 7 - User Control """

import arcade
import random

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

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
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.ball = Ball(50,50,15,arcade.color.FLORAL_WHITE)


        self.tree = Tree(400,300)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.DOLLAR_BILL)

        self.ball.draw()
        self.tree.draw()



def main():
    window = MyGame()
    arcade.run()


main()