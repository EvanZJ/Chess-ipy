# import pygame
# import sys

# pygame.init()
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Pygame Text Example")

# font = pygame.font.Font(None, 36)
# text = "Hello, Pygame!"
# text_surface = font.render(text, True, (255, 255, 255))
# text_rect = text_surface.get_rect()
# text_rect.center = (width // 2, height // 2)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     screen.fill((0, 0, 0))
#     screen.blit(text_surface, text_rect)
#     pygame.display.flip()

from item.network.Client import Client


client = Client("localhost", 5000)

print(client == client)