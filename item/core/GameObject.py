import pygame as p

from item.core.Event import Event
from typing import TypeVar

from item.display.ImageLoader import ImageLoader

class GameObject:
    T = TypeVar('T', bound='GameObject')

    def __init__(self):
        self.sprite: p.Surface = None
        self.resized_sprite: p.Surface = None
        self.screen: p.Surface
        self.rect: p.Rect = None
        self.order_layer: int = 0
        self.enabled : bool = False
        self.block_raycast : bool = True
        self.children : list['GameObject'] = []
        self.parent : 'GameObject' = None
        self.coordinate : tuple[int, int] = (0, 0)
        self.scale_xy : tuple[float, float] = None
        
        self.on_resize_window = Event()
        self.on_awake = Event()
        self.on_draw = Event()
        self.on_start = Event()
        self.on_update = Event()
        self.on_destroy = Event()
        self.on_instantiate = Event()
        self.on_hover = Event()
        self.on_mouse_down = Event()
        self.on_mouse_up = Event()
        self.on_load_scene = Event()
        self.on_change_order_layer = Event()
        self.on_keyboard_down = Event()
        self.on_enable = Event()
        self.on_disable = Event()
        self.on_rect_change = Event()
        
        self.on_resize_window += self.__on_resize_window
        self.on_awake += self.__awake
        self.on_draw += self.__draw

        # print(self.on_draw)

    def __on_resize_window(self):
        self.__resize()

    def __awake(self):
        if(self.resized_sprite is not None):
            self.rect = self.resized_sprite.get_rect()

    def __draw(self):
        if(self.resized_sprite is None):
            return
        if(self.rect is None):    
            return
        
        self.screen.blit(self.resized_sprite.copy(), self.rect)

    def scale(self, width : int, height : int):
        self.scale_xy = (width, height)
        self.__resize()

    def move(self, x : float, y : float):
        if isinstance(self.rect, p.Rect):
            self.rect.topleft = (x, y)

    def instantiate(self, game_object : T, parent : 'GameObject' = None) -> T:
        if parent is not None:
            game_object.parent = parent
            parent.children.append(game_object)
        self.on_instantiate(game_object)
        return game_object

    def load_scene(self, scene_id : int, *args, **keywargs):
        self.on_load_scene(scene_id, *args, **keywargs)

    def change_order_layer(self, new_order_layer: int):
        old_order_layer = self.order_layer
        self.order_layer = new_order_layer
        self.on_change_order_layer(self, old_order_layer, new_order_layer)

    def destroy(self):
        for child in self.children:
            child.parent = None
            child.destroy()
        self.children.clear()
        self.on_destroy(self)

    def collidepoint(self, x_y) -> bool:
        if(self.rect is not None):
            return self.rect.collidepoint(x_y)
        return False
    
    def set_active(self, value : bool):
        self.enabled = value
        if(self.enabled == True):
            self.on_enable()
        else:
            self.on_disable()

    def set_sprite(self, sprite : p.Surface):
        self.sprite = sprite
        self.__resize()

    def set_coordinate(self, new_coordinate : tuple[int, int]):
        self.coordinate = new_coordinate
        self.__resize()

    def __resize(self):
        if self.sprite is None:
            return
        
        self.resized_sprite = self.__resize_sprite(self.sprite)

        if self.scale_xy is not None:
            self.resized_sprite = ImageLoader.scale(
                self.resized_sprite, 
                (self.sprite.get_width(), self.sprite.get_height()), 
                self.scale_xy
            )

        self.__resize_rect(self.resized_sprite)

    def __resize_sprite(self, sprite : p.Surface) -> p.Surface:
        if sprite is None:
            return
        
        return ImageLoader.resize_surface(sprite)
    
    def __resize_rect(self, sprite : p.Surface):
        if sprite is None:
            return
        if self.rect is None:
            return
        
        self.rect = sprite.get_rect()
        x = ImageLoader.resize(self.coordinate[0], True)
        y = ImageLoader.resize(self.coordinate[1], False)
        self.rect.topleft = (x, y)
        self.on_rect_change()