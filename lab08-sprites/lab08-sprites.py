""" Lab 8 - Sprites"""

import arcade
import random

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_COIN = 0.05
SPRITE_SCALING_GHOST = 0.05

COIN_COUNT = 50
COIN_VOLUME = 1.0

GHOST_COUNT = 3
DAMAGE_VOLUME = 1.0

MOVEMENT_SPEED = 3

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8 - Sprites")

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Variables that will hold sprite lists.
        self.player_list = None
        self.coin_list = None
        self.ghost_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0
        self.lives = 0



        arcade.set_background_color(arcade.color.CERULEAN_BLUE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()

        # Sounds
        self.coin_sound = arcade.load_sound("C:\Tecnologia de Videojuegos\LOCAL_SOUNDS\Mario_coin.wav", False)
        self.damage_sound = arcade.load_sound("C:\Tecnologia de Videojuegos\LOCAL_SOUNDS\Mario_oof.wav",False)

        # Score
        self.score = 0

        # Lives
        self.lives = 3

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("C:\Tecnologia de Videojuegos\LOCAL_IMAGES\Mario_head.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):
            # Create the coin instance

            coin = arcade.Sprite("C:\Tecnologia de Videojuegos\LOCAL_IMAGES\Mario_coin.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        # Create the ghosts
        for i in range(GHOST_COUNT):
            # Create the ghost instance

            ghost = arcade.Sprite("C:\Tecnologia de Videojuegos\LOCAL_IMAGES\Mario_ghost.png", SPRITE_SCALING_GHOST)

            # Position the ghost
            ghost.center_x = random.randrange(SCREEN_WIDTH)
            ghost.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the ghost to the lists
            self.ghost_list.append(ghost)

    def on_draw(self):
        arcade.start_render()

        self.coin_list.draw()
        self.player_list.draw()
        self.ghost_list.draw()

        # Put the text on the screen.
        output1 = f"Coins: {self.score}"
        arcade.draw_text(output1, 10, 20, arcade.color.WHITE, 14)
        output2 = f"Lives: {self.lives}"
        arcade.draw_text(output2,10,40,arcade.color.WHITE,14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()
        self.ghost_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)
        ghost_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.ghost_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.coin_sound,COIN_VOLUME)
            self.score += 1

        for ghost in ghost_hit_list:
            arcade.play_sound(self.damage_sound,DAMAGE_VOLUME)
            self.lives -=1


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()