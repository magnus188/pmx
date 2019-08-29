import pygame

pygame.init()
canvas = pygame.display.set_mode((500,250))
pygame.display.set_caption("Game")
canvas.fill((255,0,0))

done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()