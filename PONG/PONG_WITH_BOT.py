import pygame
import time
import os
pygame.init()
SOUND=pygame.mixer.Sound("C:\\Users\\karti\\Desktop\\PYTHON\\PONG\\BOUNCE.mp3")
GOAL=pygame.mixer.Sound("C:\\Users\\karti\\Desktop\\PYTHON\\PONG\\LASER.mp3")
SCORE_FONT = pygame.font.SysFont("comicsans", 50)
WINNING_SCORE = 10
VEL=8
WIDTH,HEIGHT=800,600
P_WIDTH,P_HEIGHT=20,100
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PONG")
FPS=60
WHITE=(255,255,255)
BLACK=(0,0,0)
BALL_VEL=8

class Paddle:
    VEL=8
    COLOR=(255,0,0)
    def __init__(self,x,y,width,height):
        self.x = self.original_x=x
        self.y = self.original_y=y
        self.width=width
        self.height=height
    
    def draw(self,win):
        pygame.draw.rect(win,self.COLOR,(self.x,self.y,self.width,self.height))
    
    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y


class Ball:
    BALL_VEL=8
    COLOR=(0,255,255)
    def __init__(self,x,y,radius):
        self.x=self.x_o=x
        self.y=self.y_o=y
        self.radius=radius
        self.x_vel=self.BALL_VEL
        self.y_vel=0

    def draw(self,win):
        pygame.draw.circle(win,self.COLOR,(self.x,self.y),self.radius)

    def move(self):
        self.x+=self.x_vel
        self.y+=self.y_vel
    def reset(self):
        self.x=self.x_o
        self.y=self.y_o   
        self.x_vel*=-1
        self.y_vel=0



def draw(win,paddles,ball,left_score,right_score):
    WIN.fill(BLACK)
    ball.draw(win)
    left_score_text=SCORE_FONT.render(f"{left_score}",1,WHITE)
    right_score_text=SCORE_FONT.render(f"{right_score}",1,WHITE)
    win.blit(left_score_text,(WIDTH//4-left_score_text.get_width(),20))
    win.blit(right_score_text,((WIDTH*3)//4-right_score_text.get_width(),20))
    for paddle in paddles:
        paddle.draw(win)
    pygame.display.update()

def collision(ball,left_paddle,right_paddle,BALL_VEL):
    if ball.y+ball.radius>=HEIGHT or ball.y-ball.radius<=0:
        SOUND.play()
        ball.y_vel*=-1
    if ball.x_vel<0:
        if ball.y>=left_paddle.y and ball.y<=left_paddle.y+left_paddle.height:
            if ball.x-ball.radius<=left_paddle.x+left_paddle.width:
                ball.x_vel*=-1
                SOUND.play()
                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.BALL_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel
                # comp_paddle_move(ball,left_paddle)

    else:
        if ball.y>=right_paddle.y and ball.y<=right_paddle.y+right_paddle.height:
            if ball.x+ball.radius>=right_paddle.x:
                SOUND.play()
                ball.x_vel*=-1
                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.BALL_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel
                # comp_paddle_move(ball,left_paddle)
    
def left_paddle_move(left_paddle):
    # if up ==True:
        
        while True:
           left_paddle.y-=left_paddle.VEL
        #    if left_paddle.y<final_y and left_paddle.y+left_paddle.height>final_y:
        #        return None
    # else:
        # while True:
        #    left_paddle.y+=left_paddle.VEL
        #    if left_paddle.y<final_y and left_paddle.y+left_paddle.height>final_y:
        #        return None
    
    


def paddle_move(keys,left_paddle,right_paddle):
    if keys[pygame.K_w] and left_paddle.y-VEL>=0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y+VEL+P_HEIGHT<=HEIGHT:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y-VEL>=0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y+VEL+P_HEIGHT<=HEIGHT:
        right_paddle.move(up=False)
# def up_move(left_paddle,final_y):
#     left_paddle.y-=left_paddle.VEL
#     # if left_paddle.y<final_y and left_paddle.y+left_paddle.height>final_y:
#     #     return None
# def down_move(left_paddle,final_y):
#     left_paddle.y+=left_paddle.VEL
#     # if left_paddle.y<final_y and left_paddle.y+left_paddle.height>final_y:
#     #     return None
    
def comp_paddle_move(ball,left_paddle):
    # ball.x_vel*=-1
    if  ball.y_vel>0:
        hori=((HEIGHT - ball.y)*ball.x_vel)//ball.y_vel
        final_y= ((WIDTH- hori)*ball.y)//hori
            # if left_paddle.y<=final_y and left_paddle.y+left_paddle.height>=final_y:
            #     break
        if left_paddle.y>final_y :
                # left_paddle_move(left_paddle,final_y,up=True)
                up_move(left_paddle,final_y)
        elif left_paddle.y+left_paddle.height<final_y:
                down_move(left_paddle,final_y)
    elif ball.y_vel<0:
        hori=((ball.y)*ball.x_vel)//ball.y_vel
        final_y= ((WIDTH- hori)*ball.y)//hori
        
            # if left_paddle.y<=final_y and left_paddle.y+left_paddle.height>=final_y:
            #     break
        if left_paddle.y>final_y :
                # left_paddle_move(left_paddle,final_y,up=True)
                up_move(left_paddle,final_y)
        elif left_paddle.y+left_paddle.height<final_y:
                # left_paddle.move(up=False)
               down_move(left_paddle,final_y)
    else:
        final_y= ball.y
        while True:
            if left_paddle.y<=final_y and left_paddle.y+left_paddle.height>=final_y:
                break
            elif left_paddle.y>final_y :
                left_paddle.move(up=True)
            elif left_paddle.y+left_paddle.height<final_y:
                left_paddle.move(up=False)


def main():
    run=True
    clock=pygame.time.Clock()

    left_paddle=Paddle(10,HEIGHT//2-P_HEIGHT//2,P_WIDTH,P_HEIGHT)
    right_paddle=Paddle(WIDTH-P_WIDTH-10,HEIGHT//2-P_HEIGHT//2,P_WIDTH,P_HEIGHT)
    ball=Ball(WIDTH//2,HEIGHT//2,10)
    left_score=0
    right_score=0

    while run:
        clock.tick(FPS)
        draw(WIN,[left_paddle,right_paddle],ball,left_score,right_score)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
        keys=pygame.key.get_pressed()
        left_paddle_move(left_paddle)
        ball.move()
        paddle_move(keys,left_paddle,right_paddle)
        
        collision(ball,left_paddle,right_paddle,BALL_VEL)
        if ball.x<0:
            right_score+=1
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            GOAL.play()
        elif ball.x>WIDTH:
            left_score+=1
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            GOAL.play()
        
        won = False
        if left_score >= WINNING_SCORE:
            won = True
            win_text = "Left Player Won!"
        elif right_score >= WINNING_SCORE:
            won = True
            win_text = "Right Player Won!"

        if won:
            text = SCORE_FONT.render(win_text, 1, WHITE)
            WIN.blit(text, (WIDTH//2 - text.get_width() //
                            2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0

    pygame.quit()

if __name__=="__main__":
    main()