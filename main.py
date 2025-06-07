import pygame
from constants import *
from player import Player
from asteroid import Asteroid
import asteroidfield
import circleshape
import shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (drawable, updatable, shots)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = asteroidfield.AsteroidField()
    
    while True: # Game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for a in asteroids: # checks for asteroid collision
            if a.collision(player):
                print("Game over!")
                sys.exit()
        for a in asteroids: # checks for shot asteroids
            for s in shots:
                if a.collision(s) or s.collision(a):
                    a.kill()
                    s.kill()
        for obj in drawable: # draws objects
            obj.draw(screen)
        pygame.display.flip()
        #60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
