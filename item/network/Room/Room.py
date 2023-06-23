import socket as so

import pygame as p

from item.core.GameObject import GameObject
from item.network.chat.Chat import Chat
from item.network.chess.MultiplayerBoard import MultiplayerBoard
from item.network.room.Participant import Participant
from item.network.room.PieceColor import PieceColor
from item.network.room.Role import Role
from item.network.room.RoomDetail import RoomDetail
from item.ui.TextRender import TextRender
from item.ui.popup.NotificationFinished import NotificationFinished

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
        self.participant.client.send(["room", "join", room_number, user_name])

    def create(self, room_number : int):
        print("a")
        self.participant.change_role(Role.ROOMMASTER)
        self.board = self.instantiate(MultiplayerBoard(self.participant))
        self.participant.change_piece_color(PieceColor.WHITE)
        self.create_room(room_number)

    def join(self, room_number : int):
        print("b")
        self.participant.change_role(Role.CHALLENGER)
        self.board = self.instantiate(MultiplayerBoard(self.participant))
        self.participant.change_piece_color(PieceColor.BLACK)
        self.create_room(room_number)

    def create_room(self, room_number : int):
        self.instantiate(Chat(self.user_name))
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