import pygame
import sys
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from logger import log_state,  log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():

    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    tock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable= pygame.sprite.Group()
    asteroids= pygame.sprite.Group()
    shots= pygame.sprite.Group()

    Player.containers  = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)

    asteroidfield= AsteroidField()
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)



    #GAME LOOP  
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for boulder in asteroids:
            if boulder.collides_with(ship) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        screen.fill("black")

        for boulder in asteroids:
            for bullet in shots:
                if bullet.collides_with(boulder) == True:
                    log_event("asteroid_shot")
                    boulder.split()
                    bullet.kill()

        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()
        dt = tock.tick(60) / 1000
        

            

if __name__ == "__main__":
    main()
