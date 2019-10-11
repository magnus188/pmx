import pygame
import random

x = 50
y = 10
length = 3
speed = 20

pygame.init()
canvas = pygame.display.set_mode((400,400))

# create snake
for i in range(0,length):
    pygame.draw.rect(canvas, (255,255,255), (x+i*25,200,20,20))

pygame.display.update()


while True:
    


    for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                print(e)

            if e.type == pygame.QUIT:
                    pygame.quit()

    pygame.display.update()