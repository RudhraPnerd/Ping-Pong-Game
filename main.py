import pygame

import assets
import configs
from objects.block import Block
from objects.circle import Circle

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH,configs.SCREEN_HEIGHT ))
clock = pygame.time.Clock()
running = True

assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()

Circle(sprites)
Block(sprites)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(configs.SCREEN_BG_COLOUR)

    sprites.draw(screen)

    pygame.display.flip()

    clock.tick(configs.FPS)

pygame.quit()