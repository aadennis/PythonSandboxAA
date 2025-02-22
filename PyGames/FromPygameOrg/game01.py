# credit - https://www.pygame.org/docs/
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("cyan")

    # RENDER YOUR GAME HERE

    pygame.display.flip()

    clock.tick(30)  

pygame.quit()