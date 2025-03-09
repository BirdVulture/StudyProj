import pygame

pygame.init()

width = 400  # Ширина окна
height = 600  # Высота окна
screen = pygame.display.set_mode([width, height])


clock = pygame.time.Clock()  
FPS = 25  

num0 = pygame.image.load("numeral0.png")
num1 = pygame.image.load("numeral1.png")
num2 = pygame.image.load("numeral2.png")
num3 = pygame.image.load("numeral3.png")
bg = pygame.image.load("bg.png")
logo = pygame.image.load("header.png")
ship = pygame.image.load("ship.png")
s = 5
bgx = 0
bgy = 0
logox = 50
logoy = 50
shipx = 150
shipy = 500
numx = 20
numy = 20
fps = 0                         #счетчик фпс
num = 0                          #какое число отрисовывать


game_run = True
while game_run:
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT: 
            game_run = False
        screen.blit(bg, (bgx, bgy))
        screen.blit(logo, (logox, logoy))
        screen.blit(ship, (shipx, shipy))
        if num == 0:
            screen.blit(num0, (numx, numy))
        if num == 1:
            screen.blit(num1, (numx, numy))
        if num == 2:
            screen.blit(num2, (numx, numy))
        if num == 3:
            screen.blit(num3, (numx, numy))
    
    shipy = shipy - s
    if fps > 30:
        num += 1
        fps = 0

    
    pygame.display.flip()

    fps = fps + 1
    clock.tick(FPS)

pygame.quit()