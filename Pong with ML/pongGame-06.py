import pygame, random
pygame.init()
pygame.display.set_caption('Pongers!')
# Variables
WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 0.5
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
        global bgColor
        self.show(bgColor)

        # TO DO - collision detection with walls
        if self.x - Ball.RADIUS - 1 < BORDER:
            self.vx *= -1
        if self.y - Ball.RADIUS - 1 < BORDER:
            self.vy *= -1
        if self.y + Ball.RADIUS + 1 > HEIGHT - BORDER:
            self.vy *= -1

        # TO DO - collision detection with paddle
        

        # Update the position of the ball
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(color)
    
class Paddle:
    PWIDTH = 20
    PHEIGHT = 100

    def __init__(self, y):
        self.y = y

    def show(self, color):
        global screen
        pygame.draw.rect(screen, color, pygame.Rect(WIDTH - self.PWIDTH, self.y - self.PHEIGHT, self.PWIDTH, self.PHEIGHT))

    def update(self):
        global bgColor
        self.show(bgColor)
        # This is a list, the second element is the y pos of the mouse
        self.y = pygame.mouse.get_pos()[1]
        self.show(pygame.Color("white"))


# Create objects
ballplay = Ball( WIDTH - Ball.RADIUS, HEIGHT // 2, -VELOCITY, -0.3 ) # '//' returns the integer value of the division only
playerpaddle = Paddle( 100 )

colorOptions = ['blue','red','pink','yellow','grey','green','purple','white']
bgColor = pygame.Color("black")
fgColor = pygame.Color(random.choice(colorOptions))
# Draw the screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,WIDTH,BORDER))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,BORDER,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,HEIGHT-BORDER,WIDTH,BORDER))

# Show the objects for the first time
ballplay.show(pygame.Color(random.choice(colorOptions)))
print("Ball shown")
playerpaddle.show(pygame.Color("white"))
print("Paddle shown")

running = True
while running:
    ballplay.update( pygame.Color(random.choice(colorOptions)) )
    playerpaddle.update()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    