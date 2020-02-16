"""
Handle user input, and notify the observers object which
subscribed to the corresponding events.

Act as a bridge between pygame events, and game logic
"""

import pygame
import logging
from enum import Enum


log = logging.getLogger(__name__)


class MouseButton(Enum):
    LEFT_MOTION = 0 
    MIDDLE_MOTION = 1
    RIGHT_MOTION = 2
    LEFT = 1 
    MIDDLE = 2
    RIGHT = 3
    SCROLLUP = 4
    SCROLLDOWN = 5


class EventName(Enum):
    QUIT = 'QUIT'
    ESCAPE = 'ESCAPE'
    SPACE = 'SPACE'
    RETURN = 'RETURN'
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    MOUSEMOTION = 'MOUSEMOTION'
    MOUSEMOTIONUP = 'MOUSEMOTIONUP'
    MOUSEMOTIONDOWN = 'MOUSEMOTIONDOWN'
    MOUSEBUTTONUP = 'MOUSEBUTTONUP'
    MOUSEBUTTONDOWN = 'MOUSEBUTTONDOWN'


class InputHandler:
    def __init__(self):
        self.subscribers = {} 

    def add_subscriber(self, event_name, subscriber):
        """Add subscribers for a particular event.

        The subscribers dict is storing lists of subscribers,
        indexed by event types.

        Parameters
        ----------
        event_name : str
            Description of arg1
        event_attributes : dict
            Dictionary containing information about the occured 
            event. This dict 

        """
        if event_name in self.subscribers:
            self.subscribers[event_name].add(subscriber)
        else:
            self.subscribers[event_name] = {subscriber}

    def remove_subscriber(self, event_name, subscriber):
        """Remove a subscriber linked to a certain event.

        """
        if event_name in self.subscribers:
            self.subscribers[event_name].remove(subscriber)


    def notify_subscribers(self, event_name, event_attributes=None):
        """Notifies subscribers.

        Assumes that the subscribers have a method named input_update,
        with the following signature: 
            input_update(self, event_name, event_attributes)

        Parameters
        ----------
        event_type : str
            Description of arg1
        event_attributes : dict
            Dictionary containing information about the occured 
            event. This dict 

        """
        if event_name in self.subscribers:
            for subscriber in self.subscribers[event_name]:
                subscriber.input_update(event_name, event_attributes)
            
    def process_events(self):
        """Reads pygame events to notify the subscribers

        Loops through the events obtained via the get()
        method of pygame. 

        """
        for event in pygame.event.get():
            log.info(event)
            if event.type == pygame.QUIT:
                self.notify_subscribers(EventName.QUIT)
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE):
                    self.notify_subscribers(EventName.ESCAPE)
                if (event.key == pygame.K_SPACE):
                    self.notify_subscribers(EventName.SPACE)
                if (event.key == pygame.K_RETURN):
                    self.notify_subscribers(EventName.RETURN)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.notify_subscribers(
                    EventName.MOUSEBUTTONUP, event.__dict__)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.notify_subscribers(
                    EventName.MOUSEBUTTONDOWN, event.__dict__)
            elif event.type == pygame.MOUSEMOTION:
                self.notify_subscribers(EventName.MOUSEMOTION, event.__dict__)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.notify_subscribers(EventName.MOUSEMOTIONUP, event.__dict__)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.notify_subscribers(EventName.MOUSEMOTIONDOWN, event.__dict__)


                

