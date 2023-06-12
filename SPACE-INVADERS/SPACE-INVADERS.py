import pygame
import time
pygame.init()
VEL=5
MAX_BULLETS=5
BULLET_VEL=7
WIDTH,HEIGHT=900,600
SHIP_WIDTH,SHIP_HEIGHT=80,60
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('SPACE-INVADERS')
BLUE_SHIP=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SPACESHIP\\blueship.png").convert_alpha()
BLUE_SHIP=pygame.transform.scale(BLUE_SHIP,(SHIP_WIDTH,SHIP_HEIGHT))
BLUE_SHIP=pygame.transform.rotate(BLUE_SHIP,-90)

BACKGROUND=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SPACESHIP\\back2.jpg")
FPS=60
def draw(blue,blue_shots):
    WIN.blit(BACKGROUND,(0,0))
    WIN.blit(BLUE_SHIP,(blue.x,blue.y))
    for bullet in blue_shots:
        pygame.draw.rect(WIN,(0,255,255),bullet)
    pygame.display.update()

def blue_move(keys_pressed,blue):
    if(keys_pressed[pygame.K_LEFT] and blue.x-VEL>0):
            blue.x-= VEL
    if(keys_pressed[pygame.K_RIGHT] and blue.x+blue.width<WIDTH): 
            blue.x+=VEL
    
def shots(blue_shots):
    for bullet in blue_shots:
        bullet.y-=BULLET_VEL
        if(bullet.y<=0):
            blue_shots.remove(bullet)
def main():
    clock=pygame.time.Clock()
    run=True
    blue=pygame.Rect(450,500,80,60)
    blue_shots=[]
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP and len(blue_shots)<MAX_BULLETS:
                    bullet=pygame.Rect(blue.x+blue.width//2-13,blue.y,5,10)
                    blue_shots.append(bullet)
                     
        keys_pressed= pygame.key.get_pressed()
        blue_move(keys_pressed,blue)
        shots(blue_shots)
        draw(blue,blue_shots)

    pygame.quit()


if __name__=='__main__':
    main()