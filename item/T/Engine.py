import time
import pygame as p
import sys
import asyncio
import chess.engine
from item.T.GameObject import GameObject

class Engine:
    def __init__(self, screen : p.Surface):
        self.screen : p.Surface = screen
        self.game_objects: list[GameObject] = []
        self.mouse_down : bool = False

    def run(self):
        asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
        asyncio.run(self.__loop())

    def instantiate(self, game_object : GameObject):
        self.game_objects.append(game_object)
        game_object.screen = self.screen
        game_object.on_instantiate += self.instantiate
        game_object.on_load += self.load
        game_object.on_destroy += self.__destroy
        game_object.on_awake()
        game_object.on_start()

    def destroy_all(self):
        for game_object in self.game_objects.copy():
            self.__destroy(game_object)

    def load(self, game_object : GameObject):
        self.destroy_all()

        self.mouse_down = False
        self.screen.fill((0, 0, 0))

        for game_object in self.game_objects:
            print(game_object.__class__)

        self.instantiate(game_object)

    async def __loop(self):
        running = True
        while running:
            for event in p.event.get():
                if event.type == p.QUIT:
                    running = False
                    p.display.quit()
                    p.quit()
                    sys.exit()
            self.__draw()
            self.__update()
            
    def __draw(self):
        for game_object in self.game_objects:
            game_object.on_draw()
        p.display.update()

    def __update(self):
        for game_object in self.game_objects:
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

    def __destroy(self, game_object : GameObject):
        if(self.game_objects.__contains__(game_object)):
            self.game_objects.remove(game_object)
            game_object.on_destroy(game_object)
            game_object.on_instantiate -= self.instantiate
            game_object.on_load -= self.load
            game_object.on_destroy -= self.__destroy