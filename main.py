import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20
FPS = 10

# Color Scheme
BG_COLOR = (25, 25, 40)
SNAKE_COLOR = (102, 255, 102)
FOOD_COLOR = (255, 76, 76)
ENEMY_COLOR = (255, 153, 51)
TEXT_COLOR = (255, 255, 102)
SCORE_COLOR = (255, 255, 255)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kid-Friendly Snake Game")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, 36)
score_font = pygame.font.Font(None, 28)

# Game variables
snake = [[WIDTH//2, HEIGHT//2]]
direction = (0, 0)
food = [random.randrange(1, (WIDTH//CELL_SIZE)) * CELL_SIZE,
        random.randrange(1, (HEIGHT//CELL_SIZE)) * CELL_SIZE]
enemies = []
score = 0
highest_score = 0  # NEW: Track highest score

def draw_score(current, highest):  # MODIFIED: Now shows both scores
    score_text = score_font.render(f"Score: {current}", True, SCORE_COLOR)
    highest_text = score_font.render(f"Highest: {highest}", True, SCORE_COLOR)
    screen.blit(score_text, (10, 10))
    screen.blit(highest_text, (WIDTH - 150, 10))  # Top-right position

def draw_text(text, color, y_offset=0):
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect(center=(WIDTH/2, HEIGHT/2 + y_offset))
    screen.blit(text_surf, text_rect)

def generate_enemy():
    while True:
        enemy = [random.randrange(1, (WIDTH//CELL_SIZE)) * CELL_SIZE,
                 random.randrange(1, (HEIGHT//CELL_SIZE)) * CELL_SIZE]
        if enemy not in snake and enemy != food and enemy not in enemies:
            return enemy

# Game loop
running = True
game_over = False

while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_c:
                    # Reset game but keep highest score
                    snake = [[WIDTH//2, HEIGHT//2]]
                    direction = (0, 0)
                    food = [random.randrange(1, (WIDTH//CELL_SIZE)) * CELL_SIZE,
                            random.randrange(1, (HEIGHT//CELL_SIZE)) * CELL_SIZE]
                    enemies.clear()
                    score = 0
                    game_over = False
            else:
                if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)

    if not game_over:
        new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
        snake.insert(0, new_head)

        if snake[0] == food:
            score += 10
            food = [random.randrange(1, (WIDTH//CELL_SIZE)) * CELL_SIZE,
                    random.randrange(1, (HEIGHT//CELL_SIZE)) * CELL_SIZE]
            if score % 50 == 0:
                enemies.append(generate_enemy())
        else:
            snake.pop()

        # Collision check
        if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
            snake[0][1] < 0 or snake[0][1] >= HEIGHT or
            snake[0] in snake[1:] or
            snake[0] in enemies):
            game_over = True
            # Update highest score if needed
            if score > highest_score:  # NEW: Check and update high score
                highest_score = score

    # Draw elements
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, FOOD_COLOR, (food[0], food[1], CELL_SIZE, CELL_SIZE))

    for enemy in enemies:
        pygame.draw.rect(screen, ENEMY_COLOR, (enemy[0], enemy[1], CELL_SIZE, CELL_SIZE))

    draw_score(score, highest_score)  # MODIFIED: Pass both scores

    if game_over:
        draw_text("Game Over! Womp Womp", TEXT_COLOR, -60)
        draw_text(f"Final Score: {score}", TEXT_COLOR, -20)
        draw_text(f"Highest Score: {highest_score}", TEXT_COLOR, 20)  # NEW: Show highest
        draw_text("Press Q to quit or C to play again", TEXT_COLOR, 60)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()