import pygame
import random
from pygame.locals import *
pygame.init()										
screen = pygame.display.set_mode((1200,0) , FULLSCREEN)
cactus_surface = pygame.image.load('cactus_bricks.png').convert_alpha()			#To load various image sprites of the game
maryo_surface = pygame.image.load('maryo.png').convert_alpha()
fire_surface = pygame.image.load('fire_bricks.png').convert_alpha()
dragon_surface = pygame.image.load('dragon.png').convert_alpha()
start_screen = pygame.image.load('start.png').convert()
end_screen = pygame.image.load('end.png').convert()
flame = pygame.image.load('fireball.png').convert_alpha()
fireball_surface = pygame.image.load('fireball.png').convert_alpha()
pygame.transform.rotate(fireball_surface , 180)
pygame.mixer.music.load('mario_theme.wav')
sound = pygame.mixer.Sound('mario_dies.wav')
font = pygame.font.SysFont('arial',20,True)
pygame.display.set_caption('Maryo')

class maryo:
    x = 0
    x_inc = 1
    y = screen.get_height()/2 - maryo_surface.get_height()/2
    y_inc = -1
    m = []
    @staticmethod
    def move(l): 
        global gameexit  
        if l[K_LEFT] == 1:
            maryo.x_inc = -1								#Class Mario
        elif l[K_RIGHT] == 1:								#Movement Controls
            maryo.x_inc = 1
        else:
            maryo.x_inc = 0
        if l[K_UP]:
            maryo.y_inc = -1
        else:
            maryo.y_inc = 1
        maryo.y += maryo.y_inc
        maryo.x += maryo.x_inc
        screen.blit(maryo_surface , (maryo.x,maryo.y))
        i = 0
        for coord in maryo.m:
            screen.blit(fireball_surface , coord)
            maryo.m[i] = (coord[0]+1 , coord[1])
            if (coord[0] > dragon.x) and (dragon.y < coord[1] < dragon.y+dragon_surface.get_height()):
                maryo.m.remove((coord[0]+1,coord[1]))
                dragon.life -= 1
            if  (coord[0])== screen.get_width():
                maryo.m.remove((coord[0]+1 , coord[1]))
            i += 1
        if (maryo.y <= cactus.cac_surf.get_height()) or (maryo.y + maryo_surface.get_height()-10 >= screen.get_height() - fire.fire_surf.get_height()):
                    gameexit = 1
    @staticmethod
    def attack():
      #  print("Attack called")
       # screen.blit(fireball_surface , (maryo.get_rect().right() , (maryo.get_rect().height())/2 + maryo.get_rect.top()))	#Attack/Releasing Fireballs
        maryo.m += [(maryo.x + maryo_surface.get_width() , maryo.y + maryo_surface.get_height()/2)]
    @staticmethod
    def get_rect():
        return Rect(maryo.x , maryo.y , maryo_surface.get_width() , maryo_surface.get_height())
class cactus:
    y = 50
    cac_surf = None
    @staticmethod
    def load(level):
        cactus.cac_surf = cactus_surface.subsurface(0 , 200 - cactus.y*level , 1200 , cactus.y*level)
        screen.blit(cactus.cac_surf , ( 0 , 0))
class fire:
    y=50
    fire_surf = None
    @staticmethod
    def load(level):
        fire.fire_surf = fire_surface.subsurface( 0 , 0 , 1200 , fire.y*level)
        screen.blit( fire.fire_surf , (0 , screen.get_height() - fire.y*level))
class scoreboard:
    @staticmethod
    def show_score(score , topscore , level):
        string = "Score:" + str(score) + ' | ' + 'Topscore:' + str(topscore) + ' | Level:' + str(level) + '|' + ' Dragon LifePoints ' + str(dragon.life)
        screen.blit(font.render(string,True , (255,255,255)) , (((1200/len(string))/2*len(string)-125) , level*50))
class dragon:										#Dragon Class
    forbidden = 50
    x = screen.get_width()-dragon_surface.get_width()
    y = screen.get_height()/2-dragon_surface.get_height()/2
    y_inc = 1
    x_flame = x - flame.get_width()*.7
    x_inc = -1
    l = []
    life = 10
    @staticmethod
    def get_rect():
        return Rect(dragon.x , dragon.y , dragon_surface.get_width() , dragon_surface.get_height()) 
    @staticmethod
    def move(level):									#Governs Movement of the dragon
        global gameexit
        rect = maryo.get_rect()
        screen.blit(dragon_surface , (dragon.x , dragon.y))
        dragon.y += dragon.y_inc
        if (dragon.y + dragon_surface.get_height() )>= (screen.get_height() - fire.y*level):
            dragon.y_inc = -dragon.y_inc
        elif ((dragon.y )<=(dragon.forbidden*level)):
            dragon.y_inc = -dragon.y_inc
        elif rect.colliderect(dragon.get_rect()):
            gameexit = 1
        if dragon.life == 0:
            gameexit = 1
    @staticmethod
    def create_flame():
        dragon.l += [(dragon.x_flame , dragon.y)]
    @staticmethod
    def flame_throw():										#Flame throwing functionality of the dragon
        global gameexit
        i = 0
        for coord in dragon.l:
            screen.blit(flame ,coord )
            rect = Rect(coord[0] , coord[1] , flame.get_width()/2 , flame.get_height())
            if rect.colliderect(maryo.get_rect()):
                gameexit = 1
            if coord[0]-1 <=-flame.get_width():
                dragon.l.remove(coord)
                continue
            dragon.l[i] = (coord[0]-1 , coord[1])
            i += 1
clock = pygame.time.Clock()      
tick = 0
level = 1
score =0
topscore =0
gameexit = 0
screen.blit(start_screen , (screen.get_width()/2-start_screen.get_width()/2 , screen.get_height()/2-start_screen.get_height()/2))
pygame.display.update()
while True:
    pygame.event.clear()
    if (pygame.key.get_pressed()[K_RETURN] or pygame.key.get_pressed()[K_KP_ENTER] and (not gameexit)):
        sound.stop()										#Main Game Loop: deals with handling of the messages in the queue
        pygame.mixer.music.play(-1)
        while not gameexit:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_f:
                        maryo.attack()
            screen.fill((0,0,0))
            l = pygame.key.get_pressed()
            if l[K_ESCAPE]:
                pygame.quit()
            if l[K_UP] or l[K_LEFT] or l[K_RIGHT]:
                score += 1
            if (score%10000 == 0) and score>0:
                level += 1
                if level > 4:
                    level = 4
            if score>topscore:
                topscore = score
            tick += clock.tick()
            if tick > 800:
                dragon.create_flame()
                tick = 0
            cactus.load(level)
            fire.load(level)
            scoreboard.show_score(score , topscore , level)
            dragon.move(level)
            maryo.move(l)
            dragon.flame_throw()
            pygame.display.update()
        pygame.mixer.music.stop()
    elif pygame.key.get_pressed()[K_ESCAPE]:
        pygame.quit()
    elif gameexit:
        sound.play()
        screen.blit(end_screen , (screen.get_width()/2-end_screen.get_width()/2 , screen.get_height()/2-end_screen.get_height()/2))
        pygame.display.update()
        if  (1) or (pygame.key.get_pressed()[K_KP_ENTER]):
            tick = 0
            dragon.life = 10
            maryo.m = []
            gameexit = 0
            maryo.y = screen.get_height()/2 - maryo_surface.get_height()/2
            maryo.y_inc = -1
            maryo.x_inc = 0
            maryo.x = 0
            cactus.cac_surf = None
            fire.fire_surf = None
            dragon.y = screen.get_height()/2-dragon_surface.get_height()/2
            dragon.y_inc = 1
            dragon.x = screen.get_width()-dragon_surface.get_width()
            dragon.x_flame =  screen.get_width()-dragon_surface.get_width() - flame.get_width()*.7
            dragon.x_inc = -1
            dragon.l = []
            score = 0
            level = 1
        
