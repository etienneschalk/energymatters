import logging 
import os 
import pygame 
import random
from enum import Enum   

from config import config 
from core.game import Game


log = logging.getLogger(__name__)


def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG,
        datefmt='%Y/%m/%d %H:%M:%S'
    ) 
    #filename=...  #  logging.config.fileConfig(fname, defaults=None, disable_existing_loggers=True)
    # https://docs.python.org/3/library/logging.config.html#module-logging.config
    log.info("Game started")
    Game().run()
    log.info("Game finished")


if __name__ == "__main__":
    main()
