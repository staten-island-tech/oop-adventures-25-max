import pygame
import random
import sys


class Monster:
    def __init__(self):
        self.show_closet_monster = False
        self.show_bed_monster = False
        self.show_door_monster = False
    def roll_closet(self):
        self.show_closet_monster = random.randint(1, 4) == 1
    def roll_bed(self):
        self.show_bed_monster = random.randint(1, 4) == 1
    def roll_door(self):
        self.show_door_monster = random.randint(1, 4) == 1
    def draw_closet(self):
        if self.show_closet_monster:
            pygame.draw.circle(screen, (255, 0, 0), (1065, 600), 5)
            pygame.draw.circle(screen, (255, 0, 0), (1015, 600), 5)
    def draw_bed(self):
        if self.show_bed_monster:
            pygame.draw.circle(screen, (255, 0, 0), (100, 680), 5)
            pygame.draw.circle(screen, (255, 0, 0), (140, 680), 5)
    def draw_door(self):
        if self.show_door_monster:
            pygame.draw.circle(screen, (255, 0, 0), (670, 575), 5)
            pygame.draw.circle(screen, (255, 0, 0), (710, 575), 5)
monster = Monster()


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
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    run_time = pygame.time.get_ticks()
    if run_time - start_time >= 1000 and not monster.show_closet_monster:
        monster.roll_closet()
        start_time = run_time
    if run_time - start_time >= 1000 and not monster.show_door_monster:
        monster.roll_door()
        start_time = run_time
    if run_time - start_time >= 1000 and not monster.show_bed_monster:
        monster.roll_bed()
        start_time = run_time




    monster.draw_closet()
    monster.draw_door()
    monster.draw_bed()




    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
