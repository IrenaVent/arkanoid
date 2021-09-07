import pygame as pg
from pygame.sprite import Sprite
from . import FPS, ANCHO, ALTO

class Raqueta (Sprite):
    disfraces = ["electric00.png", "electric01.png", "electric02.png"]
    def __init__(self, **kwargs):
        super().__init__()
        self.lista_images = []

        for nombre in self.disfraces:
            self.lista_images.append(pg.image.load(f"resources/images/{nombre}"))
        self.imagen_activa = 0

        self.tiempo_trascurrido = 0
        self.tiempo_hasta_cambio_disfraz = 1000//FPS * 5

        self.posicion_inicial = kwargs
        self.image = self.lista_images[self.imagen_activa]
        self.rect = self.image.get_rect(**kwargs)

    def reset(self):
        self.rect = self.image.get_rect(**self.posicion_inicial)

    def update(self, dt):
        if pg.key.get_pressed()[pg.K_LEFT]:
            self.rect.x -= 5
        
        #limite pantalla izrq
        if self.rect.left <= 0:
            self.rect.left = 0

        if pg.key.get_pressed()[pg.K_RIGHT]:
            self.rect.x += 5

        #limite pantalla drcha
        if self.rect.right >= ANCHO:
            self.rect.right = ANCHO
        
        self.tiempo_trascurrido += dt
        if self.tiempo_trascurrido >= self.tiempo_hasta_cambio_disfraz:
            self.imagen_activa += 1
            if self.imagen_activa >= len(self.lista_images):
                self.imagen_activa = 0
            
            self.tiempo_trascurrido = 0
        
        self.image = self.lista_images[self.imagen_activa]

class Bola (Sprite):
    disfraces = "ball1.png"
    def __init__(self, **kwargs):
        super().__init__()
        self.image = pg.image.load(f"resources/images/{self.disfraces}")
        self.rect = self.image.get_rect(**kwargs)
        self.delta_x = 5 # movimiento en x
        self.delta_y = 5 # movimiento en y
        self.viva = True
        self.posicion_inicial = kwargs # alamcenamos la posición 
        
    def update(self, dt):
        self.rect.x += self.delta_x
        if self.rect.x <= 0 or self.rect.right >= ANCHO:
            self.delta_x *= -1

        self.rect.y += self.delta_y
        if self.rect.y <= 0:
            self.delta_y *= -1

        if self.rect.bottom >= ALTO:
            self.viva = False
            self.reset()
    
    def reset(self): # cuando la bola muere/se pierde vida, resetear su posicion
        self.rect = self.image.get_rect(**self.posicion_inicial)
        self.delta_x = 5
        self.delta_y = 5

    def comprobar_choque(self,raqueta):
        if self.rect.right >= raqueta.rect.left and self.rect.left <= raqueta.rect.right and \
            self.rect.bottom >= raqueta.rect.top and self.rect.top <= raqueta.rect.bottom:
            self.delta_y *= -1   

class Ladrillo (Sprite):
    disfraces = "greenTile.png"
    def __init__(self, x=5, y=5):       
        super().__init__() #siempre que herede de sprite y lo vamos a meter en un grupo
        # pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(f"resources/images/{self.disfraces}")
        self.rect = self.image.get_rect(x=x,y=y)

class Marcador (Sprite):
    def __init__(self, x, y, fichero_letra, tamanyo, color):
        super().__init__()
        self._texto = ""
        self.x = x
        self.y = y
        self.color = color
        self.fuente = pg.font.Font(f"resources/fonts/{fichero_letra}", tamanyo)
        self.image = self.fuente.render(self._texto, True, self.color)
        self.rect = self.image.get_rect(x = self.x, y = self.y)
    
    def update(self, dt):
        self.image = self.fuente.render(self._texto, True, self.color)
        self.rect = self.image.get_rect(x = self.x, y = self.y)
    
    @property
    def texto(self):
        return self._texto

    @texto.setter
    def texto(self, valor):
        self._texto = str(valor)