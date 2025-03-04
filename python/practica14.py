import pygame
import random

# Inicializa pygame
pygame.init()

# Dimensiones de la pantalla
ANCHO = 600
ALTO = 400
TAM_OBJETO = 30
TAM_JUGADOR = 50
COLOR_FONDO = (0, 0, 0)
COLOR_OBJETO = (0, 255, 0)
COLOR_JUGADOR = (255, 0, 0)
COLOR_TEXTO = (255, 255, 255)

# Configura la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Atrapados")
reloj = pygame.time.Clock()

# Clase del objeto que cae
class Objeto:
    def __init__(self):
        self.x = random.randint(0, ANCHO - TAM_OBJETO)
        self.y = -TAM_OBJETO
        self.velocidad = random.randint(2, 5)

    def mover(self):
        self.y += self.velocidad

    def dibujar(self):
        pygame.draw.rect(pantalla, COLOR_OBJETO, (self.x, self.y, TAM_OBJETO, TAM_OBJETO))

# Clase del jugador
class Jugador:
    def __init__(self):
        self.x = ANCHO // 2 - TAM_JUGADOR // 2
        self.y = ALTO - TAM_JUGADOR - 10
        self.velocidad = 5

    def mover(self, tecla):
        if tecla[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velocidad
        if tecla[pygame.K_RIGHT] and self.x < ANCHO - TAM_JUGADOR:
            self.x += self.velocidad

    def dibujar(self):
        pygame.draw.rect(pantalla, COLOR_JUGADOR, (self.x, self.y, TAM_JUGADOR, TAM_JUGADOR))

# Función principal del juego
def main():
    jugador = Jugador()
    objetos = [Objeto()]
    puntuacion = 0
    vidas = 3
    font = pygame.font.SysFont("Arial", 24)

    while vidas > 0:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

        tecla = pygame.key.get_pressed()
        jugador.mover(tecla)

        # Crear nuevos objetos
        if random.random() < 0.02:
            objetos.append(Objeto())

        # Mover objetos
        for objeto in objetos:
            objeto.mover()
            # Si el objeto llega al fondo sin ser atrapado
            if objeto.y > ALTO:
                objetos.remove(objeto)
                vidas -= 1  # Pierdes una vida
            # Verificar si el jugador ha atrapado un objeto
            if (jugador.x < objeto.x + TAM_OBJETO and jugador.x + TAM_JUGADOR > objeto.x) and \
               (jugador.y < objeto.y + TAM_OBJETO and jugador.y + TAM_JUGADOR > objeto.y):
                objetos.remove(objeto)
                puntuacion += 1  # Ganar puntos por atrapar un objeto

        # Dibujar fondo
        pantalla.fill(COLOR_FONDO)

        # Dibujar objetos y jugador
        for objeto in objetos:
            objeto.dibujar()
        jugador.dibujar()

        # Mostrar puntuación y vidas
        texto_puntuacion = font.render(f"Puntuación: {puntuacion}", True, COLOR_TEXTO)
        pantalla.blit(texto_puntuacion, (10, 10))

        texto_vidas = font.render(f"Vidas: {vidas}", True, COLOR_TEXTO)
        pantalla.blit(texto_vidas, (ANCHO - 100, 10))

        pygame.display.update()
        reloj.tick(60)

    # Mostrar mensaje de Game Over
    pantalla.fill(COLOR_FONDO)
    texto_game_over = font.render("¡Game Over!", True, COLOR_TEXTO)
    texto_puntuacion_final = font.render(f"Puntuación final: {puntuacion}", True, COLOR_TEXTO)
    pantalla.blit(texto_game_over, (ANCHO // 2 - 100, ALTO // 2 - 30))
    pantalla.blit(texto_puntuacion_final, (ANCHO // 2 - 150, ALTO // 2 + 30))
    pygame.display.update()
    pygame.time.wait(2000)

    pygame.quit()

# Ejecutar el juego
if __name__ == "__main__":
    main()
