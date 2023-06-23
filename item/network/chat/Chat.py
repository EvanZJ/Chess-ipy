from item.core.GameObject import GameObject
from item.display.ImageLoader import ImageLoader
from item.network.Client import Client
from item.ui.chat.ChatUI import ChatUI
import pygame as p

class Chat(GameObject):
    def __init__(self, client : Client, user : str):
        super().__init__()

        self.client = client
        self.user = user
        self.block_raycast = False
        
        self.on_awake += self.__awake

        self.on_resize_window += self.__on_resize_window
    #     self.on_draw += self.__draw

    # def __draw(self):
    #     p.draw.rect(self.screen, p.Color("red"), self.rect)

    def __on_resize_window(self):
        self.rect = self.screen.get_rect()

    def __awake(self):
        self.change_order_layer(-1)
        self.chat = self.instantiate(ChatUI(self.user, p.Rect(0, 0, 375, 625), p.Color(72, 99, 156)), self)
        self.chat.set_anchor((0, 1))
        self.chat.set_pivot((0, 1))
        self.chat.set_margin(bottom = 50, left = 25)
        self.chat.on_user_message_enter += lambda user, message : self.client.send(["chat", "sendall", user, message])

        # self.chat.add_message("John", "Bwahahaha")
        # self.chat.add_message("Test", "Yuhu")

    def add_message(self, sender : str, message : str):
        self.chat.add_message(sender, message)