import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Размеры экрана и ячейки
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 30
CELL_GAP = 1

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Map Editor")

# Создание карты
rows = HEIGHT // (CELL_SIZE + CELL_GAP)
cols = WIDTH // (CELL_SIZE + CELL_GAP)
level = [[0] * cols for _ in range(rows)]

# Переменная для отслеживания рисования
drawing = False

def draw_grid():
    for row in range(rows):
        for col in range(cols):
            color = WHITE if level[row][col] == 0 else BLACK
            pygame.draw.rect(screen, color, (col * (CELL_SIZE + CELL_GAP), row * (CELL_SIZE + CELL_GAP), CELL_SIZE, CELL_SIZE))

def save_map(filename):
    with open(filename, 'w') as file:
        for row in level:
            file.write(','.join(map(str, row)) + '\n')

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                x, y = event.pos
                col = x // (CELL_SIZE + CELL_GAP)
                row = y // (CELL_SIZE + CELL_GAP)
                level[row][col] = 1

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save_map('custom_map.txt')

    screen.fill(WHITE)
    draw_grid()

    pygame.display.flip()

pygame.quit()
sys.exit()
