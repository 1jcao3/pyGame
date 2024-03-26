import Constantes
import pygame
class Niveles:
 def niveles():
    # Pintando
    Constantes.ventana.fill(Constantes.NEGRO)
    titulo = Constantes.fuente2.render("Selecciona el nivel", True, Constantes.BLANCO)
    Constantes.ventana.blit(titulo, (320, 280))
    opcion = Constantes.fuente2.render('Normal', True, Constantes.VERDE)
    opcion2 = Constantes.fuente2.render('Dificil', True, Constantes.ROJO)
    texto_rect = opcion.get_rect(center=(Constantes.ANCHO // 2, 380))  # Coordenadas del rectángulo
    texto_rect2 = opcion2.get_rect(center=(Constantes.ANCHO // 2, 480))  # Coordenadas del rectángulo
    Constantes.ventana.blit(opcion, texto_rect.topleft)  # Blit con las coordenadas del rectángulo
    Constantes.ventana.blit(opcion2, texto_rect2.topleft)  # Blit con las coordenadas del rectángulo
    pygame.display.update()
    return texto_rect, texto_rect2