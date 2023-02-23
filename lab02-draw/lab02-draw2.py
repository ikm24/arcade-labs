"""
Dibujo lab usando funciones
"""

import arcade

#Plantilla de dibujo
arcade.open_window(1200,800,"Mi precioso dibujo")

#Fondo
arcade.set_background_color(arcade.color.BABY_BLUE)


#Comienzo para dibujar
arcade.start_render()

'''
#Sol
arcade.draw_circle_filled(1000,680,100,arcade.color.ICTERINE)
'''
'''

#Montaña centro
arcade.draw_triangle_filled(100,200,400,800,700,200,arcade.color.AUROMETALSAURUS)
arcade.draw_triangle_filled(350,700,400,800,450,700,arcade.color.WHITE_SMOKE)
#Montaña derecha
arcade.draw_triangle_filled(300,100,600,700,900,100,arcade.color.ASH_GREY)
arcade.draw_triangle_filled(550,600,600,700,650,600,arcade.color.GHOST_WHITE)
#Montaña izquierda
arcade.draw_triangle_filled(-100,100,200,700,500,100,arcade.color.ASH_GREY)
arcade.draw_triangle_filled(150,600,200,700,250,600,arcade.color.GHOST_WHITE)
'''
'''

def montaña():
    
#Lago
arcade.draw_rectangle_filled(600,200,1200,200,arcade.color.BLEU_DE_FRANCE)

#Cosa verde
arcade.draw_circle_filled(1400,-500,1000,arcade.color.DOLLAR_BILL)
'''

def arbol(x,y):
    '''int, int --> nada
    OBJ: crea un arbol con centro en las cordenadas x e y'''
    arcade.draw_rectangle_filled(x, y-50, 10, 50, arcade.color.DONKEY_BROWN)
    arcade.draw_triangle_filled(x-25, y, x, y+50, x+25, y, arcade.color.AO)
    arcade.draw_triangle_filled(x-25, y-25, x, y+25, x+25, y-25, arcade.color.AO)
    arcade.draw_triangle_filled(x-25, y-50, x, y, x+25, y-50, arcade.color.AO)

'''
#Arboles
arcade.draw_rectangle_filled(725,200,10,50,arcade.color.DONKEY_BROWN) #x = 725 , y = 250
arcade.draw_triangle_filled(700,250,725,300,750,250,arcade.color.AO)
arcade.draw_triangle_filled(700,225,725,275,750,225,arcade.color.AO)
arcade.draw_triangle_filled(700,200,725,250,750,200,arcade.color.AO)
'''

#Acabar dibujo
arcade.finish_render()

#Mantener pestaña abierta
arcade.run()