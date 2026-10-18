import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
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

    # initiate player object 
    Player.containers = (updatable, drawable)
    player_object: Player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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

        pygame.display.flip()  # refresh the screen

        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
