# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import *
from Asteroid import *
from AsteroidField import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for entity in asteroids:
            if entity.check_collision(player):
                print("Game over!")
                sys.exit()
        screen.fill((0,0,0))
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time()/1000


if __name__ == "__main__":
    main()
