import pygame
import logging

import config.config as config
from core.orientation import Orientation

from .text import TextHandler

log = logging.getLogger(__name__)

class Drawer: 
    def __init__(self, screen):
        self.screen = screen
        self.images = {}
        

        self.canvas = pygame.Surface(self.screen.get_size())

        self._init_images()
        
        self.font_handler = TextHandler()

        # These can be modified by the camera
        self.tilesize = 32
        self.canvas_pos_x = 0
        self.canvas_pos_y = 0
        self.grid_offset_x = 0
        self.grid_offset_y = 0
        

        self.toasts = pygame.sprite.Group()


    def _init_images(self):
        # Initialize images dict, and pre-rotate images
        for element, img_name in config.images.items():
            self.images[element] = {}
            self.images[element][Orientation.Up] = pygame.image.load(
                img_name).convert_alpha()
            self.images[element][Orientation.Left] = pygame.transform.rotate(
                self.images[element][Orientation.Up], Orientation.Left.value)
            self.images[element][Orientation.Down] = pygame.transform.rotate(
                self.images[element][Orientation.Up], Orientation.Down.value)
            self.images[element][Orientation.Right] = pygame.transform.rotate(
                self.images[element][Orientation.Up], Orientation.Right.value)


    def draw_grid(self):
        for x in range(- self.tilesize, self.canvas.get_rect().width, self.tilesize):
            pygame.draw.line(self.canvas, 0xff0000, 
                             (x + self.grid_offset_x % self.tilesize,
                              self.grid_offset_y % self.tilesize - self.tilesize),
                             (x + self.grid_offset_x % self.tilesize, self.canvas.get_rect().height + self.grid_offset_y % self.tilesize))

        for y in range(- self.tilesize, self.canvas.get_rect().height, self.tilesize):
            pygame.draw.line(self.canvas, 0x0000ff, (self.grid_offset_x % self.tilesize - self.tilesize, y + self.grid_offset_y % self.tilesize),
                             (self.canvas.get_rect().width + self.grid_offset_x % self.tilesize, y + self.grid_offset_y % self.tilesize))

        # Repere
        pygame.draw.rect(self.canvas, 0x00ff00,
                         (self.grid_offset_x, self.grid_offset_y, self.tilesize, self.tilesize))
        # for x in range(0, self.canvas.get_rect().width, self.tilesize):
        #     pygame.draw.line(self.canvas, 0x0000ff, (x + self.grid_offset_x, self.grid_offset_y),
        #                      (x + self.grid_offset_x, self.canvas.get_rect().height + self.grid_offset_y))

        # for y in range(0, self.canvas.get_rect().height, self.tilesize):
        #     pygame.draw.line(self.canvas, 0x0000ff, (self.grid_offset_x, y + self.grid_offset_y),
        #                      (self.canvas.get_rect().width + self.grid_offset_x, y + self.grid_offset_y))
        

    def draw_toasts(self):
        self.toasts.draw(self.canvas)

    
    def draw(self):

        self.screen.fill(0xeeeeee)
        self.canvas.fill(0xaaaaff)
        
        pygame.draw.rect(self.canvas, 0xffffff,
                         (0, 0, self.tilesize, self.tilesize))

        self.draw_grid()
        self.draw_toasts()

        self.screen.blit(self.canvas, (self.canvas_pos_x, self.canvas_pos_y))

        pygame.display.flip()


    def draw_text_line(self, x, y, text,
                  size=config.fonts["default_size"],
                  color=config.fonts["default_color"],
                  antialiazed=config.fonts["default_antialiazed"]):

        text_surface = self.font[size].render(
            text, antialiazed, color)  # antialiazed
        text_rect = text_surface.get_rect()
        text_rect = (x, y)
        self.canvas.blit(text_surface, text_rect)


    def draw_text(self, x, y, text, shadow=False):
        lines = text.split("\n")
        offset = 0
        for idx, line in enumerate(lines):
            if shadow:
                self.draw_text_line(x+1, y+1 + offset, line, color=0x000000)
            self.draw_text_line(x, y + offset, line, color=0xffffff)
            offset += 13

    
    def update_sprites(self):
        self.toasts.update()

    
    def create_float_text(self, text, x, y):
        self.font_handler.create_float_text(text, x, y, self.toasts)

