import pygame
import player
import enemy
from settings import *
import random

class App:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Shoot")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = player.Player(64, HEIGHT - 96)
        self.spritegroup = pygame.sprite.Group()
        self.enemy_limit = 30
        self.generate_enemies(self.enemy_limit)

    def generate_enemies(self, enemy_limit):
        for x in range(enemy_limit):
            self.spritegroup.add(enemy.Enemy(random.randint(0, WIDTH - 64), random.randint(-100, -32)))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            self.update()
            self.draw()


    def update(self):
        self.clock.tick(FPS)
        self.player.update()
        self.spritegroup.update()

        hits = pygame.sprite.groupcollide(self.player.bullet_group, self.spritegroup, True, True)

        if len(self.spritegroup) == 0:
            self.generate_enemies(self.enemy_limit)
            print("New emeies spawned")

        # print(len(self.spritegroup))
        

    def draw(self):
        self.window.fill(BLACK)
        self.player.draw(self.window)
        self.spritegroup.draw(self.window)

        pygame.display.update()


if __name__ == "__main__":
    app = App()
    app.run()