import pygame, random
pygame.init()
pygame.display.set_caption('Pongers!')
# Variables
WIDTH = 1200
HEIGHT = 600
BORDER = 20
# Classes
class Ball: # Using a capital for classes
    RADIUS = 10
    # note these are double underscores - they're called 'dunder' functions
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        global screen
        pygame.draw.circle(screen, pygame.Color("white"), (self.x, self.y), self.RADIUS)
class Paddle:
    pass # we haven't made this yet so we use 'pass' to prevent crashing

# Create objects
ballplay = Ball( WIDTH - Ball.RADIUS, HEIGHT // 2 ) # '//' returns the integer value of the division only


colorOptions = ['blue','red','pink','yellow','grey','green','purple']
fgColor = pygame.Color(random.choice(colorOptions))
# Draw the screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,WIDTH,BORDER))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,BORDER,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,HEIGHT-BORDER,WIDTH,BORDER))
ballplay.show()

running = True
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False