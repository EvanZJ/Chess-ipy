import pygame as p
from item.core.GameObject import GameObject
from item.ui.button.PlayLocalButton import PlayLocalButton
from item.ui.button.PlayOnlineButton import PlayOnlineButton
from item.ui.button.WatchGameButton import WatchGameButton
from item.ui.button.QuitButton import QuitButton
from item.ui.popup.NotificationFinished import NotificationFinished
from item.scene.Game import Game
from item.ui.popup.Room import Room

class MainMenu(GameObject):
    def __init__(self):
        super().__init__()

        self.background : p.Surface = p.image.load("resource/images/background.jpg")
        logo = p.image.load("resource/images/logo.png")
        self.logo : p.Surface = p.transform.scale(logo, (int(logo.get_width() * 0.75), int(logo.get_height() * 0.75)))

        self.on_awake += self.__awake
        self.on_draw += self.__draw

    def __awake(self):
        self.instantiate(PlayLocalButton(100, 100, 0.75)).on_mouse_down += self.play_local
        self.instantiate(PlayOnlineButton(100, 250, 0.75)).on_mouse_down += self.enable_room
        self.instantiate(WatchGameButton(100, 400, 0.75))
        self.instantiate(QuitButton(100, 550, 0.75))

        self.room = self.instantiate(Room(560, 600, p.Color(55, 56, 85, 255)))
        self.room.set_active(False)

    def __draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.logo, (720, 325))

    def play_local(self):
        current_game = Game()
        self.load(current_game)
        self.instantiate(NotificationFinished()) if current_game.is_finished else None

    def enable_room(self):
        self.room.set_active(True)



