import os
import sys
import pygame


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



pygame.init()

width, height = 800, 800
size = width, height

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Свой курсор мыши')

pygame.mouse.set_visible(False)

cursor_img = load_image("arrow.png")
cursor_img_rect = cursor_img.get_rect()

running = True

while running:
    if pygame.mouse.get_focused():
        cursor_img_rect.topleft = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))
        screen.blit(cursor_img, cursor_img_rect)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
