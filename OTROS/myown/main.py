import pygame as pg

pg.init()

screen = pg.display.set_mode((800,600))
run = True
xd = pg.image.load("C:/Users/ElPapu/Desktop/momazos diego/pastel_de_papa.jpg")
personaje = pg.image.load("C:/Users/ElPapu/Desktop/complicado.png")

def main_menu():
    run = True
    
    while run:
        pass



personaje = pg.image.load("C:/Users/ElPapu/Desktop/complicado.png")
while run:
    
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            run = False
        
        if event.type == pg.KEYDOWN:
            match event.type:
                case K_a:
                    run = False
                    print("SOS TERRIBLE PUTTTT")
    
    screen.blit(personaje,(5,5))
    boton_1 = pg.Rect(50,50,50,50)
    
    pg.display.update()
        

