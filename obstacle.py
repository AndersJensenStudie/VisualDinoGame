import pygame

class Obstacle():
    def __init__(self, game):
        self.game = game
        
        self.img = pygame.image.load("cactus.png")
        self.img_width = self.img.get_width()
        self.img_height = self.img.get_height()

        self.x = game.width
        self.y = game.height - game.ground_height - self.img_width
        self.x_vel = -4

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def update(self):
        if self.x >= 0:
            self.x += self.x_vel
            self.x_vel -= .0001
            ##print(self.x_vel)
        elif self.x < 0:
            self.x = self.game.width

    def get_rect(self):
        return pygame.Rect(self.x,
            self.y,
            self.img_width,
            self.img_height)