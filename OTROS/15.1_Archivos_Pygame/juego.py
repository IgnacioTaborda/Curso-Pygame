import pygame as pg 
import variables as var
import forms.menu as menu
import forms.historia as historia

def pythonisa():
    
    pg.display.set_caption(var.TITULO_JUEGO)
    pantalla = pg.display.set_mode(var.DIMENSION_PANTALLA)
    corriendo =True
    reloj = pg.time.Clock()
    form_actual = 'menu'
    bandera_juego = False
    datos_juego = {
        "puntuacion": 0,
        "cantidad_vidas": var.CANTIDAD_VIDAS,
        "nombre": '',
        'volumen_musica' : 100
    }
    
    while corriendo:
        
        
        cola_eventos = pg.event.get()
        reloj.tick(var.FPS)
        
        if form_actual == 'menu':
            form_actual = menu.mostrar_menu(pantalla, cola_eventos)
        elif form_actual == 'historia':
            form_actual, bandera_juego = historia.mostrar_historia(pantalla, cola_eventos)
        elif form_actual == 'salir':
            corriendo = False

        pg.display.flip()
    pg.quit()