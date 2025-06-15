import pygame.sprite
import configs
import assets
from objects.block import Block


class Ball(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.image = pygame.transform.scale(assets.get_sprites("ball"), (10, 10))
        self.rect = self.image.get_rect(center=(configs.CIRCLE_X, configs.CIRCLE_Y))
        self.mask = pygame.mask.from_surface(self.image)

        self.mx = 1
        self.my = 1

        super().__init__(*groups)

    def update(self):
        self.rect.x += self.mx
        self.rect.y += self.my

    def check_collisions(self, sprites, sprite=None):
        for sprite in sprites:
            if (type(sprite) is Block) and sprite.mask.overlap(self.mask,
                                                            (self.rect.x - sprite.rect.x, self.rect.y - sprite.rect.y)):
                print("Check")