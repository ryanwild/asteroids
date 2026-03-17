import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def wrap_around(self, screen):
        x = self.position[0]
        y = self.position[1]
        sw = screen.get_width()
        sh = screen.get_height()
        if x < 0:
            # off screen left
            self.position = pygame.Vector2(sw, y)
        if x > (sw + self.radius):
            # off screen right
            self.position = pygame.Vector2(0, y)
        if y < 0:
            # off screen top
            self.position = pygame.Vector2(x, sh)
        if y > (sh + self.radius):
            # off screen bottom
            self.position = pygame.Vector2(x, 0)

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        total_radius = self.radius + other.radius
        return distance <= total_radius
