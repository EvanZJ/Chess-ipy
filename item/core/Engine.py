import time
import pygame as p
import sys
import asyncio
import chess.engine
from item.core.GameObject import GameObject

class Engine:
    def __init__(self, screen : p.Surface):
        self.screen : p.Surface = screen
        self.ordered_game_objects: dict[int, list[GameObject]] = {}
        self.ordered_game_objects_cache: dict[int, list[GameObject]] = {}
        self.mouse_down : bool = False

    def run(self):
        asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
        asyncio.run(self.__loop())

    def instantiate(self, game_object : GameObject):
        if game_object.order_layer not in self.ordered_game_objects_cache:
            self.ordered_game_objects_cache[game_object.order_layer] = []
        self.ordered_game_objects_cache[game_object.order_layer].append(game_object)
        game_object.screen = self.screen
        game_object.on_instantiate += self.instantiate
        game_object.on_load += self.load
        game_object.on_destroy += self.__destroy
        game_object.on_change_order_layer += self.__change_order_layer
        game_object.on_awake()
        game_object.on_start()

    def destroy_all(self):
        for game_objects in self.ordered_game_objects_cache.values():
            for game_object in game_objects.copy():
                self.__destroy(game_object)

    def load(self, game_object : GameObject):
        self.destroy_all()

        self.mouse_down = False
        self.screen.fill((0, 0, 0))
        # print('sini')
        for game_objects in self.ordered_game_objects.values():
            for game_object in game_objects:
                print(game_object.__class__)

        self.instantiate(game_object)

    async def __loop(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))
            for event in p.event.get():
                if event.type == p.QUIT:
                    running = False
                    p.display.quit()
                    p.quit()
                    sys.exit()
                if event.type == p.KEYDOWN:
                    self.__on_keyboard_down(p.key.get_pressed())
            self.__draw()
            self.__update()
            self.__end_frame()
            
    def __draw(self):
        for key, game_objects in sorted(self.ordered_game_objects.items()):
            for game_object in game_objects:
                if not game_object.enabled:
                    continue
                game_object.on_draw()
        p.display.update()

    def __update(self):
        for game_objects in self.ordered_game_objects.values():
            for game_object in game_objects:
                if not game_object.enabled:
                    continue
                pos = p.mouse.get_pos()
                if game_object.collidepoint(pos):
                    game_object.on_hover()
                    if self.mouse_down != p.mouse.get_pressed()[0]:
                        if self.mouse_down == False:
                            self.mouse_down = True
                            game_object.on_mouse_down()
                        else:
                            self.mouse_down = False
                            game_object.on_mouse_up()
                game_object.on_update()

    def __end_frame(self):
        self.ordered_game_objects = self.ordered_game_objects_cache.copy()

    def __destroy(self, game_object : GameObject):
        if(game_object.order_layer not in self.ordered_game_objects_cache):
            return
        game_objects = self.ordered_game_objects_cache[game_object.order_layer]
        if(game_object in game_objects):
            game_objects.remove(game_object)
            game_object.on_destroy(game_object)
            game_object.on_instantiate -= self.instantiate
            game_object.on_load -= self.load
            game_object.on_destroy -= self.__destroy
            game_object.on_change_order_layer -= self.__change_order_layer

    def __change_order_layer(self, game_object : GameObject, old_order_layer : int, new_order_layer : int):
        if(old_order_layer not in self.ordered_game_objects_cache):
            return
        game_objects = self.ordered_game_objects_cache[old_order_layer]
        if(game_object not in game_objects):
            return
        game_objects.remove(game_object)
        self.ordered_game_objects_cache[old_order_layer] = game_objects
        if(new_order_layer not in self.ordered_game_objects_cache):
            self.ordered_game_objects_cache[new_order_layer] = []
        game_objects = self.ordered_game_objects_cache[new_order_layer]
        game_objects.append(game_object)
        self.ordered_game_objects_cache[new_order_layer] = game_objects

    def __on_keyboard_down(self, keys_pressed : p.key.ScancodeWrapper):
        for game_objects in self.ordered_game_objects.values():
            for game_object in game_objects:
                if not game_object.enabled:
                    continue
                game_object.on_keyboard_down(keys_pressed)