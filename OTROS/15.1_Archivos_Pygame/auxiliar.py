import pygame as pg 

def crear_lista_botones(cantidad: int, dimension: tuple, color: str = 'purple'):
    lista_botones = [] 
    for i in range(cantidad):
        boton = {}
        boton['superficie'] = pg.Surface(dimension)
        boton['rectangulo'] = boton.get('superficie').get_rect()
        boton['superficie'].fill(pg.Color(color))
        lista_botones.append(boton)
    return lista_botones

def mostrar_texto(surface: pg.Surface, texto: str, pos: tuple, font, color = pg.Color('black')):
    words = []
    
    for word in texto.splitlines():
        words.append(word.split(' '))
    
    space = font.size(' ')[0]
    ancho_max, alto_max = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            ancho_palabra, alto_palabra = word_surface.get_size()
            if x + ancho_palabra >= ancho_max:
                x = pos[0]
                y += alto_palabra
            surface.blit(word_surface, (x, y))
            x += ancho_palabra + space
        x = pos[0]
        y += alto_palabra

def crear_cuadro(dimensiones: tuple, coordenadas: tuple, color: tuple) -> dict:
    cuadro = {}
    cuadro['superficie'] = pg.Surface(dimensiones)
    cuadro['rectangulo'] = cuadro.get('superficie').get_rect()
    cuadro['rectangulo'].topleft = coordenadas
    cuadro['superficie'].fill(pg.Color(color))
    return cuadro

def crear_boton(pantalla: pg.Surface, texto: str, ruta_fuente: str, dimensiones: tuple, coordenadas: tuple,color_fondo: tuple, color_texto: tuple):
    cuadro = crear_cuadro(dimensiones, coordenadas, color_fondo)
    cuadro['texto'] = texto
    cuadro['pantalla'] = pantalla
    cuadro['color_texto'] = color_texto
    cuadro['color_boton'] = color_fondo
    cuadro['font_path'] = ruta_fuente
    cuadro['padding'] = (10,10)
    return cuadro

def mostrar_boton(boton_dict: dict):
    mostrar_texto(
        boton_dict.get('superficie'),
        boton_dict.get('texto'),
        boton_dict.get('padding'),
        boton_dict.get('font_path'),
        boton_dict.get('color_texto')
    )
    boton_dict['rectangulo'] = boton_dict.get('pantalla').blit(
        boton_dict.get('superficie'), boton_dict.get('rectangulo').topleft
    )
    pg.draw.rect(boton_dict.get('pantalla'), boton_dict.get('color_boton'), boton_dict.get('rectangulo'), 2)