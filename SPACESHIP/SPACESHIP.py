import pygame
import os
import time
pygame.init()
pygame.font.init()
red_health=10
blue_health=10
SHOOT_SOUND=pygame.mixer.Sound("C:\\Users\\karti\\Desktop\\PYTHON\\SPACESHIP\\shoot.mp3")
BLAST_SOUND=pygame.mixer.Sound("C:\\Users\\karti\\Desktop\\PYTHON\\SPACESHIP\\explosion.mp3")
HEALTH_FONT=pygame.font.SysFont("arial",20)
WIDTH,HEIGHT=900,500
VEL=4
BULLET_VEL=8
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SPACESHIP BATTLE")
WHITE=(255,255,255)
FPS=60
MAX_SHOTS=5
BORDER=pygame.Rect(WIDTH/2-2.5,0,1,HEIGHT)
RED_SHIP=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SPACESHIP\\redship.png").convert_alpha( )
RED_SHIP=pygame.transform.scale(RED_SHIP,(75,60))
BLUE_SHIP=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SPACESHIP\\blueship.png").convert_alpha( )
BLUE_SHIP=pygame.transform.scale(BLUE_SHIP,(75,60))
SPACE=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SPACESHIP\\back2.jpg")
RED_HIT=pygame.USEREVENT+1
BLUE_HIT=pygame.USEREVENT+2

def draw_window(red,blue,red_shots,blue_shots,red_health,blue_health):
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN,(255,255,255),BORDER)
    red_health_text=HEALTH_FONT.render(f"HEALTH: {red_health}",1,(255,0,0))
    blue_health_text=HEALTH_FONT.render(f"HEALTH: {blue_health}",1,(0,255,255))
    WIN.blit(red_health_text,(30,30))
    WIN.blit(blue_health_text,(WIDTH-red_health_text.get_width()-30,30))
    WIN.blit(RED_SHIP,(red.x,red.y))
    WIN.blit(BLUE_SHIP,(blue.x,blue.y))
    for bullet in red_shots:
        pygame.draw.rect(WIN,(255,0,0),bullet)
    for bullet in blue_shots:
        pygame.draw.rect(WIN,(0,255,255),bullet)
          
    pygame.display.update()
 
def red_move(keys_pressed,red):
    if(keys_pressed[pygame.K_a] and red.x-VEL>0):
            red.x-= VEL
    if(keys_pressed[pygame.K_d] and red.x+VEL+red.width<BORDER.x):
            red.x+=VEL
    if(keys_pressed[pygame.K_w] and red.y-VEL>0):
            red.y-= VEL
    if(keys_pressed[pygame.K_s] and red.y+VEL+red.height<HEIGHT):
            red.y+=VEL
def blue_move(keys_pressed,blue):
    if(keys_pressed[pygame.K_LEFT] and blue.x-VEL>BORDER.x):
            blue.x-= VEL
    if(keys_pressed[pygame.K_RIGHT] and blue.x+VEL+blue.width<WIDTH): 
            blue.x+=VEL
    if(keys_pressed[pygame.K_UP] and blue.y-VEL>0):
            blue.y-= VEL
    if(keys_pressed[pygame.K_DOWN] and blue.y+VEL+blue.height<HEIGHT):
            blue.y+=VEL
def shots(red_shots,blue_shots,red,blue):
    for bullet in red_shots:
        bullet.x+=BULLET_VEL
        if blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(BLUE_HIT))
            red_shots.remove(bullet)
        elif(bullet.x>WIDTH):
            red_shots.remove(bullet) 
    for bullet in blue_shots:
        bullet.x-=BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            blue_shots.remove(bullet)
        elif(bullet.x<0):
             blue_shots.remove(bullet)
             
                  
def windraw(text,red_shots,blue_shots):
    WINNER_FONT=pygame.font.SysFont("arial",80)
    winner_text=WINNER_FONT.render(text,1,(255,255,0))
    WIN.blit(winner_text,(WIDTH//2-winner_text.get_width()//2,HEIGHT//2-winner_text.get_height()//2))
    for bullet in red_shots:
        red_shots.remove(bullet)
    for bullet in blue_shots:
        blue_shots.remove(bullet)
    pygame.display.update()
    time.sleep(5)
    main()


def main():
    pygame.display.update()
    pygame.event.clear()
    red=pygame.Rect(100,200,75,60)
    blue=pygame.Rect(700,200,75,60)
    red_shots=[]
    blue_shots=[]
    clock=pygame.time.Clock()
    run=True
    red_health=10
    blue_health=10
    while run:
        winner_text=''
        # windraw(winner_text,red_shots,blue_shots)
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                run=False
                pygame.quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q and len(red_shots)<MAX_SHOTS:
                    bullet=pygame.Rect(red.x+red.width,red.y+red.height//2,10,5)
                    red_shots.append(bullet)
                    SHOOT_SOUND.play()
                if event.key==pygame.K_RCTRL and len(blue_shots)<MAX_SHOTS:
                    bullet=pygame.Rect(blue.x,blue.y+blue.height//2,10,5)
                    blue_shots.append(bullet)
                    SHOOT_SOUND.play()

            if event.type==RED_HIT:
                BLAST_SOUND.play()
                red_health-=1
            if event.type==BLUE_HIT:
                BLAST_SOUND.play()
                blue_health-=1
            if red_health<=0:
                winner_text="BLUE WINS!!"
                break
            if blue_health<=0:
                winner_text="RED WINS!!"
                break
        # winner_text=''
        # if red_health<=0:
        #     winner_text="BLUE WINS!!"
        # if blue_health<=0:
        #     winner_text="RED WINS!!"

        if winner_text!='':
             windraw(winner_text,red_shots,blue_shots)
             break
        
        keys_pressed= pygame.key.get_pressed()
        blue_move(keys_pressed,blue)
        red_move(keys_pressed,red)

        shots(red_shots,blue_shots,red,blue)

        draw_window(red,blue,red_shots,blue_shots,red_health,blue_health)
    

    
        
     


if __name__=="__main__":
    main() 