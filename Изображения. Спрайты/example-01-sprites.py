import os
import sys
import random
import pygame


width, height = 500, 500
size = width, height

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Бомбочки 1.0')

clock = pygame.time.Clock()


def load_image(name, colorkey=None):
    fullname = f'data/{name}'

    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)
    if colorkey is None:
        image = image.convert_alpha()
    else:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)

    return image


bomb_image = load_image("bomb.png")

# группа, содержащая все спрайты
all_sprites = pygame.sprite.Group()

for i in range(50):
    # можно сразу создавать спрайты с указанием группы
    bomb = pygame.sprite.Sprite(all_sprites)
    bomb.image = bomb_image
    bomb.rect = bomb.image.get_rect()

    # задаём бомбочке случайное местоположение
    bomb.rect.x = random.randrange(width)
    bomb.rect.y = random.randrange(height)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
