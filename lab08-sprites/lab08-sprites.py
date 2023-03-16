""" Lab 8 - Sprites"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8 - Sprites")


        self.set_mouse_visible(True)




    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.BISQUE)








def main():
    window = MyGame()
    arcade.run()


main()