import pygame
import logging
import config.config as config

from inputs.inputs import EventName, MouseButton, InputHandler
from graphics.camera import Camera
from graphics.drawer import Drawer
from graphics.text import TextHandler, FloatText
from .controller import Controller

log = logging.getLogger(__name__)


class Game:


    def _pygame_init(self, sound=False):
        pygame.init()
        pygame.display.set_caption("Energy Matters")
        self.screen = pygame.display.set_mode(
            (0 , 0), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)
        # self.screen = pygame.display.set_mode(
            # (640, 480), pygame.HWSURFACE | pygame.DOUBLEBUF)
        log.info(f"Screen size: {self.screen.get_size()}")
        self.screen_width, self.screen_height = self.screen.get_size()
        self.game_surface = pygame.Surface([self.screen.get_size()[0], self.screen.get_size()[0]])
        self.clock = pygame.time.Clock()


    def __init__(self):
        self._pygame_init()
        self.input_handler = InputHandler()
        self.drawer = Drawer(self.screen)
        self.camera = Camera(self.drawer, self.screen_width, self.screen_height)

        self.input_handler.add_subscriber(EventName.QUIT, self)
        self.input_handler.add_subscriber(EventName.ESCAPE, self)
        self.input_handler.add_subscriber(EventName.SPACE, self)
        self.input_handler.add_subscriber(EventName.RETURN, self)
        self.input_handler.add_subscriber(EventName.UP, self)
        self.input_handler.add_subscriber(EventName.DOWN, self)
        self.input_handler.add_subscriber(EventName.LEFT, self)
        self.input_handler.add_subscriber(EventName.RIGHT, self)
        self.input_handler.add_subscriber(EventName.MOUSEMOTION, self)
        self.input_handler.add_subscriber(EventName.MOUSEMOTIONUP, self)
        self.input_handler.add_subscriber(EventName.MOUSEBUTTONUP, self)
        self.input_handler.add_subscriber(EventName.MOUSEBUTTONDOWN, self)

        self.running = True

        self.rickmorty = pygame.image.load("assets/images/rickmorty3.jpeg")
        # .convert_alpha()
        self.transformrick = 0

        self.startx = 0
        self.starty = 0
        self.screen.fill(0xeeeeee)
        self.game_surface.fill(0xaaaaaa)
        pygame.draw.rect(self.game_surface, 0xffffff, (10, 50, 100, 200))
        pygame.draw.rect(self.game_surface, 0xff0000, (50, 60, 10, 20))
        self.game_surface.blit(self.rickmorty, (0, 0))


    def update(self):
        self.drawer.update_sprites()
        pass 


    def draw(self):
        self.drawer.draw()
        # self.screen.fill(0xeeeeee)
        # self.game_surface.fill(0xaaaaaa)
        # pygame.draw.rect(self.game_surface, 0xffffff, (10, 50, 100, 200))
        # pygame.draw.rect(self.game_surface, 0xff0000, (50, 60, 10, 20))
        # self.game_surface.blit(self.rickmorty, (0, 0))
        # self.screen.blit(self.game_surface, (self.startx, self.starty))
        # pygame.display.flip()
        pass 

    
    def run(self):
        while self.running:
            self.clock.tick(30)
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         self.running=False
            self.input_handler.process_events()
            self.update()
            self.draw()
        log.info("Exiting the Game.run() loop")
        pygame.quit()

    def input_update(self, event_type, event_attributes):
        if event_type == EventName.QUIT:
            self.running = False
        elif event_type == EventName.ESCAPE:
            self.running = False
        elif event_type == EventName.MOUSEBUTTONDOWN:
            
            message = repr(event_attributes) \
            + " | grid_offset_x: " + str(self.drawer.grid_offset_x) \
            + " | grid_offset_y: " + str(self.drawer.grid_offset_y)
            self.drawer.create_float_text(
                message,  event_attributes['pos'][0],  event_attributes['pos'][1])

            message = repr(self.camera) + \
                str(self.camera.get_tile_coords_from_click(*event_attributes['pos']))
            self.drawer.create_float_text(
                message,  event_attributes['pos'][0],  event_attributes['pos'][1] - 40)
            # pass
            log.info(event_attributes)
            if event_attributes['button'] == MouseButton.LEFT.value:   # Left click
                log.info("transofrm")
                self.transformrick = 1
                pass
            elif event_attributes['button'] == MouseButton.RIGHT.value:  # Right click
                pass
            elif event_attributes['button'] == MouseButton.SCROLLUP.value:   # Scroll up
                
                self.camera.zoomIn()

                #Test without camera
                # new_rect = [self.game_surface.get_rect(
                # )[0] * 2, self.game_surface.get_rect()[1] * 2]
                # self.game_surface = pygame.transform.smoothscale(
                #     self.game_surface, [200, 200])
            elif event_attributes['button'] == MouseButton.SCROLLDOWN.value:  # Scroll down

                
                self.camera.zoomOut()

                #Test without camera
                # new_rect = [self.game_surface.get_rect(
                # )[0] * 2, self.game_surface.get_rect()[1] * 2]
                # self.game_surface = pygame.transform.smoothscale(
                #     self.game_surface, [400, 400])
        elif event_type == EventName.MOUSEMOTION:
            log.info(event_attributes['buttons'])
            log.info(MouseButton.LEFT.value)
            log.info(event_attributes['buttons'][MouseButton.LEFT.value])
            if event_attributes['buttons'][MouseButton.LEFT_MOTION.value]:
                self.camera.translate(*event_attributes['rel']) # Unpacking the coords tuple

