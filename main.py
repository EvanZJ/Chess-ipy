import pygame as p
from item.Button import Button

p.init()
screen = p.display.set_mode((1600, 900))
p.display.set_caption("Chess-ipy")
game_state = "main_menu"


def main_menu():
    screen.fill((0, 0, 0))
    background = p.image.load("resource/images/background.jpg")
    screen.blit(background, (0, 0))
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
        if(buttons[0].hovered):
            print("Play local")
            # break
        if(buttons[1].hovered):
            print("Play online")
            # break
        if(buttons[2].hovered):
            print("Quit")
        if(buttons[3].hovered):
            print("Watch game")
            # break
        # if play_local.draw(screen):
        #     print("Play local")
        #     break
        # if play_online.draw(screen):
        #     print("Play online")
        #     break
        # if quit_game.draw(screen):
        #     print("Quit")
        #     break
        if(buttons[2].clicked):
            p.event.post(p.event.Event(p.QUIT))
            game_state = "exit"
        for event in p.event.get():
            if event.type == p.QUIT:
                p.display.quit()
                p.quit()
                exit()
        p.display.update()

if __name__ == "__main__":
    running = True
    while running:
        p.display.update()

        if game_state == "exit":
            running = False
        if(game_state == "main_menu"):
            main_menu()

