"""
Dibujo laaboratiorio (Ejercicio 2)
"""

import arcade

#Plantilla de dibujo
arcade.open_window(1200,800,"Mi precioso dibujo")

#Fondo
arcade.set_background_color(arcade.color.ATOMIC_TANGERINE)

#Comienzo para dibujar
arcade.start_render()



#Montaña
arcade.draw_triangle_filled(300,100,600,700,900,100,arcade.color.COOL_GREY)
arcade.draw_triangle_filled(550,600,600,700,650,600,arcade.color.WHITE)



#Acabar dibujo
arcade.finish_render()

#Mantener pestaña abierta
arcade.run()


