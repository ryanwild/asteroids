import sys

import pygame

from lib.shot import Shot
from lib.asteroid import Asteroid
from lib.asteroidfield import AsteroidField
from lib.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from lib.logger import log_event, log_state
from lib.player import Player


def main():
    message = f"""Starting Asteroids with pygame version: {pygame.version.ver}
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}
"""
    print(message)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    cx = SCREEN_WIDTH / 2
    cy = SCREEN_HEIGHT / 2

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (drawable, shots, updatable)
    Player.containers = (updatable, drawable)

    player = Player(cx, cy)
    asteroid_field = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
