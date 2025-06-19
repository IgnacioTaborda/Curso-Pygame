import pygame as pg
import constantes as cons
from personaje import Personaje
import movimiento_personaje as mov_pj

jugador = Personaje(50,50,cons.ALTO_PERSONAJE, cons.ANCHO_PERSONAJE) #JUGADOR Y SU POSICION X y Y


pg.init() #INICIA LA LIBRERIA

ventana = pg.display.set_mode(cons.RESOLUCION) #TAMAÑO DE PANTALLA
pg.display.set_caption("El Juego del Papu") #TITULO DE LA APP
run = True
reloj = pg.time.Clock() #CONTROLAR FPS
dict_movimientos = mov_pj.dict_movimientos

while run:
    
    jugador.dibujar(ventana,cons.VIOLETA) #PONEMOS AL JUGADOR EN LA CANTALLA y LE DAMOS COLOR
    reloj = cons.FPS
    
    delta_x = 0
    delta_y = 0
    
    if dict_movimientos["arriba"] == True:
        delta_y = -1
    if dict_movimientos["abajo"] == True:
        delta_y = 1
    if dict_movimientos["derecha"] == True:
        delta_x = 1
    if dict_movimientos["izquierda"] == True:
        delta_x = -1
        
    jugador.movimiento(delta_x,delta_y)
    
    for event in pg.event.get():
        
        ventana.fill(cons.BG)
        
        if event.type == pg.QUIT:
            run = False 
       
        if event.type == pg.KEYDOWN:   
            mov_pj.keydown(dict_movimientos, event.key)
            
        if event.type == pg.KEYUP:   
            mov_pj.keyup(dict_movimientos, event.key)
            
    pg.display.update()
  
pg.QUIT
