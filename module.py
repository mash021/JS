import random
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 60
PLAYER_VEL = 5
ENEMY_VEL = 3
BULLET_VEL = 7

PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
ENEMY_WIDTH, ENEMY_HEIGHT = 50, 50
BULLET_WIDTH, BULLET_HEIGHT = 10, 20

PLAYER = pygame.Rect(WIDTH//2, HEIGHT-PLAYER_HEIGHT-10, PLAYER_WIDTH, PLAYER_HEIGHT)
ENEMIES = []
BULLETS = []

def draw_window():
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLUE, PLAYER)
    for enemy in ENEMIES:
        pygame.draw.rect(WIN, RED, enemy)
    for bullet in BULLETS:
        pygame.draw.rect(WIN, GREEN, bullet)
    pygame.display.update()

def handle_player_movement(keys_pressed):
    if keys_pressed[pygame.K_LEFT] and PLAYER.x - PLAYER_VEL > 0:
        PLAYER.x -= PLAYER_VEL
    if keys_pressed[pygame.K_RIGHT] and PLAYER.x + PLAYER_VEL + PLAYER_WIDTH < WIDTH:
        PLAYER.x += PLAYER_VEL
    if keys_pressed[pygame.K_UP] and PLAYER.y - PLAYER_VEL > 0:
        PLAYER.y -= PLAYER_VEL
    if keys_pressed[pygame.K_DOWN] and PLAYER.y + PLAYER_VEL + PLAYER_HEIGHT < HEIGHT:
        PLAYER.y += PLAYER_VEL

def handle_bullets():
    for bullet in BULLETS:
        bullet.y -= BULLET_VEL
        if bullet.y < 0:
            BULLETS.remove(bullet)
        for enemy in ENEMIES:
            if bullet.colliderect(enemy):
                ENEMIES.remove(enemy)
                BULLETS.remove(bullet)
                break

def handle_enemies():
    for enemy in ENEMIES:
        enemy.y += ENEMY_VEL
        if enemy.y > HEIGHT:
            ENEMIES.remove(enemy)

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(PLAYER.x + PLAYER_WIDTH//2 - BULLET_WIDTH//2, PLAYER.y, BULLET_WIDTH, BULLET_HEIGHT)
                    BULLETS.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        handle_player_movement(keys_pressed)
        handle_bullets()
        handle_enemies()

        if random.randint(1, 20) == 1:
            enemy = pygame.Rect(random.randint(0, WIDTH-ENEMY_WIDTH), 0, ENEMY_WIDTH, ENEMY_HEIGHT)
            ENEMIES.append(enemy)

        draw_window()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
