import pygame
import sys

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set Game clock 
    game_clock: pygame.time.Clock = pygame.time.Clock()
    dt: float = 0.0

    # initiate group objects 
    updatable: pygame.sprite.Group = pygame.sprite.Group()
    drawable: pygame.sprite.Group = pygame.sprite.Group()
    asteroids: pygame.sprite.Group = pygame.sprite.Group()

    # group objects
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player_object: Player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field: AsteroidField = AsteroidField()

    # GAME loop s
    while True: 
        log_state()
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT: 
                return

        screen.fill("black")

        # update 
        updatable.update(dt) 

        for game_object in drawable:  
            game_object.draw(screen)

        # asteroids 
        for asteroid in asteroids:
            if asteroid.collides_with(player_object): 
                print("Game Over!")
                log_event("player_hit")
                sys.exit()


        pygame.display.flip()  # refresh the screen

        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
