import pygame as p

from item.Button import Button
from item.Board import Board
import sys

import threading
import tracemalloc
import time

from item.Engine import Engine
from item.scene.MainMenu import MainMenu
tracemalloc.start()

threads = []
p.init()
# screen = p.display.set_mode((800, 450))
# screen = p.display.set_mode((1600, 900))
screen = p.display.set_mode((0, 0), p.FULLSCREEN)
p.display.set_caption("Chess-ipy")

engine = Engine(screen)
engine.load(MainMenu())
engine.run()