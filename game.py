import pygame
import dino
import obstacle
import sys
import visualinput as vi
import scoring as sc

class Game():
    def __init__(self):
        # init input device
        self.input = vi.Visualinput()

        # init pygame
        pygame.init()
        self.height = 400
        self.width = 600
        self.ground_height = 20
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.fps = 60
        pygame.display.set_caption("Dino Game")

        #create objects
        self.d = dino.Dino(self)
        self.o = obstacle.Obstacle(self)
        self.sc = sc.Scoring()

    def mainLoop(self):
        while True:
            self.handle_input()
            if self.d.get_rect().colliderect(self.o.get_rect()):
                break
            self.tick()
    
    def tick(self):
        self.d.update()
        self.o.update()
        self.sc.update()

        if self.sc.score % 4 == 0:
            self.input.show_image()

        self.screen.fill((255, 255, 255))
        pygame.draw.rect(self.screen, (0, 0, 0),
                         (0, self.height - self.ground_height,
                          self.width, self.ground_height))
        
        self.d.draw(self.screen)
        self.o.draw(self.screen)

        self.clock.tick(self.fps)
        pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #elif event.type == pygame.KEYDOWN:
            #    if event.key == pygame.K_SPACE:
            #        self.d.jump()
        if self.input.decideJump():
            self.d.jump()

if __name__ == '__main__':
    g = Game()
    g.mainLoop()

