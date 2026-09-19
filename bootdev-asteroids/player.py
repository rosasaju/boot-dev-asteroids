from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED
import pygame

class Player(CircleShape): 

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        triangle_points: list[pygame.Vector2] = self.triangle()
        pygame.draw.polygon(screen, "white", triangle_points, LINE_WIDTH)

    def rotate(self, dt: float) -> None: 
        self.rotation = PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        reverse_dt: float = -dt

        # move left
        if keys[pygame.K_a]:
            self.rotate(reverse_dt)

        # move right
        if keys[pygame.K_d]:
            self.rotate(dt)

        # move up
        if keys[pygame.K_w]: 
            self.move(dt)

        # move down
        if keys[pygame.K_s]: 
            self.move(reverse_dt)

    def move(self, dt: float) -> None: 
        unit_vector: pygame.Vector2 = pygame.Vector2(0, 1)
        rotated_vector: pygame.Vector2 = unit_vector.rotate(self.rotation) * (PLAYER_SPEED * dt)
        self.position = self.position + rotated_vector
