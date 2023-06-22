import chess
import pygame as p
from item.chess.Board import Board
from item.network.room.Participant import Participant
from item.network.room.PieceColor import PieceColor
from item.network.room.Role import Role
from item.ui.TextButton import TextButton

class MultiplayerBoard(Board):
    def __init__(self, participant : Participant):
        super().__init__()

        self.begin_button = None
        self.participant : Participant = participant
        self.participant.on_change_piece_color += self.__on_change_piece_color
        self.on_keyboard_down += self.__on_keyboard_down
        self.on_awake += self.__awake
        self.participant.on_ready += self.__on_ready
        self.on_push += self.__request_push
        self.participant.on_opponent_move += self.__on_opponent_move

    def __awake(self):
        self.__instantiate_begin_button()

    def can_move(self):
        if self.board.turn == chess.WHITE and self.participant.piece_color == PieceColor.WHITE:
            return True
        elif self.board.turn == chess.BLACK and self.participant.piece_color == PieceColor.BLACK:
            return True
        return False

    def __instantiate_begin_button(self):
        if self.participant.role != Role.ROOMMASTER:
            return

        self.begin_button = self.instantiate(TextButton(
            p.Rect(0, 80, 220, 60), 
            p.Color(255, 255, 255, 50),
            8,
            text = "Begin", 
            text_size = 36
        ))
        self.begin_button.on_mouse_down += lambda : self.__request_begin()

    def __on_change_piece_color(self, new_piece_color : PieceColor):
        if self.flipped == False and new_piece_color == PieceColor.BLACK:
            self.flip_board()
        elif self.flipped == True and new_piece_color == PieceColor.WHITE:
            self.flip_board()

    def __on_opponent_move(self, move_uci : str):
        self.last_move_tile.clear()
        self.push(chess.Move.from_uci(move_uci))

    def __on_keyboard_down(self, event : p.event.Event):
        if event.key == p.K_f:
            self.__request_change_piece_color()

    def __on_ready(self):
        if self.begin_button is not None:
            self.begin_button.set_active(False)
        self.begin()

    def __request_change_piece_color(self):
        if self.has_begun:
            return
        if self.participant.role != Role.ROOMMASTER:
            return
        
        self.participant.client.send("chess flip")

    def __request_begin(self):
        if self.has_begun:
            return
        if self.participant.role != Role.ROOMMASTER:
            return
        
        self.participant.client.send("chess begin")

    def __request_push(self, move : chess.Move):
        self.participant.client.send("chess move " + move.uci())