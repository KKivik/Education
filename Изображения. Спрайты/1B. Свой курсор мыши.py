import pygame


pygame.init()

width, height = 800, 800
size = width, height

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Свой курсор мыши')

arrow_image = pygame.image.load('data/arrow.png')
pygame.mouse.set_cursor((0, 0), arrow_image)

pygame.display.flip()

running = True

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

pygame.quit()
