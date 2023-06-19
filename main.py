from typing import Callable
import pygame as p
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
# screen = p.display.set_mode((800, 450))
# screen = p.display.set_mode((1600, 900))
screen = p.display.set_mode((0, 0), p.FULLSCREEN)
screen.set_alpha()
p.display.set_caption("Chess-ipy")

scenes = {
    0: MainMenu,
    1: Game,
    2: MultiplayerGame
}

engine = Engine(screen, scenes)
engine.load_scene(0)
engine.run()