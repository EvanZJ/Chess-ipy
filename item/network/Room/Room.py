import socket as so

import pygame as p

from item.core.GameObject import GameObject
from item.network.chat.Chat import Chat
from item.network.chess.MultiplayerBoard import MultiplayerBoard
from item.network.room.Participant import Participant
from item.network.room.PieceColor import PieceColor
from item.network.room.Role import Role
from item.network.room.RoomDetail import RoomDetail
from item.ui.TextButton import TextButton
from item.ui.TextRender import TextRender
from item.ui.popup.Error import Error
from item.ui.popup.NotificationFinished import NotificationFinished
from item.ui.popup.SaveMatch import SaveMatch

class Room(GameObject):
    def __init__(self, participant : Participant, user_name : str):
        super().__init__()

        self.relative_value_text : TextRender = None
        self.notif_popup : NotificationFinished = None
        self.board : MultiplayerBoard = None

        self.participant : Participant = participant
        self.user_name : str = user_name

        self.on_update += self.__update
        self.participant.on_restart += self.__on_restart
        # self.participant.on_quit += lambda : self.load_scene(0)
        self.participant.on_quit += lambda : self.load_scene(0)
        self.participant.on_save += lambda json : self.instantiate(SaveMatch(json, 600, 400, p.Color(55, 56, 85, 255)))
        # self.participant.on_quit += lambda : print("test222")

    def __update(self):
        if self.relative_value_text is not None:
            self.relative_value_text.text = str(self.board.relative_value)
        # self.screen.blit(self.relative_value_text.render(), (0, 0))
        # print(self.relative_value_text.text)
        if self.board is not None:
            self.finished = self.board.finished
        # print(self.board.result)

            if self.finished and self.notif_popup is None:
            # self.instantiate(PromotionUI(p.Rect( 0, 0, 800, 600), p.Color(255, 255, 255, 100))))
                self.notif_popup = self.instantiate(NotificationFinished(0,0,2, self.board.result + " wins!"), self)
                self.save_button = self.instantiate(TextButton(p.Rect(0, 0, 100, 40), p.Color("black"), 8, "save", 36), self.notif_popup)
                self.save_button.set_anchor((0.5, 1))
                self.save_button.set_pivot((0.5, 1))
                self.save_button.set_margin(bottom = 30)
                self.save_button.change_order_layer(30)
                self.save_button.on_mouse_down += lambda event : self.participant.client.send(["chess", "save"])
                self.notif_popup.retry_button.set_active(False)

    def __on_restart(self):
        if self.board is not None:
            self.board.destroy()
            self.board = self.instantiate(MultiplayerBoard(self.participant))

    def request_create(self, user_name : str):
        print("Username: " + user_name)
        # self.participant.client.send("room create " + user_name)
        self.participant.client.send(["room", "create", user_name])

    def request_join(self, user_name : str, room_number : int):
        # self.participant.client.send("room join " + room_number + " " + user_name)
        self.participant.client.send(["room", "join", room_number, user_name, self.participant.role.value])

    def create(self, room_number : int):
        self.board = self.instantiate(MultiplayerBoard(self.participant))
        self.participant.change_piece_color(PieceColor.WHITE)
        self.create_room(room_number)

    def join(self, room_number : int):
        self.board = self.instantiate(MultiplayerBoard(self.participant))
        self.participant.change_piece_color(PieceColor.BLACK)
        self.create_room(room_number)

    def error(self, error_message : str):
        self.instantiate(Error(error_message, 600, 400, p.Color(55, 56, 85, 255)))

    def create_room(self, room_number : int):
        self.chat = self.instantiate(Chat(self.participant.client, self.user_name))
        self.participant.on_receive_chat += self.chat.add_message
        self.instantiate(RoomDetail(p.Rect(1200, 90, 200, 600), room_number, self.user_name))
        self.relative_value_text = self.__create_relative_value_text(str(self.board.relative_value))

    def __create_relative_value_text(self, text : str) -> TextRender:
        text = self.instantiate(TextRender(
            200,
            100,
            text,
            100,
            p.Color(255, 255, 255, 255),
        ), self)
        return text