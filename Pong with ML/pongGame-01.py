import pygame, random

pygame.init()

# Variables
WIDTH = 1200
HEIGHT = 600
BORDER = 20
colorOptions = ['blue','red','pink','yellow','grey','green','purple']
fgColor = pygame.Color(random.choice(colorOptions))

# Draw the screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,WIDTH,BORDER))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,BORDER,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,HEIGHT-BORDER,WIDTH,BORDER))

running = True
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False