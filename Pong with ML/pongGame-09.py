import pygame, random
pygame.init()
pygame.display.set_caption('Pongers!')
# Variables and constants
WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 0.5
FRAMERATE = 1000
colorOptions = ['blue','red','pink','yellow','green','purple','white']
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
            self.x = int(round(nextX,0))
            self.y = int(round(nextY,0))
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
        # This is a list, the second element is the y pos of the mouse
        self.y = pygame.mouse.get_pos()[1]
        # print("New y pos for paddle:",self.y)
        self.show(pygame.Color("white"))


# Create objects
ball = Ball( WIDTH // 2, HEIGHT // 2, -0.8, -0.8 ) # '//' returns the integer value of the division only
paddle1 = Paddle( 150 )
# paddle2 = Paddle( 250 )

# Draw the screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,WIDTH-BORDER,BORDER))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,BORDER,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,HEIGHT-BORDER,WIDTH-BORDER,BORDER))

# Show the objects for the first time
ball.show(pygame.Color(random.choice(colorOptions)))
paddle1.show(pygame.Color("white"))

sample = open("sample.csv","w")
print( "x,y,vx,vy,Paddle.y", file=sample)

clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sample.close()
            running = False

    clock.tick( FRAMERATE )

    paddle1.update()
    ball.update( pygame.Color(fgColor) )
    print("{},{},{},{},{}".format(ball.x,ball.y,ball.vx,ball.vy,paddle1.y), file=sample)
    pygame.display.flip()
    
