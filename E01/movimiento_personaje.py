import pygame as pg

dict_movimientos = {
        "arriba" : False,
        "abajo" : False,
        "derecha" : False,
        "izquierda" : False    
    }

def keydown(dict_movimientos, event_key):
    match event_key:
        case pg.K_a:
            retorno = dict_movimientos["izquierda"] = True
        case pg.K_d:
            retorno = dict_movimientos["derecha"] = True
        case pg.K_w:
            retorno = dict_movimientos["arriba"] = True
        case pg.K_s:
            retorno = dict_movimientos["abajo"] = True
    return retorno

def keyup(dict_movimientos, event_key):
    match event_key:
        case pg.K_a:
            retorno = dict_movimientos["izquierda"] = False
        case pg.K_d:
            retorno = dict_movimientos["derecha"] = False
        case pg.K_w:
            retorno = dict_movimientos["arriba"] = False
        case pg.K_s:
            retorno = dict_movimientos["abajo"] = False
    return retorno