import pygame as pg

win = pg.display.set_mode((500,500))

pg.display.set_caption("First Game")

x = 50
y = 425
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10

run = True
while run:
    pg.time.delay(50)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] and x > vel:
        x -= vel
    if keys[pg.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if isJump == False:
        if keys[pg.K_UP] and y > vel:
            y -= vel
        if keys[pg.K_DOWN] and y < 500 - height - vel:
            y += vel
        if keys[pg.K_SPACE]:
            isJump = True
    elif isJump == True:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10


    win.fill((0,0,0))
    pg.draw.rect(win, (255,0,0), (x,y,width,height))
    pg.display.update()

pg.quit()