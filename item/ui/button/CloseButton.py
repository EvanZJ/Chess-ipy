import pygame as p
from item.ui.TextButton import TextButton

class CloseButton(TextButton):
    def __init__(self, size : int = 18):
        super().__init__(
            p.Rect(0, 0, size, size),
            p.Color(255, 255, 255, 0),
            0,
            "X",
            size
        )