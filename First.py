#IKKE FERDIG :)


import random as rnd
import sys
import pygame
import time

print("gaard3n")

seconds = time.time()
local_time = time.ctime(seconds)


# pygame setup
# pygame setup
pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Girl")
clock = pygame.time.Clock()
running = True

bird_pos = pygame.Vector2(screen.get_width() / 5, screen.get_height() / 2)
color = "gray"

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(color)

    # RENDER YOUR GAME HERE
    pygame.draw.circle(screen, "red", bird_pos, 10)
    pygame.draw.rect(screen, "green", (1200, 300, 100 ,200))
    bird_pos.y += 3
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        bird_pos.y -= 10
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    #Death condition
    if bird_pos.y > height:
        alive = False
    if keys[pygame.K_r] and alive == False:
        alive = True
        bird_pos = pygame.Vector2(screen.get_width() / 5, screen.get_height() / 2)


x, y = 0, 0 #Initialbetingelser, bra om y posisjon er litt tilfeldig ?
Pipes = []

#Trykker på skjermen fugl blir høyere :)
def on_click(pos):
    return pos + 5

pygame.quit()
