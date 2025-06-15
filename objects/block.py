import pygame.sprite
import configs
import assets


class Block(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.image = pygame.transform.scale(assets.get_sprites("block"), (configs.CIRCLE_RADIUS, configs.CIRCLE_RADIUS))
        self.image.set_alpha(configs.CIRCLE_OPACITY)
        self.rect = self.image.get_rect(center=(configs.CIRCLE_X, configs.CIRCLE_Y))
        super().__init__(*groups)