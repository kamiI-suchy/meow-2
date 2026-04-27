import pygame
import sys


class Ball:
    def __init__(self, image_path, position, speed):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.speed = speed

    def update(self, screen_width, screen_height):
        self.rect = self.rect.move(self.speed)

        if self.rect.left < 0:
            self.rect.left = 0
            self.speed[0] = -self.speed[0]
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
            self.speed[0] = -self.speed[0]

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed[1] = -self.speed[1]
        elif self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.speed[1] = -self.speed[1]


class Game:
    WIDTH = 640
    HEIGHT = 480
    FPS = 50
    BG_COLOR = (100, 100, 100)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.fps_clock = pygame.time.Clock()
        self.balls = []

    def addBall(self, ball):
        self.balls.append(ball)

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.BG_COLOR)

            for ball in self.balls:
                ball.update(self.WIDTH, self.HEIGHT)
                self.screen.blit(ball.image, ball.rect)

            pygame.display.update()
            self.fps_clock.tick(self.FPS)


game = Game()
game.addBall(Ball("ball_soccer.png", [0, 0], [5, 5]))
game.addBall(Ball("ball_basketball.png", [100, 200], [-4, 4]))
game.addBall(Ball("ball_volleyball.png", [200, 50], [8, -8]))
game.start()
