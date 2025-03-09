import pygame

pygame.init()
# Код, описывающий окно программы
width = 400  # Ширина окна
height = 600  # Высота окна
screen = pygame.display.set_mode([width, height])

# Создаём контроль FPS
clock = pygame.time.Clock()  # Создаём таймер
FPS = 30  # Устанавливаем нужное значение FPS

# Игровые переменные, если надо, описываем в этом блоке
bg = pygame.image.load("bg.png")


# Игровой цикл и флаг выполнения программы
game_run = True
while game_run:
    # БЛОК ОБРАБОТКИ СОБЫТИЙ ИГРЫ
    for i in pygame.event.get():
        if i.type == pygame.QUIT:  # Закрыли окно?
            game_run = False
    screen.blit(bg, (0, 0))
    # БЛОК ИГРОВОЙ ЛОГИКИ
    # ... тут размещаем все вычисления ...

    # БЛОК ОТРИСОВКИ ОБЪЕКТОВ В ОКНЕ ПРОГРАММЫ
    # ... тут закрашиваем фон и рисуем все объекты программы ...

    # Отображение нарисованных объектов
    pygame.display.flip()

    # Контроль FPS
    clock.tick(FPS)

pygame.quit()

