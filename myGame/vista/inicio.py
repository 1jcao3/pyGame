import Constantes
import pygame
class Inicio:
 

 def inicio():
    # Pintando
    Constantes.ventana.fill(Constantes.NEGRO)
    titulo = Constantes.fuente.render("OLE", True, Constantes.BLANCO)
    Constantes.ventana.blit(titulo, (350, 280))
    opcion = Constantes.fuente2.render('jugar', True, Constantes.VERDE)
    opcionR = opcion.get_rect(center=(Constantes.ANCHO // 2, Constantes.ALTO // 2))
    Constantes.ventana.blit(opcion, opcionR.topleft)
    pygame.display.update()
    return opcionR