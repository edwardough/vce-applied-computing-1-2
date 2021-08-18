import pygame as pg

scrWidth = 600
scrHeight = 400
win = pg.display.set_mode((scrWidth,scrHeight))

pg.display.set_caption("First Game")

# This goes outside the while loop, near the top of the program
walkRight = [pg.image.load('R1.png'), pg.image.load('R2.png'), pg.image.load('R3.png'), pg.image.load('R4.png'), pg.image.load('R5.png'), pg.image.load('R6.png')]
walkLeft = [pg.image.load('L1.png'), pg.image.load('L2.png'), pg.image.load('L3.png'), pg.image.load('L4.png'), pg.image.load('L5.png'), pg.image.load('L6.png')]
background = pg.image.load('background.png')
char = pg.image.load('R1.png')

clock = pg.time.Clock()

x = 50
y = 350
chrWidth = 17
chrHeight = 27
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
direction = 'right'
walkCount = 0

def redrawWindow():
    global walkCount, direction
    
    win.blit(background, (0,0))
    
    if walkCount + 1 >= 18:
        walkCount = 0

    if left == True:
        win.blit(walkLeft[walkCount // 3], (x,y))
        walkCount += 1
        direction = 'left'
    elif right == True:
        win.blit(walkRight[walkCount // 3], (x,y))
        walkCount += 1
        direction = 'right'
    else:
        if direction == 'right':
            win.blit(walkRight[0], (x,y))
        elif direction == 'left':
            win.blit(walkLeft[0], (x,y))

    pg.display.update()


# main loop
run = True
while run:
    clock.tick(18)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pg.K_RIGHT] and x < scrWidth - chrWidth - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if isJump == False:
        if keys[pg.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    elif isJump == True:
        if jumpCount >= 0:
            y -= (jumpCount ** 2) * 0.35
            jumpCount -= 1
        elif jumpCount < 0:
            y += (jumpCount ** 2) * 0.35
            jumpCount -= 1
        if jumpCount < -10:
            isJump = False
            jumpCount = 10

    redrawWindow()

pg.quit()