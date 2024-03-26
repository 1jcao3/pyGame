import Constantes
import pygame
from modelo import enemigo,avatar
class Juego:

  avatar_x = 100
  avatar_y = 100
  velocidadx=0
  velocidady=0
   

  def juego(key): 
    
     enemigo_o,ene=enemigo.Enemigo.enemigo()
     enemigo_x,enemigo_y=enemigo.mover()
     avatar_o=avatar.Avatar.avatar()
     avatar_x,avatar_y=avatar.mover(key)
     Constantes.ventana.fill(Constantes.NEGRO)
     Constantes.ventana.blit(avatar_o, (avatar_x,avatar_y))
     Constantes.ventana.blit(enemigo_o[0], (enemigo_x, enemigo_y))  # Dibujar el muñeco enemigo
     avatar.dibujar_bolas_de_fuego()
     pygame.display.update()
     pygame.time.delay(10)  # Pequeña pausa para controlar la velocidad de movimiento

