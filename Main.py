#import pygame 
import pygame

pygame.init()

window_width = 1500
window_height = 780
fps = (60)
clock = pygame.time.Clock()
screen = pygame.display.set_mode([window_width, window_height], pygame.RESIZABLE)
pygame.display.set_caption('Test Game') 
init_game = False

font = pygame.font.Font('FiraCodeNerdFont-Bold.ttf', 50)

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

    
def start_game(): #draw game
    button = Button("text", (200,400))
    button.draw() 

    return button.check_clicked()

def play_game(): #draw menu
    pygame.draw.rect(screen, 'black',[0, 0, 1920, 1080])
    text = font.render('This is where the game will take place', True, 'white')
    screen.blit(text, (100, 100))
run = True
while run:
    screen.fill('gray34')
    clock.tick(fps)

    if init_game:
        play_game()
    else:
        init_game = start_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    

    pygame.display.update()
pygame.quit()
