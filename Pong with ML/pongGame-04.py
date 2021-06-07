import pygame, random
pygame.init()
pygame.display.set_caption('Pongers!')
# Variables
WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 0.2
# Classes
class Ball: # Using a capital for classes
    RADIUS = 15
    # note these are double underscores - they're called 'dunder' functions
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    def show(self, color):
        global screen
        pygame.draw.circle(screen, color, (self.x, self.y), self.RADIUS)
    def update(self, color):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(color)
    
class Paddle:
    pass # we haven't made this yet so we use 'pass' to prevent crashing

# Create objects
ballplay = Ball( WIDTH - Ball.RADIUS, HEIGHT // 2, -VELOCITY, 0 ) # '//' returns the integer value of the division only

colorOptions = ['blue','red','pink','yellow','grey','green','purple','white']
fgColor = pygame.Color(random.choice(colorOptions))
# Draw the screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,WIDTH,BORDER))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,BORDER,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,HEIGHT-BORDER,WIDTH,BORDER))
ballplay.show(pygame.Color(random.choice(colorOptions)))
# ballplay.show(pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))

running = True
while running:
    ballplay.update( pygame.Color(random.choice(colorOptions)) )
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    