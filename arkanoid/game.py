import pygame as pg
from arkanoid import ALTO, ANCHO
from arkanoid.escenas import Portada, Partida, Records

pg.init()

# simplemente va a coordinar las escenas / dirección 

class Game():
    def __init__(self):
        pantalla = pg.display.set_mode((ANCHO,ALTO))
        self.escenas = [Portada(pantalla), Partida(pantalla), Records(pantalla)] # escenas puede ser screen o cualquier cosa pertenece a la clase game

    def launch(self):
        i=0

        while True: # buscle infinito
            self.escenas[i].bucle_principal()
            i += 1
            if i == len(self.escenas):
                i = 0
            # i = (i + 1) % len(self.escenas) - lo mismo que las 3 líneas anteriores 