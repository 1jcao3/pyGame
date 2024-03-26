import pygame
from modelo import avatar
import Constantes
enemigo_x = 600  # Posición inicial del muñeco enemigo
enemigo_y = 400  # Posición inicial del muñeco enemigo  
vel_enemigo = 1
class Enemigo:

  def enemigo():
  
   enemigo1 = pygame.image.load('myGame/imgs/mostruo1.png')
   enemigosR=enemigo1.get_rect(center=(enemigo_x// 2, enemigo_y // 2))
   enemigos=[enemigo1]
   enemigosRR=[enemigosR]
   return enemigos,enemigosRR
  
def mover():
    global enemigo_x,enemigo_y
    if enemigo_x < avatar.avatar_x:
      enemigo_x += vel_enemigo
    elif enemigo_x > avatar.avatar_x:
     enemigo_x -= vel_enemigo
    if enemigo_y < avatar.avatar_y:
     enemigo_y += vel_enemigo
    elif enemigo_y > avatar.avatar_y:
     enemigo_y -= vel_enemigo

    return enemigo_x,enemigo_y