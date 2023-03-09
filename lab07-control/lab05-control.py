""" Lab 7 - User Control """

import arcade
import random

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Arbol:
    def __init__(self,position_x,postion_y):

        self.position_x = position_x
        self.position_y = position_y
    def arbol(x, y):
        """int, int, int  --> nada
        OBJ: crea un arbol con la base del tronco en las cordenadas x e y"""
        arcade.draw_rectangle_filled(x, y + 25, 10, 50, arcade.color.DONKEY_BROWN)
        arcade.draw_triangle_filled(x - 25, y + 75, x, y + 125, x + 25, y + 75, arcade.color.AO)
        arcade.draw_triangle_filled(x - 25, y + 50, x, y + 100, x + 25, y + 50, arcade.color.AO)
        arcade.draw_triangle_filled(x - 25, y + 25, x, y + 75, x + 25, y + 25, arcade.color.AO)

    def draw(self):
        arbol(self.position_x,self.position_y)
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

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.DOLLAR_BILL)

        self.ball.draw()
        # Arboles



def main():
    window = MyGame()
    arcade.run()


main()