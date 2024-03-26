import pygame
from vista import inicio, juego, niveles, gameWin
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
            if uno.collidepoint(evento.pos):
                opcion_seleccionada = 'juego'
            elif dos.collidepoint(evento.pos):
                opcion_seleccionada = 'juego'

    elif opcion_seleccionada == 'juego':
        if not juego_pausado:
            juego.Juego.juego(evento)
            colision = avatar.mover_bolas_de_fuego(enemigo.Enemigo.enemigo())
            if colision:
                juego_pausado = True
                opcion_seleccionada = "gameWin"

        avatar.mover_bolas_de_fuego(enemigo.Enemigo.enemigo())

    elif opcion_seleccionada == 'gameWin':
        win_rect = gameWin.GameWin.gameWin()  
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if win_rect.collidepoint(evento.pos):
                opcion_seleccionada = 'niveles'
               

# Salir del juego
pygame.quit()
