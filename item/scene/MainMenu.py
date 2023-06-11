import pygame as p
from item.GameObject import GameObject
from item.button.PlayLocalButton import PlayLocalButton
from item.button.PlayOnlineButton import PlayOnlineButton
from item.button.WatchGameButton import WatchGameButton
from item.button.QuitButton import QuitButton
from item.scene.Game import Game

class MainMenu(GameObject):
    def __init__(self):
        super().__init__()

        self.on_awake += self.__awake

    def __awake(self):
        background = p.image.load("resource/images/background.jpg")
        logo = p.image.load("resource/images/logo.png")
        logo = p.transform.scale(logo, (int(logo.get_width() * 0.75), int(logo.get_height() * 0.75)))

        self.screen.blit(background, (0, 0))
        self.screen.blit(logo, (720, 325))

        self.instantiate(PlayLocalButton(100, 100, 0.75)).on_mouse_down += self.play_local
        self.instantiate(PlayOnlineButton(100, 250, 0.75))
        self.instantiate(WatchGameButton(100, 400, 0.75))
        self.instantiate(QuitButton(100, 550, 0.75))

    def play_local(self):
        self.load(Game())



