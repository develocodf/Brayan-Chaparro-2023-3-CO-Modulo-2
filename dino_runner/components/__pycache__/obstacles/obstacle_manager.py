import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def generate_obstacle(self):
        obstacle = Cactus(SMALL_CACTUS)

        return obstacle
        ##if type == 0:
            ##obstacle =  Bird()
        ##elif type == 1:
            ##obstacle = Cactus() tips a tener en cuenta

    def update(self, game):
       
        if len(self.obstacles) == 0:
            obstacle = self.generate.obstacle()
            self.obstacles.append(obstacle)

        for  obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderrect(obstacle.rect):
              game.playing = False
              pygame.time.delay(1000)
              break
               

    def draw (self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
