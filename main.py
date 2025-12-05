import pygame #type: ignore

pygame.init()

size = width, height = 1000, 800
screen = pygame.display.set_mode(size)

run = True

player = pygame.Rect((75, 75, 100, 100))

vel = 5

while run:

    color = (255, 255, 255)

    screen.fill(color)

    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] and player.x > 0:
        player.move_ip(-1, 0)
    elif key[pygame.K_RIGHT] and player.x < width - 100:
        player.move_ip(1, 0)
    elif key[pygame.K_UP]:
        player.move_ip(0, -1)
    elif key[pygame.K_DOWN]:
        player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    print(player.y)

    pygame.display.update()

pygame.quit()