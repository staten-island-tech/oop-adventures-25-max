import pygame
import random
import sys
class Monster:
    def __init__(self):
        self.show_closet_monster = False
        self.show_bed_monster = False
        self.show_door_monster = False
    def roll_closet(self):
        self.show_closet_monster = random.randint(1, 1) == 1
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
Jumpscare = pygame.image.load('y.png').convert_alpha()
clock = pygame.time.Clock()
running = True
TIMER_INTERVAL = 10000 
next_trigger_time = pygame.time.get_ticks() + TIMER_INTERVAL
TIMER_INTERVAL = 10000 
next_trigger_time = pygame.time.get_ticks() + TIMER_INTERVAL
font = pygame.font.SysFont(None, 23)

screen_width = 1200
screen_height = 800
WIDTH = 1200
HEIGHT = 800
WIDTH = 1200
HEIGHT = 800
# Timer
start_time = pygame.time.get_ticks()
# Closet settings
closet_x = 950
closet_y = 450
closet_width = 180
closet_height = 300
#door settings
door_x = 600
door_y =  440
door_width = 175
door_height = 300
opened_door = door_width // 3
closet_door_width = closet_width // 2
#door settings
door_x = 600
door_y =  440
door_width = 175
door_height = 300
opened_door = door_width // 3
closet_door_width = closet_width // 2
closet_open = False
under_bed = False
open_door = False
light = False
run = False
hallway = pygame.Rect(0,0,0,0)
inside = pygame.Rect(0,0,0,0)
under_space = pygame.Rect(0,0,0,0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Closet toggle
            if event.key == pygame.K_e:
                closet_open = not closet_open
            # Under bed toggle
            # Under bed toggle
            if event.key == pygame.K_q:
                under_bed = not under_bed
            # Light toggle
            if event.key == pygame.K_f:
                light = not light
            # Door toggle
            if event.key == pygame.K_d:
                open_door = not open_door
            if event.key == pygame.K_w:
                run = not run
    screen.fill((30, 30, 30))

    # Intro text for 3 seconds
    current_time = pygame.time.get_ticks()
    if current_time - start_time < 10000:
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

    #window
    window = pygame.Rect(325, 350, 186, 180)
    pygame.draw.rect(screen, (13, 14, 46), window)
    #window cross thingy
    window1=pygame.Rect(413, 350, 10, 180)
    pygame.draw.rect(screen,(30,30,30), window1)
    window2=pygame.Rect(325, 435, 186, 10)
    pygame.draw.rect(screen,(30,30,30), window2)

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
     closet_door_width,
     closet_door_width,
        closet_height
    )

    right_door = pygame.Rect(
        closet_x + closet_door_width,
        closet_x + closet_door_width,
        closet_y,
     closet_door_width,
     closet_door_width,
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
        
        monster.draw_closet()
        

    else:
        pygame.draw.rect(screen, (139, 69, 19), left_door)
        pygame.draw.rect(screen, (139, 69, 19), right_door)

        pygame.draw.line(
            screen,
            (80, 40, 10),
            (closet_x + closet_door_width, closet_y),
            (closet_x + closet_door_width, closet_y + closet_height),
            (closet_x + closet_door_width, closet_y),
            (closet_x + closet_door_width, closet_y + closet_height),
            3
        )

        pygame.draw.circle(
            screen,
            (255, 215, 0),
            (closet_x + closet_door_width - 15, closet_y + closet_height // 2),
            (closet_x + closet_door_width - 15, closet_y + closet_height // 2),
            5
        )

        pygame.draw.circle(
            screen,
            (255, 215, 0),
            (closet_x + closet_door_width + 15, closet_y + closet_height // 2),
            (closet_x + closet_door_width + 15, closet_y + closet_height // 2),
            5
        )
       
    if open_door:
        opened = pygame.Rect(door_x - opened_door, door_y, opened_door, door_height)
        pygame.draw.rect(screen, (90, 50, 20), opened)

        hallway = pygame.Rect(door_x, door_y, door_width, door_height)
        pygame.draw.rect(screen,(10,10,10), hallway)

        handle_=pygame.Rect(758 - door_width - opened_door , 590, 17, 10)
        pygame.draw.rect(screen, (255, 215, 0), handle_)

        monster.roll_door()
        monster.draw_closet()

    else:
        door = pygame.Rect(door_x, door_y, door_width, door_height)
        pygame.draw.rect(screen, (120, 70, 25), door)

        handle=pygame.Rect(723, 590, 35, 10)
        pygame.draw.circle(screen, (255, 215, 0), (755, 595), 9)
        pygame.draw.rect(screen, (255, 215, 0 ), handle)

    if under_bed:
        overlay = pygame.Surface((1200, 800))
        overlay.set_alpha(210)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        under_space = pygame.Rect(20, 650, 300, 80)
        pygame.draw.rect(screen, (10, 10, 10), under_space)
        monster.roll_bed()
       
        
        monster.draw_closet()
        
    if light == True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (0, 255, 0), (mouse_x, mouse_y), 20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        hallway_click = False
        under_click = False
        inside_click = False
       
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            if hallway.collidepoint(event.pos):
                hallway_click=True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            if under_space.collidepoint(event.pos):
                under_click= True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            if inside.collidepoint(event.pos):
                inside_click=True

        if hallway_click:
            hallwayc = pygame.Rect(door_x, door_y, door_width, door_height)
            pygame.draw.rect(screen,(0,255,0), hallwayc)
        if under_click:
            under_spacec = pygame.Rect(20, 650, 300, 80)
            pygame.draw.rect(screen, (0, 255, 0), under_spacec)
        if inside_click:
            insidec = pygame.Rect(closet_x + 10, closet_y + 10, closet_width - 20, closet_height - 20)
            pygame.draw.rect(screen, (0, 255, 0), insidec)


        monster.roll_bed()
       
        
        monster.draw_closet()
        
    if light == True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (0, 255, 0), (mouse_x, mouse_y), 20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        hallway_click = False
        under_click = False
        inside_click = False
       
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            if hallway.collidepoint(event.pos):
                hallway_click=True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            if under_space.collidepoint(event.pos):
                under_click= True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            if inside.collidepoint(event.pos):
                inside_click=True

        if hallway_click:
            hallwayc = pygame.Rect(door_x, door_y, door_width, door_height)
            pygame.draw.rect(screen,(0,255,0), hallwayc)
        if under_click:
            under_spacec = pygame.Rect(20, 650, 300, 80)
            pygame.draw.rect(screen, (0, 255, 0), under_spacec)
        if inside_click:
            insidec = pygame.Rect(closet_x + 10, closet_y + 10, closet_width - 20, closet_height - 20)
            pygame.draw.rect(screen, (0, 255, 0), insidec)


    # Controls text
    controls = font.render("Press E to open/close closet", True, (255, 255, 255))
    screen.blit(controls, (20, 20))

    controls2 = font.render("Press Q to look under your bed", True, (255, 255, 255))
    screen.blit(controls2, (20, 50))

    controls3 = font.render("Press F to open light thing", True, (255, 255, 255))
    controls3 = font.render("Press F to open light thing", True, (255, 255, 255))
    screen.blit(controls3, (20, 80))

    controls4 = font.render("Press D to check the door", True, (255, 255, 255))
    screen.blit(controls4, (20, 110))

    #timer
    elapsed_ms = pygame.time.get_ticks() - start_time
    elapsed_sec = elapsed_ms // 1000
    
    timer_text = font.render(f"Time: {elapsed_sec}", True, (255, 255, 255))
    screen.blit(timer_text, (1120, 20))

    controls4 = font.render("Press D to check the door", True, (255, 255, 255))
    screen.blit(controls4, (20, 110))

    #timer
    elapsed_ms = pygame.time.get_ticks() - start_time
    elapsed_sec = elapsed_ms // 1000
    
    timer_text = font.render(f"Time: {elapsed_sec}", True, (255, 255, 255))
    screen.blit(timer_text, (1120, 20))

    if elapsed_sec >= 100:
        screen.fill((252,132,3))
        end_text = font.render( "YYAYAYAYYA you win, it the early morning because you fell asleep",True,(0, 0, 0))
        p = end_text.get_rect(center=(600, 100))
        screen.blit(end_text, p)
        end_text2 = font.render( "but it the next night, gulp",True,(0, 0, 0))
        p2= end_text.get_rect(center=(700, 150))
        screen.blit(end_text2, p2)
        end_text3 = font.render("ring ring ring ring",True,(0, 0, 0))
        p3= end_text.get_rect(center=(1200, 570))
        screen.blit(end_text3, p3)
    if elapsed_sec >= 110:
        screen.fill((0,0,0))
        new_text = font.render("it too bad you got kidnaped. HHAHHAHAHHah", True, (255,255,255))
        q = new_text.get_rect(center=(600, 100))
        screen.blit(new_text, q)
    if elapsed_sec >= 120:
        screen.fill((0,0,0))
        new_text1 = font.render("Johnny, lets sell his organs muahahahaha", True,(255,255,255))
        screen.blit(new_text1,q)
    if elapsed_sec >= 130:
        screen.fill((0,0,0))
        end_credits = font.render("The end", True,(255,255,255))
        screen.blit(end_credits,q)
       
        
    pygame.display.flip()
    clock.tick(10000)
    clock.tick(10000)

pygame.quit()
sys.exit()
       
sys.exit()
       