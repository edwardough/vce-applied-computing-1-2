import pygame as pg

pg.init()
pg.display.set_caption('Build a racetrack!')

# VARIABLES AND CONSTANTS
WIDTH = 1370
HEIGHT = 710
BLOCK_SIZE = 10 # must be greater than velocity of the cars
FRAMERATE = 50
ROWS = HEIGHT // BLOCK_SIZE
COLS = WIDTH // BLOCK_SIZE
bgColor = pg.Color("black")
innerColor = pg.Color("pink")
outerColor = pg.Color("blue")
screen = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()
font = pg.font.Font('freesansbold.ttf', 48)
text = font.render('Start your enginez! Hit [space] to begin', True, innerColor, outerColor)
textRect = text.get_rect()
textRect.center = (WIDTH // 2, HEIGHT // 2)
gameStarted = False


# FUNCTIONS
def convertToListPos(targetX, targetY):
    global ROWS, COLS, BLOCK_SIZE
    currRow = targetY // BLOCK_SIZE
    currCol = targetX // BLOCK_SIZE
    position = currRow * COLS + currCol
    return position

def produceTracks( blockList ):
    result = []
    for block in blockList:
        if block.inner == True or block.inner == True:
            result.append(True)
        else:
            result.append(False)
    textResult = open("listAsText.txt","w")
    print("raceGrid=[",file=textResult)
    tempString = ""
    for item in result:
        tempString += str(item) + ","
    tempString = tempString[:-1] + "]"
    print(tempString,file=textResult)
        

# CLASSES
class Block:
    # Class: Block > the Block will be used to 'tile' the screen, allowing the user to 
    # left/right click on it to produce a list or array showing the 'inner' and 'outer' tracks
    global BLOCK_SIZE, innerColor, outerColor, bgColor

    def __init__(self, x, y, inner, outer):
        self.x = x
        self.y = y
        self.inner = inner
        self.outer = outer
    
    def show(self):
        global screen
        if self.inner == True:
            pg.draw.rect(screen, innerColor, pg.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))
        elif self.outer == True:
            pg.draw.rect(screen, outerColor, pg.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))
        else:
            pg.draw.rect(screen, bgColor, pg.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

    def update(self, innerStatus, outerStatus):
        global fgColor
        # IF MOUSE IS "IN" THE BLOCK AND MOUSE IS "DOWN" AND IT'S CURRENTLY VISIBLE = FALSE > CHANGE TO VISIBLE
        self.inner = innerStatus
        self.outer = outerStatus
        self.show()

# CREATE OBJECTS
blocks = []
for y in range(0,HEIGHT,BLOCK_SIZE):
    for x in range(0,WIDTH,BLOCK_SIZE):
        blocks.append(Block(x,y,False,False))

# print(f"{len(blocks)} blocks have been created.")

while True:
    for event in pg.event.get():
        # if event object type is QUIT then quit the pygame and program both.
        if event.type == pg.QUIT:
            produceTracks( blocks )
            pg.quit() # deactivates the pygame library
            print("Program quit.")
            quit() # quit the program.
        
        currX,currY = pg.mouse.get_pos()
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                # print("Space bar detected.")
                gameStarted = True
                # TODO currently the message remains on the screen. How could you remove it before
                # starting the rest of the program?

        if gameStarted == False:
            screen.blit(text, textRect)
        else:        
            if pg.mouse.get_pressed()[0] == True:
                listPosition = convertToListPos(currX,currY)
                # print(f"{currX,currY} has been converted to position {listPosition}.")
                blocks[listPosition].update(True,False)

            if pg.mouse.get_pressed()[1] == True:
                listPosition = convertToListPos(currX,currY)
                # print(f"{currX,currY} has been converted to position {listPosition}.")
                blocks[listPosition].update(False,False)

            if pg.mouse.get_pressed()[2] == True:
                listPosition = convertToListPos(currX,currY)
                # print(f"{currX,currY} has been converted to position {listPosition}.")
                blocks[listPosition].update(False,True)
 
        # Draws the surface object to the screen.
        pg.display.update()

    clock.tick( FRAMERATE )