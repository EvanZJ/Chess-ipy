import pygame as p
from item.T.GameObject import GameObject
from item.T.button.PlayLocalButton import PlayLocalButton
from item.T.button.PlayOnlineButton import PlayOnlineButton
from item.T.button.WatchGameButton import WatchGameButton
from item.T.button.QuitButton import QuitButton

class MainMenu(GameObject):
    def __init__(self):
        super().__init__()

        self.on_start += self.__start

    def __start(self):
        background = p.image.load("resource/images/background.jpg")
        logo = p.image.load("resource/images/logo.png")
        logo = p.transform.scale(logo, (int(logo.get_width() * 0.75), int(logo.get_height() * 0.75)))

        self.screen.blit(background, (0, 0))
        self.screen.blit(logo, (720, 325))

        self.instantiate(PlayLocalButton(100, 100, 0.75))
        self.instantiate(PlayOnlineButton(100, 250, 0.75))
        self.instantiate(WatchGameButton(100, 400, 0.75))
        self.instantiate(QuitButton(100, 550, 0.75))



