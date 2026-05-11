import pygame
import random


pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Bedroom Survival")

clock = pygame.time.Clock()
running = True

font = pygame.font.SysFont(None, 23)

screen_width = 1200
screen_height = 800

# Timer
start_time = pygame.time.get_ticks()

# Closet settings
closet_x = 950
closet_y = 450
closet_width = 180
closet_height = 300

door_width = closet_width // 2
closet_open = False
under_bed = False



# 👇 UNDER BED STATE
under_bed = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # Closet toggle
            if event.key == pygame.K_e:
                closet_open = not closet_open

            # 👇 Under bed toggle
            if event.key == pygame.K_q:
                under_bed = not under_bed

    screen.fill((30, 30, 30))

    # Intro text for 3 seconds
    current_time = pygame.time.get_ticks()
    if current_time - start_time < 3000:
        text_surface = font.render(
            "Intruders are inside your house. Survive until sunrise.",
            True,
            (255, 255, 255)
        )
        text_rect = text_surface.get_rect(center=(600, 100))
        screen.blit(text_surface, text_rect)

    # Floor
    floor = pygame.Rect(0, 740, 1200, 60)
    pygame.draw.rect(screen, (50, 50, 50), floor)

    # Bed
    bed = pygame.Rect(0, 625, 350, 100)
    pillow = pygame.Rect(20, 615, 80, 30)


    pygame.draw.rect(screen, (200, 200, 200), bed)
    pygame.draw.rect(screen, (255, 255, 255), pillow)

    # Closet body
    closet_body = pygame.Rect(
        closet_x,
        closet_y,
        closet_width,
        closet_height
    )

    pygame.draw.rect(screen, (120, 70, 25), closet_body)

    # Closet doors
    left_door = pygame.Rect(
        closet_x,
        closet_y,
        door_width,
        closet_height
    )

    right_door = pygame.Rect(
        closet_x + door_width,
        closet_y,
        door_width,
        closet_height
    )

    if closet_open:
        open_left = pygame.Rect(
            closet_x - 40,
            closet_y,
            40,
            closet_height
        )

        open_right = pygame.Rect(
            closet_x + closet_width,
            closet_y,
            40,
            closet_height
        )

        pygame.draw.rect(screen, (90, 50, 20), open_left)
        pygame.draw.rect(screen, (90, 50, 20), open_right)

        inside = pygame.Rect(
            closet_x + 10,
            closet_y + 10,
            closet_width - 20,
            closet_height - 20
        )

        pygame.draw.rect(screen, (20, 20, 20), inside)

        if random.randint(1, 4) == 1:
            pygame.draw.circle(screen, (255, 0, 0), (1100, 600), 5)
            pygame.draw.circle(screen, (255, 0, 0), (1050, 600), 5)

    else:
        pygame.draw.rect(screen, (139, 69, 19), left_door)
        pygame.draw.rect(screen, (139, 69, 19), right_door)

        pygame.draw.line(
            screen,
            (80, 40, 10),
            (closet_x + door_width, closet_y),
            (closet_x + door_width, closet_y + closet_height),
            3
        )

        pygame.draw.circle(
            screen,
            (255, 215, 0),
            (closet_x + door_width - 15, closet_y + closet_height // 2),
            5
        )

        pygame.draw.circle(
            screen,
            (255, 215, 0),
            (closet_x + door_width + 15, closet_y + closet_height // 2),
            5
        )
        


    if under_bed:
        overlay = pygame.Surface((1200, 800))
        overlay.set_alpha(210)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        under_space = pygame.Rect(20, 650, 300, 80)
        pygame.draw.rect(screen, (10, 10, 10), under_space)

        
        if random.randint(1, 4) == 1:
            pygame.draw.circle(screen, (255, 0, 0), (100, 680), 5)
            pygame.draw.circle(screen, (255, 0, 0), (140, 680), 5)
                
    # Controls text
    controls = font.render("Press E to open/close closet", True, (255, 255, 255))
    screen.blit(controls, (20, 20))

    controls2 = font.render("Press Q to look under your bed", True, (255, 255, 255))
    screen.blit(controls2, (20, 50))

    controls3 = font.render("Press F to shine flashlight", True, (255, 255, 255))
    screen.blit(controls3, (20, 80))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()