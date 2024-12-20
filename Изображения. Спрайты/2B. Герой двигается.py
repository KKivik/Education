import pygame


pygame.init()

size = 300, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Герой двигается')

all_sprites = pygame.sprite.Group()

creature = pygame.sprite.Sprite(all_sprites)
creature.image = pygame.image.load('data/creature.png')
creature.rect = creature.image.get_rect()

clock = pygame.time.Clock()

running = True

while running:
    screen.fill((255, 255, 255))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        creature.rect.x += 10
    if keys[pygame.K_LEFT]:
        creature.rect.x -= 10
    if keys[pygame.K_UP]:
        creature.rect.y -= 10
    if keys[pygame.K_DOWN]:
        creature.rect.y += 10

    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(20)

pygame.quit()