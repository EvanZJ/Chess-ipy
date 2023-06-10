import pygame as p
class Button:
    def __init__(self, x, y, image, scale):
        self.image = image
        self.image = p.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = True
        self.hovered = False

    def draw(self, screen):
        action = False
        pos = p.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if p.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
            if p.mouse.get_pressed()[0] == 0:
                self.clicked = False
            self.hovered = True
        else:
            self.hovered = False
        screen.blit(self.image, self.rect)
        return action