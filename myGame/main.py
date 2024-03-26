import pygame
from vista import inicio, juego, niveles, gameWin,gameLost
from modelo import avatar, enemigo

# Inicializar librería
pygame.init()

jugando = True
opcion_seleccionada = None
inicio_rect = inicio.Inicio.inicio()
win_rect = gameWin.GameWin.gameWin()
juego_pausado = False

while jugando:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if opcion_seleccionada is None:
                if inicio_rect.collidepoint(evento.pos):
                    opcion_seleccionada = 'niveles'
        elif evento.type == pygame.KEYDOWN:
            avatar.mover(evento.key)
            if evento.key == pygame.K_x:
                avatar.lanzar()

    if opcion_seleccionada == 'inicio':
        inicio_rect = inicio.Inicio.inicio()  # Actualizar el rectángulo de inicio
       
    elif opcion_seleccionada == 'niveles':
        niveles.Niveles.niveles()
        uno, dos = niveles.Niveles.niveles()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            juego_pausado=False
            if uno.collidepoint(evento.pos):
                opcion_seleccionada = 'juego'
            elif dos.collidepoint(evento.pos):
                opcion_seleccionada = 'juego'

               
    elif opcion_seleccionada == 'gameWin':
        win_rect = gameWin.GameWin.gameWin()  
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if win_rect.collidepoint(evento.pos):
                opcion_seleccionada = 'niveles'

    elif opcion_seleccionada == 'gameLost':
        win_rect = gameLost.GameLost.gameLost()  
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if win_rect.collidepoint(evento.pos):
                opcion_seleccionada = 'niveles'             
                
    elif opcion_seleccionada == 'juego':
        
        
        if not juego_pausado:
            juego.Juego.juego(evento)
            colision = avatar.mover_bolas_de_fuego(enemigo.Enemigo.enemigoR())
            colision2=avatar.perder(enemigo.Enemigo.enemigoR())
            if colision:
                
                juego_pausado = True
                pygame.time.delay(1000)
                opcion_seleccionada = "gameWin"
                pygame.display.update()
                avatar.limpiar()
                enemigo.limpiar()
            if colision2 :    
                juego_pausado = True
                pygame.time.delay(1000)
                opcion_seleccionada = "gameLost"
                pygame.display.update()
                avatar.limpiar()
                enemigo.limpiar()

        avatar.mover_bolas_de_fuego(enemigo.Enemigo.enemigoR())
    
   

# Salir del juego
pygame.quit()
