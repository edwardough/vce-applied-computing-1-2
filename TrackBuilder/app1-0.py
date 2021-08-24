import pygame as pg

pg.init()
pg.display.set_caption('Build a racetrack!')

# VARIABLES AND CONSTANTS
WIDTH = 800
HEIGHT = 600
BLOCK_SIZE = 20
FRAMERATE = 50
ROWS = HEIGHT // BLOCK_SIZE
COLS = WIDTH // BLOCK_SIZE
bgColor = pg.Color("black")
fgColor = pg.Color("pink")
screen = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()

# FUNCTIONS
def convertToListPos(targetX, targetY):
    global ROWS, COLS, BLOCK_SIZE
    currRow = targetY // BLOCK_SIZE
    currCol = targetX // BLOCK_SIZE
    position = currRow * COLS + currCol
    return position

# CLASSES
class Block:
    global BLOCK_SIZE, fgColor, bgColor

    def __init__(self, x, y, visible):
        self.x = x
        self.y = y
        self.visible = visible
    
    def show(self):
        global screen
        if self.visible == True:
            pg.draw.rect(screen, fgColor, pg.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))
        elif self.visible == False:
            pg.draw.rect(screen, bgColor, pg.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

    def update(self, status):
        global fgColor
        # IF MOUSE IS "IN" THE BLOCK AND MOUSE IS "DOWN" AND IT'S CURRENTLY VISIBLE = FALSE > CHANGE TO VISIBLE
        self.visible = status
        self.show()

# CREATE OBJECTS
blocks = []
for y in range(0,HEIGHT,BLOCK_SIZE):
    for x in range(0,WIDTH,BLOCK_SIZE):
        blocks.append(Block(x,y,False))

print(f"{len(blocks)} blocks have been created.")

while True:
    for event in pg.event.get():
        # if event object type is QUIT then quit the pygame and program both.
        if event.type == pg.QUIT:
            # TODO provide opportunities to name the text file being created.
            # TODO output the text file of the 'race track'
            pg.quit() # deactivates the pygame library
            print("Program quit.")
            quit() # quit the program.
        
        currX,currY = pg.mouse.get_pos()
                
        if pg.mouse.get_pressed()[0] == True:
            listPosition = convertToListPos(currX,currY)
            print(f"{currX,currY} has been converted to position {listPosition}.")
            blocks[listPosition].update(True)

        if pg.mouse.get_pressed()[2] == True:
            listPosition = convertToListPos(currX,currY)
            print(f"{currX,currY} has been converted to position {listPosition}.")
            blocks[listPosition].update(False)
 
        # Draws the surface object to the screen.
        pg.display.update()

    clock.tick( FRAMERATE )