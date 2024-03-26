import pygame
def salir():

     for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            jugando=False
            pygame.quit() 
        if evento.type==pygame.K_ESCAPE:
            jugando=False
            pygame.quit()   
            return jugando