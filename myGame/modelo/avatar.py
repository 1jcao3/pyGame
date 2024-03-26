import pygame
import Constantes


bolas_de_fuego = []
avatar_x = 100
avatar_y = 100
velocidadx = 0
velocidady = 0
class Avatar:
 

 
    def avatar():
        return pygame.image.load('myGame/imgs/muneco.png')
    def fuego():
        

        return pygame.image.load('myGame/imgs/fuego.png')


def mover(key):

        global avatar_x,velocidadx,avatar_y,velocidady

       
           
        
        if key == pygame.K_LEFT:
                velocidadx = -5
        elif key == pygame.K_RIGHT:
                velocidadx = 5
        elif key == pygame.K_UP:
                velocidady = -5
        elif key == pygame.K_DOWN:
                velocidady = 5

                
        elif key == pygame.K_LEFT and velocidadx < 0:
                    velocidadx = 0
        elif key == pygame.K_RIGHT and velocidadx > 0:
                    velocidadx = 0
        elif key == pygame.K_UP and velocidady < 0:
                    velocidady = 0
        elif key == pygame.K_DOWN and velocidady > 0:
                    velocidady = 0

        avatar_x += velocidadx
        avatar_y += velocidady

        if avatar_x < 0:
            avatar_x = 0
        elif avatar_x > Constantes.ANCHO - Avatar.avatar().get_width():
           avatar_x = Constantes.ANCHO -Avatar.avatar().get_width()
        if avatar_y < 0:
            avatar_y = 0
        elif avatar_y > Constantes.ALTO - Avatar.avatar().get_height():
            avatar_y = Constantes.ALTO - Avatar.avatar().get_height()

        pygame.display.update()
        return avatar_x, avatar_y


def lanzar():

  bolas_de_fuego.append((avatar_x + 50, avatar_y + 25))


def mover_bolas_de_fuego(enemigos):
        for index, bola in enumerate(bolas_de_fuego):
            bolas_de_fuego[index] = (bola[0] + 5, bola[1])
            
            
            enemigoFoto,enemigosR=enemigos
            
            for enemigo_rect in enemigosR:
             
             if enemigo_rect.collidepoint(bola[0], bola[1]):


              return True  # Indicar que se ha detectado una colisión
        return False  # Indicar que no se ha detectado ninguna colisión

         
def dibujar_bolas_de_fuego():
     fuegos=Avatar.fuego()
     for bola in bolas_de_fuego:   
         
      Constantes.ventana.blit(fuegos,bola)


