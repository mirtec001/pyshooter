import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("img/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
    
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= -32:
            self.kill()

    def draw(self, window):
        window.blit(self.image, self.rect)
