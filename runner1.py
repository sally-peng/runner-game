import pygame
import random
from city_scroller import Scroller

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]
screenWidth = 800
screenHeight = 600
done = False
def random_color():
    return random.choice(colors)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screenWidth, screenHeight))

#Game Loop
FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)



class RunnerSprite(pygame.sprite.Sprite):
    def __init__ (self, file_name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file_name)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x -=3

        if self.rect.x <= -40:
            self.rect.x=800+40
            self.rect.y=random.randint(0,screenHeight)

player = RunnerSprite("nyan.png")

good_sprites=pygame.sprite.Group()
bad_sprites=pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)


front_scroller = Scroller(screenWidth, 400, screenHeight, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(screenWidth, 200, (screenHeight - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(screenWidth, 20, (screenHeight - 100), BACK_SCROLLER_COLOR, 1)

    #Put Drawing code here
score=0
lives=5

for i in range(40):
        randomx=random.randint(0,800)
        randomy=random.randint(0,600)
        temp=RunnerSprite("cup.png")
        temp.rect.x=randomx
        temp.rect.y=randomy
        all_sprites_list.add(temp)
        good_sprites.add(temp)


for t in range(15):
        randomx1=random.randint(0,800)
        randomy1=random.randint(0,600)
        bad=RunnerSprite("ghost.png")
        bad.rect.x=randomx1
        bad.rect.y=randomy1
        all_sprites_list.add(bad)
        bad_sprites.add(bad)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BACKGROUND_COLOR)

    # --- Drawing code should go here

    back_scroller.draw_buildings(screen) 
    back_scroller.move_buildings()
    middle_scroller.draw_buildings(screen)
    middle_scroller.move_buildings()
    front_scroller.draw_buildings(screen)
    front_scroller.move_buildings()

    all_sprites_list.draw(screen)
    all_sprites_list.update()
    coor=pygame.mouse.get_pos()
    player.rect.x=(coor[0])
    player.rect.y=(coor[1])

    
    blocks_hit_list = pygame.sprite.spritecollide(player, good_sprites, True)
    for block in blocks_hit_list:
        score +=1

    blocks_hit_list1 = pygame.sprite.spritecollide(player, bad_sprites, True)
    for block1 in blocks_hit_list1:
        lives -=1

    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Score: " + str(score),True,WHITE)
    screen.blit(text, [100, 50])

    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Lives: " + str(lives),True,WHITE)
    screen.blit(text, [100, 100])
    
    if lives<=0:
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("GAME OVER",True,RED)
        screen.blit(text, [400,300])

    if score==40:
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("YOU WIN !!!",True,GREEN)
        screen.blit(text, [400,300])

    pygame.display.flip()


clock.tick(60)

pygame.quit()
exit()