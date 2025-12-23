import os
#os.environ["SDL_AUDIODRIVER"] = "dummy"


import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from shot import Shot
from ui import *
from background import Background
import sys


def main():
    pygame.init()
    try:
        pygame.mixer.init()
        audio_enabled = True
    except pygame.error:
        print("Audio disabled (no sound device)")
        audio_enabled = False

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    # Score System
    score_counter = 0

    def current_lives():
        return player.lives


    def current_score():
        return score_counter
    
    # UI 
    ui = UI(screen, current_score, current_lives)

    # Background
    background = Background(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

    


    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    player.try_shoot()
                elif event.button == 3:
                    player.try_boost()


        updatable.update(dt)

        

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                if player.take_damage():
                    log_event("player_hit")

                if player.lives <= 0:
                    print("Game Over")
                    sys.exit()

            
            for shot in shots:
                
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    asteroid.kill()
                    score_counter += 25
        
        
        screen.fill("black")
        background.draw()

        for obj in drawable:
            obj.draw(screen)
        
        ui.draw()

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        
   

if __name__ == "__main__":
    main()
