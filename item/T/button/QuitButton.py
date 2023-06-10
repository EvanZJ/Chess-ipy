from item.T.Button import Button
import pygame as p

class QuitButton(Button):
    def __init__(self, x : float, y : float, scale : float):
        image = p.image.load("resource/images/quit.png").convert_alpha()
        super().__init__(x, y, image, scale)

        self.on_mouse_down += self.quit

    def quit(self):
        p.event.post(p.event.Event(p.QUIT))

    