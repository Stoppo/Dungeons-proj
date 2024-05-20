#import pygame 
import pygame

#initialize pygame wwhich allows pygame to process images sounds etc
pygame.init()

#create a window for your game/project
window_width = 1200
window_height = 775
#you can make variables for you diensions, #width,    height
screen = pygame.display.set_mode((window_width, window_height)) #set in tuple

#you need to control gamespeed and time
clock = pygame.time.Clock()

#create a title for your game
pygame.display.set_caption('Test Game') #you can change the icon too id imagine using a pic

#create a surface for your game
surface = pygame.Surface((1200,300)) #acts as dimension for surface also set in tuple
surface.fill('brown')
#you have to make the main game loop in order to keep the window running,
#usually use a while loop, this is also where you draw all elements and update everything


pygame.display.set_caption()
while True:
    #need to make an event for player input (usually a for loop)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()    #exit will uninitialize all of the code even after while loop

#display our surface
    screen.blit(surface,(0, 575))


#this line of code will update everything in the while loop back onto the screen
    pygame.display.update()
    clock.tick(60)