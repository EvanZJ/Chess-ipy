from typing import Callable
import pygame as p
from item.display.ImageLoader import ImageLoader
from item.scene.Game import Game
from item.scene.MultiplayerGame import MultiplayerGame

from item.ui.ImageButton import ImageButton
from item.chess.Board import Board
import sys

import threading
import tracemalloc
import time

from item.core.Engine import Engine
from item.scene.MainMenu import MainMenu

tracemalloc.start()

threads = []
p.init()
window = p.display.set_mode((640, 360), p.RESIZABLE)
# window = p.display.set_mode((800, 450), p.RESIZABLE)
# window = p.display.set_mode((1600, 900), p.RESIZABLE)
# window = p.display.set_mode((0, 0), p.FULLSCREEN)
screen = p.Surface((window.get_width(), window.get_height()))

window.set_alpha()
p.display.set_caption("Chess-ipy")

ImageLoader.set_reference_resolution(1600, 900)
ImageLoader.set_screen(window)

scenes = {
    0: MainMenu,
    1: Game,
    2: MultiplayerGame
}

engine = Engine(window, screen, scenes)
engine.load_scene(0)
engine.run()