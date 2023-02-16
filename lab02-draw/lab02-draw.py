"""
Dibujo laaboratiorio (Ejercicio 2)
"""

import arcade

#Plantilla de dibujo
arcade.open_window(800,600,"Mi precioso dibujo")

#Fondo
arcade.set_background_color(arcade.color.ATOMIC_TANGERINE)

#Comienzo para dibujar (?)
arcade.start_render()

#Montaña
arcade.draw_triangle_filled(300,100,600,400,900,100,arcade.color.COOL_GREY)


#Acabar dibujo
arcade.finish_render()

#Mantener pestaña abierta
arcade.run()


