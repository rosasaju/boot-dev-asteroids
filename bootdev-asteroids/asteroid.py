import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape): 

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position = self.position + (self.velocity * dt)

    def split(self) -> None: 
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS: 
            return 

        log_event("asteroid_split")
        asteroid1_degrees = random.uniform(20, 50)
        asteroid1_velocity = self.velocity.rotate(asteroid1_degrees)

        asteroid2_degrees = random.uniform(-50, -20)
        asteroid2_velocity = self.velocity.rotate(asteroid2_degrees)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = asteroid1_velocity * 1.2
        asteroid2.velocity = asteroid2_velocity * 1.2
