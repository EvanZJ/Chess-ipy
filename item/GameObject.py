import pygame as p

from item.Event import Event
from typing import TypeVar

class GameObject:
    T = TypeVar('T', bound='GameObject')

    def __init__(self):
        self.sprite: p.Surface = None
        self.screen: p.Surface
        self.rect: p.Rect = None
        self.order_layer: int = 0
        
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
        self.on_change_order_layer = Event()
        
        self.on_awake += self.__awake
        self.on_draw += self.__draw

    def __awake(self):
        if(self.sprite is not None):
            self.rect = self.sprite.get_rect()

    def __draw(self):
        if(self.sprite is None):
            return
        if(self.rect is None):    
            return
        
        scaled_sprite = p.transform.scale(self.sprite, (self.rect.width, self.rect.height))
        self.screen.blit(scaled_sprite, self.rect)

    def scale(self, width : int, height : int):
        self.rect.width = width
        self.rect.height = height

    def move(self, x : float, y : float):
        self.rect.topleft = (x, y)

    def instantiate(self, game_object : T) -> T:
        self.on_instantiate(game_object)
        return game_object

    def load(self, game_object : 'GameObject'):
        self.on_load(game_object)

    def change_order_layer(self, new_order_layer: int):
        old_order_layer = self.order_layer
        self.order_layer = new_order_layer
        self.on_change_order_layer(self, old_order_layer, new_order_layer)

    def destroy(self, game_object : 'GameObject'):
        self.on_destroy(game_object)

    def collidepoint(self, x_y) -> bool:
        if(self.rect is not None):
            return self.rect.collidepoint(x_y)
        return False