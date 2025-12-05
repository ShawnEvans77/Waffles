import pygame #type: ignore

pygame.init()

size = width, height = 1000, 800

screen = pygame.display.set_mode(size)

run = True

player = pygame.Rect((100, 100, 100, 100))

while run:

    color = (255, 255, 255)

    screen.fill(color)

    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_RIGHT] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_UP] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_DOWN] == True:
        player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()