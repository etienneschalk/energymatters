"""
Handle user input, and notify the observers object which
subscribed to the corresponding events.

Act as a bridge between pygame events, and game logic
"""

import pygame
import logging
from enum import Enum


log = logging.getLogger(__name__)


class Camera:
    def __init__(self, drawer, screen_width, screen_height):
        self.drawer = drawer
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.scale = 32
        # self.scale = 1
        self.x = 0
        self.y = 0

        self.tile_x = 0
        self.tile_y = 0

    def set_drawer(self, drawer):
        self.drawer = drawer
        

    def zoomIn(self, amount=1):
        log.info(f"scale in of {amount} / {self.scale}")
        log.info(self)

        self.drawer.tilesize += 4

        self.scale = self.drawer.tilesize
        # if self.scale > 0.1:
        #     self.scale = self.scale / (1.5 ** amount)


    def zoomOut(self, amount=1):
        log.info(f"scale Out of {amount} / {self.scale}")
        log.info(self)

        if self.drawer.tilesize > 4:
            self.drawer.tilesize -= 4
            self.scale = self.drawer.tilesize

        # if self.scale < 512:
        #     self.scale = self.scale * (1.5 ** amount)


    def translate(self, dx, dy):
        log.info(self)
        self.x += dx 
        self.y += dy 

        # self.drawer.canvas_pos_x += dx
        # self.drawer.canvas_pos_y += dy
        self.drawer.grid_offset_x += dx 
        self.drawer.grid_offset_y += dy 

        self.tile_x = self.x // self.scale
        self.tile_y = self.y // self.scale
    

    def get_tile_coords_from_click(self, pos_x, pos_y):
        return ((pos_x - self.x) // self.scale, (pos_y - self.y) // self.scale)


    def __repr__(self):
        return f"<Camera (x: {self.x}, y: {self.y}, tile_x: {self.tile_x}, tile_y: {self.tile_y}, scale: {self.scale})>"

