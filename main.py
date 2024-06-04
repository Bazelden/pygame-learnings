import pygame
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def create_tilemap(self):
        for i, row in enumerate(tilemap):
            for j, col in enumerate(row):
                if col == "B":
                    Block(self, j, i)
                if col == "P":
                    self.player = Player(self, j, i)

    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.create_tilemap()
                             
    def events(self):
        #game loop - events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        #game updates
        self.all_sprites.update()

    def draw(self):
        #screen draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.flip()

    def main(self):
        #game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        pass

g = Game()
g.new()
g.intro_screen()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
