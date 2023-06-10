import pygame as p

from item.T.Event import Event

class GameObject:
    def __init__(self):
        self.sprite: p.Surface = None
        self.screen: p.Surface
        self.rect: p.Rect = None
        
        self.on_awake = Event()
        self.on_draw = Event()
        self.on_start = Event()
        self.on_update = Event()
        self.on_destroy = Event()
        self.on_instantiate = Event()
        self.on_hover = Event()
        self.on_mouse_down = Event()
        self.on_mouse_up = Event()
        self.on_load = Event()
        
        self.on_awake += self.__awake

    def __awake(self):
        if(self.sprite is not None):
            self.rect = self.sprite.get_rect()

    def instantiate(self, game_object : 'GameObject'):
        self.on_instantiate(game_object)

    def load(self, game_object : 'GameObject'):
        self.on_load(game_object)

    def destroy(self, game_object : 'GameObject'):
        self.on_destroy(game_object)

    def collidepoint(self, x_y) -> bool:
        if(self.rect is not None):
            return self.rect.collidepoint(x_y)
        return False