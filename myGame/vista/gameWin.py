import Constantes
import pygame
class GameWin:
 

 def gameWin():
    # Pintando
    Constantes.ventana.fill(Constantes.NEGRO)
    titulo = Constantes.fuente.render("Ganaste", True, Constantes.BLANCO)
    Constantes.ventana.blit(titulo, (310, 280))
    opcion = Constantes.fuente2.render('volver a jugar', True, Constantes.VERDE)
    opcionR = opcion.get_rect(center=(Constantes.ANCHO // 2, Constantes.ALTO // 2))
    opcionR.width = opcion.get_width()
    opcionR.height = opcion.get_height()
    Constantes.ventana.blit(opcion, opcionR)
    pygame.display.update()
    return opcionR