import pygame


pygame.init()

size = 300, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Герой двигается')

creature_image = pygame.image.load('data/creature.png')
x, y = 0, 0

clock = pygame.time.Clock()

running = True

while running:
    screen.fill((255, 255, 255))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x += 10
    if keys[pygame.K_LEFT]:
        x -= 10
    if keys[pygame.K_UP]:
        y -= 10
    if keys[pygame.K_DOWN]:
        y += 10

    screen.blit(creature_image, (x, y))
    pygame.display.flip()
    clock.tick(20)

pygame.quit()
