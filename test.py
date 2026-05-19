import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clickable Object Example")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 120, 255)
GREEN = (0, 200, 0)

# Create a rectangle object (x, y, width, height)
button_rect = pygame.Rect(150, 150, 200, 80)

# Main loop
while True:
    screen.fill(WHITE)

    # Draw the button
    pygame.draw.rect(screen, BLUE, button_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Detect mouse click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            if button_rect.collidepoint(event.pos):
                pygame.draw.rect(screen, GREEN, button_rect)

    pygame.display.flip()