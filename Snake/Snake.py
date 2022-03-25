"""
Увлекательная игра - "змейка на двоих" )))
клавиши управления:
Игрок №1 Вверх, Вниз, Влево, Вправо
Игрок №2 W, A, S, D
Space - пауза
Старт для каждой змеи - любая клавиша управления
"""


from gameActors import Snake
from random import randrange
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

FPS = 12 # Скорость
VOLUME = 20  # Размер клетки/длина шага
WIDTH, HIGHT = VOLUME * 60, VOLUME * 40  # Масштабируем окно по разменру клетки на возможное количество шагов
BLACK, WHITE, RED, GREEN, BLUE, YELLOW, MAGENTA = (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), \
                                                  (0, 0, 255), (230, 223, 0), (162, 107, 246)
COUNT_APPLES = 10
count_snakes = 2
speed = 1 # Множитель скорости
apples = []
snakes = []

screen = pygame.display.set_mode((WIDTH, HIGHT))
clock = pygame.time.Clock()

snakes.append(Snake(WIDTH, HIGHT, VOLUME, GREEN))
snakes.append(Snake(WIDTH, HIGHT, VOLUME, MAGENTA))
game_run = True


def get_position():
    coordinates = randrange(0, WIDTH, VOLUME), randrange(0, HIGHT, VOLUME)

    if coordinates not in apples:
        for i in range(count_snakes):
            if (coordinates in snakes[i].bodyPosition):
                return get_position()
    return coordinates


def colorize(color, position):
    pygame.draw.rect(screen, color, (*position, VOLUME, VOLUME))

def addApple(count):
    """Добавляет на поле нужное количество яблок
        проверяет, что бы яблоко не попало на тело змеи или другое яблоко
        записывает координаты в список и расскрашивает клетки в красный"""

    coordinates = get_position()
    apples.append(coordinates)
    colorize(RED, coordinates)
    if count > 1:
        addApple(count - 1)
    return

def choosingADirection():

    pressedKeys = pygame.key.get_pressed()
    if pressedKeys[pygame.K_UP] and not snakes[0].direction == "DOWN":
        snakes[0].direction = "UP"
    if pressedKeys[pygame.K_DOWN] and not snakes[0].direction == "UP":
        snakes[0].direction = "DOWN"
    if pressedKeys[pygame.K_LEFT] and not snakes[0].direction == "RIGHT":
        snakes[0].direction = "LEFT"
    if pressedKeys[pygame.K_RIGHT] and not snakes[0].direction == "LEFT":
        snakes[0].direction = "RIGHT"
    if pressedKeys[pygame.K_SPACE]:
        snakes[0].direction = "STOP"

    if pressedKeys[pygame.K_w] and not snakes[1].direction == "DOWN":
        snakes[1].direction = "UP"
    if pressedKeys[pygame.K_s] and not snakes[1].direction == "UP":
        snakes[1].direction = "DOWN"
    if pressedKeys[pygame.K_a] and not snakes[1].direction == "RIGHT":
        snakes[1].direction = "LEFT"
    if pressedKeys[pygame.K_d] and not snakes[1].direction == "LEFT":
        snakes[1].direction = "RIGHT"
    if pressedKeys[pygame.K_SPACE]:
        snakes[1].direction = "STOP"


addApple(COUNT_APPLES)
while game_run: # Главный цикл

    headPosition0 = (int(snakes[0].headPosition_x), int(snakes[0].headPosition_y))
    headPosition1 = (int(snakes[1].headPosition_x), int(snakes[1].headPosition_y))

    choosingADirection()
    colorize(WHITE, headPosition0) # Основное тело змеи красим белым
    colorize(WHITE, headPosition1) # в том числе клетку, которая была зеленой(головой)
                                    # на прошлой итерации
    score = str()
    pygame.display.set_caption(str(snakes[0].bodyLenght) + " / " + str(snakes[1].bodyLenght))
    for snake in snakes:
        snake.move()
        headPosition = snake.bodyPosition[-1]
        colorize(snake.color, headPosition)# Голова
        if headPosition in apples: # Встреча с яблоком
            apples.pop(apples.index(headPosition)) # Удаляем из списка съеденное яблоко
            snake.bodyLenght += 1 # После яблока добавляется длина тела
            addApple(1)# Создаем новое яблоко вместо съеденного
        colorize(BLACK, snake.bodyPosition[0])#Закрашиваем черным
                                                # освободившуюся после шага клетку
    pygame.display.flip()
    clock.tick(FPS * speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game_run = False
            break