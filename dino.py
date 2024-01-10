import pygame
class Dino():
    def __init__(self, game):
        self.img = pygame.image.load("dino.png")
        self.img_width = self.img.get_width()
        self.img_height = self.img.get_height()
        self.game = game
        
        self.y_min = game.height - game.ground_height - self.img_height
        self.y = self.y_min
        self.x = 50
        self.jumping = False
        self.vel_y = 0

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x,
            self.y,
            self.img_width,
            self.img_height)

    def update(self):
        self.y += self.vel_y
        if self.y >= self.y_min:
            self.y = self.y_min
            self.jumping = False
        self.vel_y += .3

    def jump(self):
        if not self.jumping:
            self.vel_y = -7.8
            self.jumping = True