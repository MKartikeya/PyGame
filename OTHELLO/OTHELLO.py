import pygame
import time
import os
import numpy as np
pygame.init()
pygame.font.init()
WIDTH,HEIGHT=800,800
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("OTHELLO")
FPS=60
BACKGROUND=pygame.image.load('back.png').convert()
BACKGROUND=pygame.transform.scale(BACKGROUND,(WIDTH,HEIGHT))
COIN_RADIUS=40
SCORE=pygame.font.SysFont("arial",20)
def score(white_pos,black_pos):
    whites=white_pos.sum()
    blacks=black_pos.sum()
    black_text=SCORE.render(f"SCORE: {blacks}",1,(72,72,72))
    white_text=SCORE.render(f"SCORE: {whites}",1,(72,72,72))
    WIN.blit(white_text,(20,20))
    WIN.blit(black_text,(WIDTH-black_text.get_width()-10,20))
    pygame.display.update()
def winner(text):
    WINNER_FONT=pygame.font.SysFont("arial",80)
    winner_text=WINNER_FONT.render(text,1,(255,255,0))
    WIN.blit(winner_text,(WIDTH//2-winner_text.get_width()//2,HEIGHT//2-winner_text.get_height()//2))
    pygame.display.update()
    time.sleep(5)
    main()

    
def coin_display(color,box_x,box_y,white_pos,black_pos):
    if color=='black':
        pygame.draw.circle(WIN,(0,0,0),((box_x)*100+50,box_y*100+50),COIN_RADIUS)
        black_pos[box_x][box_y]=1
        white_pos[box_x][box_y]=0

    elif color=='green':
        pygame.draw.circle(WIN,(0, 128, 0),((box_x)*100+50,box_y*100+50),COIN_RADIUS)
    else:
        pygame.draw.circle(WIN,(255,255,255),((box_x)*100+50,box_y*100+50),COIN_RADIUS)
        white_pos[box_x][box_y]=1
        black_pos[box_x][box_y]=0
    pygame.display.update()
    
def draw():
    WIN.blit(BACKGROUND,(0,0))
    pygame.display.update()

def pos_check(position,white_pos,black_pos):
    if(white_pos[position[0]//100][position[1]//100]==0 and black_pos[position[0]//100][position[1]//100]==0): return True
    else: return False

def flip_check(color,box_x,box_y,white_pos,black_pos):
    if color=='black':
        # vertical
        for i in range(0,8):
            if i!=0:

                if(box_x-i in range(0,8) and white_pos[box_x-i][box_y]!=1 and black_pos[box_x-i][box_y]==0):
                        break
                elif box_x-i in range(0,8):
                    if black_pos[box_x-i][box_y]==1:
                        for j in range(box_x-i+1,box_x):
                                coin_display(color,j,box_y,white_pos,black_pos)
                        break
        for i in range(0,8):
            if i!=0:
                if(box_x+i in range(0,8) and white_pos[box_x+i][box_y]!=1  and black_pos[box_x+i][box_y]==0):
                        break
                elif box_x+i in range(0,8):
                    if black_pos[box_x+i][box_y]==1:
                        for j in range(box_x+1,box_x+i):
                                coin_display(color,j,box_y,white_pos,black_pos)
                        break
        # horizontal
        for i in range(0,8):
            if i!=0:
                if(box_y-i in range(0,8) and white_pos[box_x][box_y-i]!=1 and black_pos[box_x][box_y-i]==0):
                        break
                elif box_y-i in range(0,8):
                    if black_pos[box_x][box_y-i]==1:
                        for j in range(box_y-i+1,box_y):
                                coin_display(color,box_x,j,white_pos,black_pos)
                        break
        for i in range(0,8):
            if i!=0:
                if(box_y+i in range(0,8) and white_pos[box_x][box_y+i]!=1 and black_pos[box_x][box_y+i]==0):
                        break
                elif box_y+i in range(0,8):
                    if black_pos[box_x][box_y+i]==1:
                        for j in range(box_y+1,box_y+i):
                                coin_display(color,box_x,j,white_pos,black_pos)
                        break
        # diagnol
        for i in range(0,8):
            print("yes")
            if i!=0:
                print(box_x,box_y)
                if(box_x+i in range(0,8) and box_y+i in range(0,8) and white_pos[box_x+i][box_y+i]!=1 and black_pos[box_x+i][box_y+i]==0):
                        print("NO2")
                        break
                elif box_x+i in range(0,8) and box_y+i in range(0,8):
                    print("YES")
                    print(i)
                    print(white_pos[box_x+i][box_x+i])
                    if black_pos[box_x+i][box_y+i]==1:
                        print("YYEESS")
                        for j in range(1,i):
                                coin_display(color,box_x+j,box_y+j,white_pos,black_pos)
                        break


        for i in range(0,8):
            if i!=0:

                if(box_x-i in range(0,8) and box_y-i in range(0,8) and white_pos[box_x-i][box_y-i]!=1 and black_pos[box_x-i][box_y-i]==0):
                        break
                elif box_x-i in range(0,8) and box_y-i in range(0,8):
                    if black_pos[box_x-i][box_y-i]==1:
                        for j in range(-i+1,0):
                                coin_display(color,box_x+j,box_y+j,white_pos,black_pos)
                        break
        

        for i in range(0,8):
            if i!=0:
                if(box_x-i in range(0,8) and box_y+i in range(0,8) and white_pos[box_x-i][box_y+i]!=1 and black_pos[box_x-i][box_y+i]==0):
                        break
                elif box_x-i in range(0,8) and box_y+i in range(0,8):
                    if black_pos[box_x-i][box_y+i]==1:
                        for j in range(1,i):
                                coin_display(color,box_x-j,box_y+j,white_pos,black_pos)
                        break


        for i in range(0,8):
            if i!=0:

                if(box_x+i in range(0,8) and box_y-i in range(0,8) and white_pos[box_x+i][box_y-i]!=1 and black_pos[box_x+i][box_y-i]==0):
                        break
                elif box_x+i in range(0,8) and box_y-i in range(0,8):
                    if black_pos[box_x+i][box_y-i]==1:
                        for j in range(1,i):
                                coin_display(color,box_x+j,box_y-j,white_pos,black_pos)
                        break
    else:
         # vertical
        for i in range(0,8):
            if i!=0:

                if(box_x-i in range(0,8) and white_pos[box_x-i][box_y]!=1 and black_pos[box_x-i][box_y]==0):
                        break
                elif box_x-i in range(0,8):
                    if white_pos[box_x-i][box_y]==1:
                        for j in range(box_x-i+1,box_x):
                                coin_display(color,j,box_y,white_pos,black_pos)
                        break
        for i in range(0,8):
            if i!=0:
                if(box_x+i in range(0,8) and white_pos[box_x+i][box_y]!=1  and black_pos[box_x+i][box_y]==0):
                        break
                elif box_x+i in range(0,8):
                    if white_pos[box_x+i][box_y]==1:
                        for j in range(box_x+1,box_x+i):
                                coin_display(color,j,box_y,white_pos,black_pos)
                        break
        # horizontal
        for i in range(0,8):
            if i!=0:
                if(box_y-i in range(0,8) and white_pos[box_x][box_y-i]!=1 and black_pos[box_x][box_y-i]==0):
                        break
                elif box_y-i in range(0,8):
                    if white_pos[box_x][box_y-i]==1:
                        for j in range(box_y-i+1,box_y):
                                coin_display(color,box_x,j,white_pos,black_pos)
                        break
        for i in range(0,8):
            if i!=0:
                if(box_y+i in range(0,8) and white_pos[box_x][box_y+i]!=1 and black_pos[box_x][box_y+i]==0):
                        break
                elif box_y+i in range(0,8):
                    if white_pos[box_x][box_y+i]==1:
                        for j in range(box_y+1,box_y+i):
                                coin_display(color,box_x,j,white_pos,black_pos)
                        break
        # diagnol
        for i in range(0,8):
            if i!=0:
                if(box_x+i in range(0,8) and box_y+i in range(0,8) and white_pos[box_x+i][box_y+i]!=1 and black_pos[box_x+i][box_y+i]==0):
                        break
                elif box_x+i in range(0,8) and box_y+i in range(0,8):
                    if white_pos[box_x+i][box_y+i]==1:
                        for j in range(1,i):
                                coin_display(color,box_x+j,box_y+j,white_pos,black_pos)
                        break


        for i in range(0,8):
            if i!=0:

                if(box_x-i in range(0,8) and box_y-i in range(0,8) and white_pos[box_x-i][box_y-i]!=1 and black_pos[box_x-i][box_y-i]==0):
                        break
                elif box_x-i in range(0,8) and box_y-i in range(0,8):
                    if white_pos[box_x-i][box_y-i]==1:
                        for j in range(-i+1,0):
                                coin_display(color,box_x+j,box_y+j,white_pos,black_pos)
                        break
        

        for i in range(0,8):
            if i!=0:
                if(box_x-i in range(0,8) and box_y+i in range(0,8) and white_pos[box_x-i][box_y+i]!=1 and black_pos[box_x-i][box_y+i]==0):
                        break
                elif box_x-i in range(0,8) and box_y+i in range(0,8):
                    if white_pos[box_x-i][box_y+i]==1:
                        for j in range(1,i):
                                coin_display(color,box_x-j,box_y+j,white_pos,black_pos)
                        break


        for i in range(0,8):
            if i!=0:

                if(box_x+i in range(0,8) and box_y-i in range(0,8) and white_pos[box_x+i][box_y-i]!=1 and black_pos[box_x+i][box_y-i]==0):
                        break
                elif box_x+i in range(0,8) and box_y-i in range(0,8):
                    if white_pos[box_x+i][box_y-i]==1:
                        for j in range(1,i):
                                coin_display(color,box_x+j,box_y-j,white_pos,black_pos)
                        break
def main():
    clock=pygame.time.Clock()
    run=True
    draw()
    coin_display('green',3,4,0,0)
    coin_display('green',4,3,0,0)
    coin_display('green',3,3,0,0)
    coin_display('green',4,4,0,0)
    turn=1
    white_pos=np.zeros((8,8))
    black_pos=np.zeros((8,8))
    PLAY_FONT=pygame.font.SysFont("arial",80)
    play_text=PLAY_FONT.render('PLAY',1,(255,0,0))
    WIN.blit(play_text,(WIDTH//2-play_text.get_width()//2,HEIGHT//2-play_text.get_height()//2))
    pygame.display.update()
    time.sleep(2)
    draw()
    coin_display('black',3,4,white_pos,black_pos)
    coin_display('black',4,3,white_pos,black_pos)
    coin_display('white',3,3,white_pos,black_pos)
    coin_display('white',4,4,white_pos,black_pos)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
            if event.type==pygame.MOUSEBUTTONDOWN:
                position=pygame.mouse.get_pos()
                box_x=(position[0]//100)
                box_y=(position[1]//100)
                if pos_check(position,white_pos,black_pos):
                    if turn==1:
                        turn=0
                        coin_display('black',box_x,box_y,white_pos,black_pos)
                        flip_check('black',box_x,box_y,white_pos,black_pos)
                        # score(white_pos,black_pos)
                        print(black_pos)
                    else:
                        coin_display('white',box_x,box_y,white_pos,black_pos)
                        flip_check('white',box_x,box_y,white_pos,black_pos)
                        # score(white_pos,black_pos)
                        turn=1
                    if(black_pos.sum()+white_pos.sum()==64):
                        if(black_pos.sum()>white_pos.sum()):
                            winner('BLACK WINS!!')
                        elif(black_pos.sum()<white_pos.sum()):
                            winner('WHITE WINS!!')
                        else:
                            winner('TIE!!')

    
    pygame.quit()

if __name__=="__main__":
    main()