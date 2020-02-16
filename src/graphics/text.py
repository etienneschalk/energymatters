
import pygame 

import config.config as config


class TextHandler:
    def __init__(self):
        self.font = {}
        self.font[11] = pygame.font.Font(config.fonts["font_name"], 11)
        self.font[22] = pygame.font.Font(config.fonts["font_name"], 22)

    
    def create_float_text(self, text, x, y, group):
        group.add(FloatText(self.get_text_surface(text), x, y))


    def get_text_surface(self, text, size=config.fonts["default_size"],
                        color=config.fonts["default_color"],
                        antialiazed=config.fonts["default_antialiazed"]):
        return self.font[size].render(text, antialiazed, color)


class FloatText(pygame.sprite.Sprite):
    def __init__(self, rendered_text, x, y, lifetime=30, decrease_lifetime=1, dy=2):
        super().__init__()

        self.lifetime = lifetime
        self.decrease_lifetime = decrease_lifetime
        self.dy = dy

        self.image = rendered_text
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y


    def update(self):
        self.lifetime -= self.decrease_lifetime
        self.rect.y -= self.dy
        if self.lifetime < 0:
            self.kill()
