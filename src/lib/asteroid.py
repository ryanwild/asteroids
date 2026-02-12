import random

import pygame

from .circleshape import CircleShape
from .constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from .logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def _new_child_asteroid(self, angle, radius):
        pass

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)

        rotation_a = self.velocity.rotate(random_angle)
        rotation_b = self.velocity.rotate(-random_angle)

        next_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_a = Asteroid(self.position.x, self.position.y, next_radius)
        asteroid_b = Asteroid(self.position.x, self.position.y, next_radius)

        asteroid_a.velocity = rotation_a * 1.2
        asteroid_b.velocity = rotation_b * 1.2
