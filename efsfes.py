# import time

# start = time.time()


# while True:
#     elapsed = time.time() - start
        
#     if elapsed >= 10:
#         break


#     time.sleep(0.1)

# print("\nStopped after 10 seconds.")


import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
running = True

font = pygame.font.SysFont(None, 23)

screen_height = 800
wall = pygame.Rect(0, screen_height - 50, 300, 50)

start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # time
    current_time = pygame.time.get_ticks()

    # TEXT (3 seconds only)
    if current_time - start_time < 3000:
        text_surface = font.render(
            "Intruders are inside your house. Survive until sunrise.",
            True,
            (255, 255, 255)
        )
        text_rect = text_surface.get_rect(center=(600, 400))
        screen.blit(text_surface, text_rect)

    # 🛏️ BED
    bed = pygame.Rect(0, 740, 320, 60)
    pillow = pygame.Rect(10, 725, 60, 20)

    pygame.draw.rect(screen, (255, 255, 255), bed, 2)
    pygame.draw.rect(screen, (255, 255, 255), pillow, 2)

    # 🚪 CLOSET (bottom-right)
    closet = pygame.Rect(1120, 650, 80, 150)
    pygame.draw.rect(screen, (139, 69, 19), closet)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()