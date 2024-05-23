#import pygame 
import pygame
import sys
from pygame.locals import *

pygame.init()

window_width = 1920
window_height = 1080
fps = (60)
clock = pygame.time.Clock()
screen = pygame.display.set_mode([window_width, window_height], pygame.RESIZABLE)
pygame.display.set_caption('Test Game') 
init_game = False

font = pygame.font.Font('FiraCodeNerdFont-Bold.ttf', 50)
bg = pygame.image.load('background.png')
lvl1 = pygame.image.load('desert.jpg')
 

class Button():
    def __init__(self, txt, pos):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (220, 100))
    
    def draw(self):
        btn = pygame.draw.rect(screen, 'red',self.button , 0, 5)
        pygame.draw.rect(screen, 'black', self.button , 5, 5)
        text = font.render("Play", True, 'black',)
        screen.blit(text,(self.pos[0]+ 10 , self.pos[1]+10))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

    
def start_game(): #draw menu
    button = Button("text", (200,400))
    button.draw() 
   

    return button.check_clicked()

def play_game(): #draw game
    screen.blit(lvl1, (0, 0))
    player.draw(screen)
    text = font.render('This is where the game will take place', True, 'white')
    screen.blit(text, (100, 100))

'''Objects'''
class Character(pygame.sprite.Sprite):
    '''spawnm a player'''
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = pygame.image.load(image)
        self.x = x
        self.y = y
    def draw(self, screen):
        screen.blit(self.images, (self.x, self.y))


player = Character('pyimage.png', 100, 100) 


run = True
while run:
    screen.blit(bg, (0, 0))
    clock.tick(fps)
   
    if init_game:
        play_game()
    else:
        init_game = start_game()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.x -= 10
            elif event.key == K_RIGHT:
                player.x += 10
            elif event.key == K_UP:
                player.y -= 10
            elif event.key == K_DOWN:
                player.y += 10
              
    pygame.display.update()
pygame.quit()
