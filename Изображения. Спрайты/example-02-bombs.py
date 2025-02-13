import os
import sys
import random
import pygame


width, height = 500, 500
size = width, height

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Бомбочки 2.0')

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
boom_image = load_image("boom.png")


class Bomb(pygame.sprite.Sprite):
    def __init__(self, *group):
        # Необходимо вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(*group)
        self.image = bomb_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)

    def update(self, *args):
        self.rect = self.rect.move(random.randrange(2) - 1, random.randrange(2) - 1)

        if not args:
            return

        if args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = boom_image


# группа, содержащая все спрайты
all_sprites = pygame.sprite.Group()

for i in range(20):
    # нам уже не нужно даже имя объекта!
    Bomb(all_sprites)

running = True
while running:
    clock.tick(30)
    all_sprites.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(e)

    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
