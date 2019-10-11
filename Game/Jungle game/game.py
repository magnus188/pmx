import pygame

pygame.init()
canvas = pygame.display.set_mode((433,258))
pygame.display.set_caption("Game")
bckg = pygame.image.load("background.png")
canvas.blit(bckg, (0,0))


player = pygame.sprite.load("Assets\Character\sprites\idle.gif")
player_x = 200
player_y = 120

canvas.blit(player, (player_x, player_y))
pygame.display.update()

while True:
        for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_Left:
                                player_x = player_x-10
                                canvas.blit(player, (player_x, player_y))

                if e.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()