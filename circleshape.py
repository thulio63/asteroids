import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # overridden by sub-classes
        pass
    
    def update(self, dt):
        # overridden by sub-classes
        pass

    def collision(self, object):
        if self.position.distance_to(object.position) <= (self.radius + object.radius):
            return True
        return False