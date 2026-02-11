import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from logger import log_state
from player import Player


def main():

    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    tock = pygame.time.Clock()
    dt = 0

    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #GAME LOOP  
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        ship.update(dt)
        screen.fill("black")
        ship.draw(screen)
        pygame.display.flip()
        dt = tock.tick(60) / 1000
        

            

if __name__ == "__main__":
    main()
