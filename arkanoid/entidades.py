import pygame as pg
from pygame.sprite import Sprite
from . import FPS, ANCHO, ALTO

class Raqueta (Sprite):
    disfraces = "electric00.png" #es una variables de clase, cuando lleva el self. es una variable de instancias
    def __init__(self, **kwargs): # **kwargs disccionario de parámetros
        self.image = pg.image.load(f"resources/images/{self.disfraces}")
        self.rect = self.image.get_rect(**kwargs)

    def update(self):
        if pg.key.get_pressed()[pg.K_LEFT]:
            self.rect.x -= 5
        
        if self.rect.x <= 0:
            self.rect.x = 0

        if self.rect.x >= ANCHO-self.rect.w:
            self.rect.x = ANCHO-self.rect.w

        if pg.key.get_pressed()[pg.K_RIGHT]:
            self.rect.x += 5


class Bola (Sprite):
    disfraces = "ball1.png"
    def __init__(self, **kwargs):
        self.image = pg.image.load(f"resources/images/{self.disfraces}")
        self.rect = self.image.get_rect(**kwargs)

        self.Derecha = True
        self.Arriba = True
        
    def update(self):
    
            if self.Derecha:
                self.rect.x += 5
            else:
                self.rect.x -= 5

            if self.rect.x >= ANCHO-self.rect.w:
                self.Derecha = False 
            
            if self.rect.x <= 0:
                self.Derecha = True

            if self.Arriba:
                self.rect.y -= 5
            else:
                self.rect.y += 5

            if self.rect.y >= ALTO - self.rect.h:
                self.Arriba = True
            
            if self.rect.y <= 0:
                self.Arriba = False

class Ladrillo (Sprite):
    disfraces = "greenTile.png"
    def __init__(self, **kwargs):
        self.image = pg.image.load(f"resources/images/{self.disfraces}")
        self.rect = self.image.get_rect(**kwargs)
    
    def update(self):
        pass

            


    
