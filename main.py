import pygame as p
import chess.engine
from item.Button import Button
from item.Board import Board
import sys
import asyncio
import threading
import tracemalloc
import time

threads = []
p.init()
screen = p.display.set_mode((1600, 900))
p.display.set_caption("Chess-ipy")
game_state = "main_menu"
        # p.time.Clock().tick(60)

# def run_engine(board, engine):
#     result = engine.play(board.board, chess.engine.Limit(time=5))
#     board.board.push(result.move)

       
def play_local() -> None:
    # global game_state
    screen.fill((0, 0, 0))
    board = Board()
    board_temp = Board()
    get_redo = False
    prev_move = []
    
    # board.board = board.board.transform(chess.flip_horizontal)
    # board.board = board.board.transform(chess.flip_vertical)
    # board.board = board.board.transform(chess.flip_horizontal)
    clock = p.time.Clock()
    # engine = chess.engine.SimpleEngine.popen_uci("engine/stockfish.exe")
    while not board.board.is_game_over():
        clock.tick(board.max_fps)
        if get_redo == True:
            board_temp.draw(screen)
        else :
            board.draw(screen)
        p.display.update()
        # board.board = board.board.transform(chess.flip_vertical)
        # board.board = board.board.transform(chess.flip_horizontal)
        for event in p.event.get():
            if event.type == p.MOUSEBUTTONDOWN and get_redo == False:
                if event.button == 1:
                    temp_uci = board.get_clicked_position()
                    temp2 = board.index_2d(temp_uci) if temp_uci != None else None
                    temp = temp2[0] * 8 + temp2[1] if temp2 != None else None
                    print(temp)
                    if(temp not in board.legal_move_highlighted):
                        print("sini")
                        board.get_piece_legal_moves(temp_uci)
                        # board.draw(screen)
                    else : 
                        board_temp.last_activated = board.last_activated
                        board.move_piece(temp_uci)
                        print(board_temp.last_activated, board.last_activated)
                        board_temp.move_piece(temp_uci)
                        print(board.board)
                        print("-------------------")
                        print(board_temp.board)
            # get left arrow key event
            if event.type == p.KEYDOWN:
                if event.key == p.K_LEFT:
                    if len(board_temp.board.move_stack) == 0:
                        continue
                    else:
                        get_redo = True
                        move = board_temp.board.pop()
                        prev_move.append(move)
                        print(board.board)
                        print("-------------------")
                        print(board_temp.board)
                if event.key == p.K_RIGHT and get_redo == True:
                    move = prev_move.pop()
                    board_temp.board.push(move)
                    print(board.board)
                    print("-------------------")
                    print(board_temp.board)
                    if len(prev_move) == 0:
                        get_redo = False
            if event.type == p.QUIT:
                game_state = "exit"
                p.display.quit()
                p.quit()
                sys.exit()
        # time.sleep(120)

def main_menu():
    p.event.pump()
    screen.fill((0, 0, 0))
    background = p.image.load("resource/images/background.jpg")
    logo = p.image.load("resource/images/logo.png")
    logo = p.transform.scale(logo, (int(logo.get_width() * 0.75), int(logo.get_height() * 0.75)))
    screen.blit(background, (0, 0))
    screen.blit(logo, (720, 325))
    play_local = Button(100, 100, p.image.load("resource/images/play_now.png").convert_alpha(), 0.75)
    play_online = Button(100, 250, p.image.load("resource/images/play_online.png").convert_alpha(), 0.75)
    watch_game = Button(100, 400, p.image.load("resource/images/watch_match.png").convert_alpha(), 0.75)
    quit_game = Button(100, 550, p.image.load("resource/images/quit.png").convert_alpha(), 0.75)
    buttons = [play_local, play_online, quit_game, watch_game]
    while True:
        play_local.draw(screen)
        play_online.draw(screen)
        watch_game.draw(screen)
        quit_game.draw(screen)
        global game_state 
        if(buttons[0].clicked):
            game_state = "play_local"
            # print(game_state)
            break

        if(buttons[2].clicked):
            p.event.post(p.event.Event(p.QUIT))
            game_state = "exit"
        for event in p.event.get():
            if event.type == p.QUIT:
                p.display.quit()
                p.quit()
                sys.exit()
        p.display.update()

async def main() -> None:
    running = True
    # refresh_thread = threading.Thread(target=refresh_screen)
    # refresh_thread.start()
    # while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.display.quit()
            p.quit()
            sys.exit()

    if game_state == "exit":
        # p.display.quit()
        # p.quit()
        sys.exit()
    if(game_state == "main_menu"):
        p.display.update()
        # print(game_state)
        main_menu()
    if(game_state == "play_local"):
        p.display.update()
        play_local()
        # asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
        # asyncio.run(play_local())
        # print(game_state)

asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
asyncio.run(main())


