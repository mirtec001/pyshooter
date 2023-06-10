import pygame
from settings import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # self.image = pygame.Surface([32, 32])
        # self.image.fill(GREEN)
        self.image = pygame.image.load("img/alien.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = 1

    def update(self):
        self.rect.y += self.velocity

        if self.rect.y >= HEIGHT:
            self.rect.y = -200

    def draw(self, window):
        window.blit(self.image, self.rect)
