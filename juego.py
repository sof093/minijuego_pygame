# Importar módulos necesarios
import pygame
import random
# Inicializar Pygame
pygame.init()
# Configurar la pantalla y el reloj
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# Función para reiniciar el juego con posiciones y velocidades iniciales
def reiniciar_juego():
    return (
        [10, 10], [100, 100],
        [480, 480], [-100, -100],
        [480, 10], [-100, 100],
        [10, 480], [100, -100],
        [55, 55], [230, 122],
        [250, 10], [-100, 100],
        [random.randint(0, 490), random.randint(0, 490)], [0, 0]  # Posición aleatoria del cuadrado naranja
    )
# Inicializar posiciones y velocidades
pos, vel, pos_1, vel_1, pos_2, vel_2, pos_3, vel_3, pos_4, vel_4, pos_5, vel_5, pos_center, vel_center = reiniciar_juego()
# Tamaños y posiciones iniciales de los elementos en pantalla
ancho = 10
alto = 10

ancho_1 = 10
alto_1 = 10

ancho_2 = 10
alto_2 = 10

ancho_3 = 10
alto_3 = 10

ancho_4 = 10
alto_4 = 10

ancho_center = 10
alto_center = 10

ancho_rosa = 20
alto_rosa = 20
pos_rosa = [250, 250]
# Configuración inicial de la puntuación y otras variables
contador = 0
puntuacion = 0  # Nueva variable de puntuación

running = True
colision = False
# Bucle principal del juego
while running:
    dt = clock.tick(60)
    dt = dt / 1000
    contador += dt
    # Manejo de eventos de Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Manejo de teclas presionadas
            if not colision:
                if event.key == pygame.K_LEFT:
                    vel_center[0] = -100
                elif event.key == pygame.K_RIGHT:
                    vel_center[0] = 100
                elif event.key == pygame.K_UP:
                    vel_center[1] = -100
                elif event.key == pygame.K_DOWN:
                    vel_center[1] = 100
            elif colision and event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                # Reiniciar juego y reiniciar puntuación
                colision = False
                pos, vel, pos_1, vel_1, pos_2, vel_2, pos_3, vel_3, pos_4, vel_4, pos_5, vel_5, pos_center, vel_center = reiniciar_juego()
                puntuacion = 0

        elif event.type == pygame.KEYUP:
            # Manejo de teclas liberadas
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                vel_center[0] = 0
            elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                vel_center[1] = 0
    # Lógica del juego
    if not colision:
        pos_center[0] += vel_center[0] * dt
        pos_center[1] += vel_center[1] * dt

        pos_center[0] = max(min(pos_center[0], 500 - ancho_center), 0)
        pos_center[1] = max(min(pos_center[1], 500 - alto_center), 0)

        screen.fill("red")

        pos[0] += vel[0] * dt
        pos[1] += vel[1] * dt

        pos_1[0] += vel_1[0] * dt
        pos_1[1] += vel_1[1] * dt

        pos_2[0] += vel_2[0] * dt
        pos_2[1] += vel_2[1] * dt

        pos_3[0] += vel_3[0] * dt
        pos_3[1] += vel_3[1] * dt

        if contador >= 5:
            vel_4[0] = random.randint(50, 250)
            vel_4[1] = random.randint(50, 250)
            contador = 0

        pos_4[0] += vel_4[0] * dt
        pos_4[1] += vel_4[1] * dt

        pos_5[0] += vel_5[0] * dt
        pos_5[1] += vel_5[1] * dt

        if (
            pos_center[0] < (pos[0] + ancho) and (pos_center[0] + ancho_center) > pos[0] and
            pos_center[1] < (pos[1] + alto) and (pos_center[1] + alto_center) > pos[1]
        ):
            print("Colisión con cuadrado negro")
            colision = True
        elif (
            pos_center[0] < (pos_1[0] + ancho_1) and (pos_center[0] + ancho_center) > pos_1[0] and
            pos_center[1] < (pos_1[1] + alto_1) and (pos_center[1] + alto_center) > pos_1[1]
        ):
            print("Colisión con cuadrado blanco")
            colision = True
        elif (
            pos_center[0] < (pos_2[0] + ancho_2) and (pos_center[0] + ancho_center) > pos_2[0] and
            pos_center[1] < (pos_2[1] + alto_2) and (pos_center[1] + alto_center) > pos_2[1]
        ):
            print("Colisión con cuadrado azul")
            colision = True
        elif (
            pos_center[0] < (pos_3[0] + ancho_3) and (pos_center[0] + ancho_center) > pos_3[0] and
            pos_center[1] < (pos_3[1] + alto_3) and (pos_center[1] + alto_center) > pos_3[1]
        ):
            print("Colisión con cuadrado verde")
            colision = True
        elif (
            pos_center[0] < (pos_4[0] + ancho_4) and (pos_center[0] + ancho_center) > pos_4[0] and
            pos_center[1] < (pos_4[1] + alto_4) and (pos_center[1] + alto_center) > pos_4[1]
        ):
            print("Colisión con cuadrado amarillo")
            colision = True
        elif (
            pos_center[0] < (pos_5[0] + ancho) and (pos_center[0] + ancho_center) > pos_5[0] and
            pos_center[1] < (pos_5[1] + alto) and (pos_center[1] + alto_center) > pos_5[1]
        ):
            print("Colisión con cuadrado morado")
            colision = True

        if (
            pos_center[0] < (pos_rosa[0] + ancho_rosa) and (pos_center[0] + ancho_center) > pos_rosa[0] and
            pos_center[1] < (pos_rosa[1] + alto_rosa) and (pos_center[1] + alto_center) > pos_rosa[1]
        ):
            print("Colisión con cuadrado rosa")
            puntuacion += 5  # Incrementar la puntuación al atrapar el cuadrado rosa
            pos_rosa = [random.randint(0, 490), random.randint(0, 490)]  # Cambiar posición aleatoria del cuadrado rosa
            contador = 0  # Reiniciar el contador para actualizar la posición cada vez que se toque

        if pos[0] + ancho > 500 or pos[0] < 0:
            vel[0] *= -1

        if pos[1] + alto > 500 or pos[1] < 0:
            vel[1] *= -1

        if pos_1[0] + ancho_1 > 500 or pos_1[0] < 0:
            vel_1[0] *= -1

        if pos_1[1] + alto_1 > 500 or pos_1[1] < 0:
            vel_1[1] *= -1

        if pos_2[0] + ancho_2 > 500 or pos_2[0] < 0:
            vel_2[0] *= -1

        if pos_2[1] + alto_2 > 500 or pos_2[1] < 0:
            vel_2[1] *= -1

        if pos_3[0] + ancho_3 > 500 or pos_3[0] < 0:
            vel_3[0] *= -1

        if pos_3[1] + alto_3 > 500 or pos_3[1] < 0:
            vel_3[1] *= -1

        if pos_4[0] + ancho_4 > 500 or pos_4[0] < 0:
            vel_4[0] *= -1

        if pos_4[1] + alto_4 > 500 or pos_4[1] < 0:
            vel_4[1] *= -1

        if pos_5[0] + ancho > 500 or pos_5[0] < 0:
            vel_5[0] *= -1

        if pos_5[1] + alto > 500 or pos_5[1] < 0:
            vel_5[1] *= -1
        # ... (repetir para otros elementos)
        pygame.draw.rect(screen, "black", (pos[0], pos[1], ancho, alto))
        pygame.draw.rect(screen, "white", (pos_1[0], pos_1[1], ancho_1, alto_1))
        pygame.draw.rect(screen, "blue", (pos_2[0], pos_2[1], ancho_2, alto_2))
        pygame.draw.rect(screen, "green", (pos_3[0], pos_3[1], ancho_3, alto_3))
        pygame.draw.rect(screen, "yellow", (pos_4[0], pos_4[1], ancho_4, alto_4))
        pygame.draw.rect(screen, "purple", (pos_5[0], pos_5[1], ancho, alto))
        pygame.draw.rect(screen, "white", (pos_center[0], pos_center[1], ancho_center, alto_center))
        pygame.draw.rect(screen, "pink", (pos_rosa[0], pos_rosa[1], ancho_rosa, alto_rosa))

        # Mostrar puntuación en la pantalla
        font = pygame.font.Font(None, 36)
        text = font.render(f"Puntuación: {puntuacion}", True, (255, 255, 255
                                                               ))
        text_rect = text.get_rect(center=(250, 20))
        screen.blit(text, text_rect)

    else:  # Mensaje de colisión
        font = pygame.font.Font(None, 36)
        text = font.render("Presiona una tecla de mover para reiniciar.", True, (255, 255, 255))
        text_rect = text.get_rect(center=(250, 250))
        screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
