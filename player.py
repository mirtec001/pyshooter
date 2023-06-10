import pygame
import bullet
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("img/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.velocity = 3
        self.bullet_cooldown = 10

        self.bullet_group = pygame.sprite.Group()
    
    def update(self):
        self.speed_x = 0
        self.speed_y = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.speed_x = -self.velocity
        if keys[pygame.K_d]:
            self.speed_x = self.velocity
        
        if keys[pygame.K_w]:
            self.speed_y = -self.velocity
        if keys[pygame.K_s]:
            self.speed_y = self.velocity

        if keys[pygame.K_SPACE] and self.bullet_cooldown == 0:
            self.bullet_group.add(bullet.Bullet(self.rect.x + 4, self.rect.y + 2))
        
        if self.bullet_cooldown == 0:
            self.bullet_cooldown = 10

        self.bullet_cooldown -= 1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.bullet_group.update()
        
        print("Bullet count: " + str(len(self.bullet_group)))


    def draw(self, window):
        window.blit(self.image, self.rect)
        self.bullet_group.draw(window)
