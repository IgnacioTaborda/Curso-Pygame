import pygame as pg
import constantes as cons

class Personaje():
    def __init__(self, coordenada_x, coordenada_y, alto, ancho):
        self.shape = pg.Rect(coordenada_x, coordenada_y, alto, ancho)
        #self.shape.center = (coordenada_x, coordenada_y)
        
    def dibujar(self, interfaz, color):
        pg.draw.rect(interfaz, color, self.shape)
        
    def movimiento(self, mov_x, mov_y):
        self.shape.x = self.shape.x + mov_x
        self.shape.y = self.shape.y + mov_y
