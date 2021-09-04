import pygame as pg
from . import FPS, ANCHO, ALTO #el punto indica al módulo al que pertece, en este caso arkanoid
from .entidades import Raqueta

class Escena():
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        pass

class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla) #hace que siempre se ejecute el init del padre que es pantalla de la calse Escena
        self.logo = pg.image.load("resources/images/arkanoid_name.png")
        
        fuente = pg.font.Font("resources/fonts/LibreFranklin-VariableFont_wght.ttf", 28)
        self.start_text = fuente.render("Press <SPC> to start",True, (200, 200, 255))

    def bucle_principal(self):
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        game_over = True

            self.pantalla.fill((10, 0, 188))
            self.pantalla.blit(self.logo, (140,140)) # blit = calcamonía/poner encima
            self.pantalla.blit(self.start_text, ((ANCHO - self.start_text.get_width()) // 2, 640))
            
            pg.display.flip()

class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.fondo = pg.image.load("resources/images/background.jpg")
        self.player = Raqueta(midbottom=(ANCHO // 2, ALTO - 15))

    def bucle_principal(self):
        game_over = False
        while not game_over:
            self.reloj.tick(FPS)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

            self.player.update()

            self.pantalla.blit(self.fondo, (0,0))
            self.pantalla.blit(self.player.image, self.player.rect)
            pg.display.flip()


class Records(Escena):
    pass