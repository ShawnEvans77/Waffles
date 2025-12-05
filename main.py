import pygame #type: ignore
import sprite_sheet as ss

pygame.init()

size = width, height = 1000, 800
screen = pygame.display.set_mode(size)

player = pygame.Rect((75, 75, 100, 100))
vel = 5
sprite_sheet_image = pygame.image.load('idle.png').convert_alpha()

run = True

COLOR = (255, 255, 255)
BLACK = (0, 0, 0)

sheet = ss.SpriteSheet(sprite_sheet_image)

animation_list = []
animation_steps = 10
last_update = pygame.time.get_ticks()
animation_cooldown = 75
frame = 0

for i in range(animation_steps):
    animation_list.append(sheet.get_image(i, 32, 32, 3, BLACK))

frame_0 = sheet.get_image(0, 32, 32, 3, BLACK)
frame_1 = sheet.get_image(1, 32, 32, 3, BLACK)
frame_2 = sheet.get_image(2, 32, 32, 3, BLACK)

while run:

    screen.fill(COLOR)

    #update animation
    current_time = pygame.time.get_ticks()

    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time

        if frame >= len(animation_list):
            frame = 0

    screen.blit(animation_list[frame], (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()