import pygame
pygame.init()
from pygame.locals import *
screen = pygame.display.set_mode()
pygame.display.set_caption('Ping Pong')
font = pygame.font.SysFont('arial' , 20 , True , True)
class scoreboard:
        @staticmethod
        def write_board():
                string = "GOAL" + str(sliderA.goal) + '|' + str(sliderB.goal)
                screen.blit(font.render(string , True ,(255,255,255))  , (screen.get_width()/3,0))
class sliderA:
        x = screen.get_width()/5
        y = screen.get_height()/4
        goal = 0
        @staticmethod
        def draw_slider():
            pygame.draw.rect(screen , (255,255,255) , ( sliderA.x , sliderA.y , 12 , 100))
        @staticmethod
        def get_rect():
                return  Rect(sliderA.x , sliderA.y , 12 , 100)
        @staticmethod
        def move_slider(unit):
            if unit == K_w:
                sliderA.y -= 1
            elif unit == K_s:
                sliderA.y += 1

class sliderB:
    x = screen.get_width()*4/5
    y = screen.get_height()*3/4
    goal = 0
    @staticmethod
    def draw_slider():
        pygame.draw.rect(screen , (255,255,255) , ( sliderB.x , sliderB.y , 12 , 100))
    @staticmethod
    def get_rect():
            return Rect(sliderB.x , sliderB.y , 12 , 100)
    @staticmethod
    def move_slider(unit):
        if unit == K_UP:
            sliderB.y -= 1
        elif unit == K_DOWN:
            sliderB.y += 1

class ball:
    x_inc = 1
    y_inc = -1
    x  =  screen.get_width()//2
    y  =  7 
    @staticmethod
    def init():
        ball.y = 7
        ball.x = screen.get_width()//2
        ball.x_inc = 1
        ball.y_inc = -1
    @staticmethod
    def move(cls):
        if sliderA.get_rect().colliderect(Rect(ball.x,ball.y,7,7)):
                ball.x_inc = -ball.x_inc
        elif sliderB.get_rect().colliderect(Rect(ball.x , ball.y , 7 , 7)):
                ball.x_inc = -ball.x_inc
        if (ball.y+7) >= screen.get_height():
                ball.y_inc = -ball.y_inc
        if (ball.y-7) <= 0:
                ball.y_inc = -ball.y_inc
        ball.x += ball.x_inc
        ball.y += ball.y_inc
        if ball.x <= 0:
                sliderA.goal += 1
                ball.init()
        elif  ball.x >= screen.get_width():
                sliderB.goal += 1
                ball.init()
        pygame.draw.circle(screen , (255,255,255) , (ball.x , ball.y) , 7)
        
def centre_line():
    y = screen.get_height()/10
    for i in range(20):
        pygame.draw.line(screen , (255 , 255 , 255) , (screen.get_width()/1.97 , i*screen.get_height()/20) , (screen.get_width()/1.97 , i*screen.get_height()/20+17))

sliderA.draw_slider()
sliderB.draw_slider()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    l = pygame.key.get_pressed()
    if l[K_UP]:
        sliderB.move_slider(K_UP)
    elif l[K_DOWN]:
        sliderB.move_slider(K_DOWN)
    if l[K_w]:
        sliderA.move_slider(K_w)
    elif l[K_s]:
        sliderA.move_slider(K_s)
    screen.fill((0,0,0))
    scoreboard.write_board()
    sliderA.draw_slider()
    sliderB.draw_slider()
    centre_line()
    ball.move(sliderA)
    pygame.display.update()

    
