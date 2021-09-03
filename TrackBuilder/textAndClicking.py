# SourceL https://www.geeksforgeeks.org/python-display-text-to-pygame-window/

import pygame, random
pygame.init()
pygame.display.set_caption('Pongers!')

# Variables
WIDTH = 1200
HEIGHT = 600
BORDER = 20
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
colorOptions = ['blue','red','pink','yellow','grey','green','purple','white']
bgColor = pygame.Color("black")
fgColor = pygame.Color(random.choice(colorOptions))

# Define objects



# Draw the screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)
 
# create a text suface object,
# on which text is drawn on it.
text = font.render('This is how you can get text onto the screen', True, green, blue)
 
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
 
# set the center of the rectangular object.
textRect.center = (WIDTH // 2, HEIGHT // 2)

# Show the objects

# infinite loop
while True:
 
    # completely fill the surface object
    # with white color
    screen.fill(white)
 
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    screen.blit(text, textRect)
 
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
        x,y = pygame.mouse.get_pos()
        textRect.center = (400, 400)
        
        if pygame.mouse.get_pressed()[0] == False:
            text = font.render("Left button clicked!", True, green, blue)
        else:
            text = font.render("Left button not clicked.", True, green, blue)
        
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
 
            # deactivates the pygame library
            pygame.quit()
 
            # quit the program.
            quit()
 
        # Draws the surface object to the screen.
        pygame.display.update()
    