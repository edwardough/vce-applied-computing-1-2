import pygame, random
pygame.init()
pygame.display.set_caption('Pongy!')
# Variables
WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 1
colorOptions = ['blue','red','pink','yellow','grey','green','purple','white']
bgColor = pygame.Color("black")
fgColor = pygame.Color(random.choice(colorOptions))
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
        global bgColor, paddle1

        # TO DO - game over message / response from program         
        nextX = self.x + self.vx
        nextY = self.y + self.vy

        if nextX - Ball.RADIUS < BORDER:
            self.vx = - self.vx
        elif nextY - Ball.RADIUS < BORDER or nextY + Ball.RADIUS > HEIGHT - BORDER:
            self.vy = - self.vy
        elif nextX + Ball.RADIUS > WIDTH - Paddle.PWIDTH and abs( nextY - paddle1.y + (Paddle.PHEIGHT // 2)) <= Paddle.PHEIGHT // 2:
            self.vx = - self.vx
        else:
            # Update the position of the ball
            self.show(bgColor)
            self.x = nextX
            self.y = nextY
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
        # colours in the current paddle black
        self.show(bgColor)
        # This is a list, the second element is the y pos of the mouse, hence [1]
        self.y = pygame.mouse.get_pos()[1]
        # print("New y pos for paddle:",self.y)
        self.show(pygame.Color("white"))


# Create objects
ballplay = Ball( WIDTH // 2, HEIGHT // 2, - VELOCITY, VELOCITY ) # '//' returns the integer value of the division only
paddle1 = Paddle( 150 )
# paddle2 = Paddle( 250 )

# Draw the screen and the borders
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,WIDTH-BORDER,BORDER))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,BORDER,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,HEIGHT-BORDER,WIDTH-BORDER,BORDER))

# Show the objects for the first time
ballplay.show(pygame.Color(random.choice(colorOptions)))
paddle1.show(pygame.Color("white"))

# Game loop
running = True
while running:
    paddle1.update()
    ballplay.update( pygame.Color(fgColor) )
    pygame.display.flip() # this redraws the screen each iteration of the while loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    