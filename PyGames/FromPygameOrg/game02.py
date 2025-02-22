# credit - https://www.pygame.org/docs/
# draw a circle on a screen and move it with
# s,w,d,a keys.
import pygame

DIST_TO_MOVE = 300 

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    # s: down, w: up, d: right, a: left 
    if keys[pygame.K_w]:
        player_pos.y -= DIST_TO_MOVE * dt
    if keys[pygame.K_s]:
        player_pos.y += DIST_TO_MOVE * dt
    if keys[pygame.K_a]:
        player_pos.x -= DIST_TO_MOVE * dt
    if keys[pygame.K_d]:
        player_pos.x += DIST_TO_MOVE * dt

    pygame.display.flip()

    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()