import pygame as pg
from . import FPS, ANCHO, ALTO #el punto indica al módulo al que pertece, en este caso arkanoid
from .entidades import Raqueta, Bola, Ladrillo, Marcador
import random

class Escena():
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        pass

class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla) #va a la calse padre, va al init del padre que es __init__ de la calse Escena
        # Escena.__init__(sef,pantalla) = super.()...
       
        self.logo = pg.image.load("resources/images/arkanoid_name.png")
        
        fuente = pg.font.Font("resources/fonts/LibreFranklin-VariableFont_wght.ttf", 28) #variable de usar y tirar (con self estará guardada)
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
        super().__init__(pantalla) #siempre queremos que ejecute el init del padre, no repetimos código
        self.fondo = pg.image.load("resources/images/background.jpg")
        self.player = Raqueta(midbottom=(ANCHO // 2, ALTO - 15))
        self.bola = Bola(center=(ANCHO // 2, ALTO // 2))
        self.cuenta_vidas = Marcador(10, 10, "CabinSketch-Bold.ttf", 24, (240,210,6))

        self.todos = pg.sprite.Group()
        self.ladrillos = pg.sprite.Group()
    
    def reset(self):
        self.vidas = 3
        self.puntos = 0

        self.ladrillos.empty()
        self.todos.empty()
        
        self.bola.reset()
        self.player.reset()
        
        for f in range (3):
            for c in range(6):
                ladrillo = Ladrillo(c * 90 + 30, f * 30 + 10)
                self.ladrillos.add(ladrillo) 
        
        self.todos.add(self.ladrillos, self.player, self.bola, self.cuenta_vidas)


    def bucle_principal(self):
        self.reset()

        while self.vidas > 0:
            dt = self.reloj.tick(FPS)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()
        
            self.cuenta_vidas.texto = self.vidas
            self.todos.update(dt)

            self.bola.comprobar_choque(self.player)

            tocados = pg.sprite.spritecollide(self.bola, self.ladrillos,True) # devuelve una lisata en casa vuelta/f
            
            # rebotar pelota tras choque 
            if len(tocados) > 0:  
                self.bola.delta_y *= -1
                self.puntos *= len(tocados) * 5

            if not self.bola.viva:
                self.vidas -= 1
                self.bola.viva = True
                self.player.reset()
              
            self.pantalla.blit(self.fondo, (0,0))
            self.todos.draw(self.pantalla)

            pg.display.flip()

class Records(Escena):
    pass 