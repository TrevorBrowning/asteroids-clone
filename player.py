import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot
class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
        


    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), LINE_WIDTH)
        


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation +=  PLAYER_TURN_SPEED * dt

    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.cooldown > 0:
            self.cooldown -= dt
            if self.cooldown < 0:
                self.cooldown = 0

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        mouse_position = pygame.mouse.get_pos()
        mouse_vector = pygame.Vector2(mouse_position)
        mouse_diff = mouse_vector - self.position
        ref_direction = pygame.Vector2(0,1)
        rotation = ref_direction.angle_to(mouse_diff)
        self.rotation = rotation
        



    def try_shoot(self):
        if self.cooldown > 0:
            print("YOU CAN'T SHOOT")
            return

        self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        self.shoot()


    def shoot(self):
        shot = Shot(self.position)
        direction = pygame.Vector2(0, 1)
        direction = direction.rotate(self.rotation)
        shot.velocity = direction * PLAYER_SHOOT_SPEED
        