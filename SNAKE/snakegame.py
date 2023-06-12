import pygame,sys,random
from pygame import mixer
from pygame.math import Vector2
pygame.init()
FPS=60
# WIDTH,HEIGHT=
CELL_SIZE=40
CELL_NUMBER=20
SCREEN_UPDATE=pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)
class SNAKE():
    def __init__(self):
        self.body=[Vector2(7,10),Vector2(6,10),Vector2(5,10)]
        self.direction=Vector2(1,0)
        self.new=False
        self.head_down=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SNAKE\\head_down.png").convert_alpha()
        self.head_up=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SNAKE\\head_up.png").convert_alpha()
        self.head_left=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SNAKE\\head_left.png").convert_alpha()
        self.head_right=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SNAKE\\head_right.png").convert_alpha()
        self.tail_down=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SNAKE\\tail_down.png").convert_alpha()
        self.tail_up=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SNAKE\\tail_up.png").convert_alpha()
        self.tail_left=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SNAKE\\tail_left.png").convert_alpha()
        self.tail_right=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SNAKE\\tail_right.png").convert_alpha()
        self.body_bl=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SNAKE\\body_bl.png").convert_alpha()
        self.body_br=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SNAKE\\body_br.png").convert_alpha()
        self.body_tl=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SNAKE\\body_tl.png").convert_alpha()
        self.body_tr=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SNAKE\\body_tr.png").convert_alpha()
        self.body_horizontal=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SNAKE\\body_horizontal.png").convert_alpha()
        self.body_vertical=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SNAKE\\body_vertical.png").convert_alpha()
    def draw_snake(self):
        self.update_head()
        self.update_tail()
        # for block in self.body:
        #     x_pos=block.x*CELL_SIZE
        #     y_pos=block.y*CELL_SIZE
        #     block_rect=pygame.Rect(x_pos,y_pos,CELL_SIZE,CELL_SIZE)
        #     pygame.draw.rect(screen,(0,0,255),block_rect)
        for index,block in enumerate(self.body):
            x_pos=block.x*CELL_SIZE
            y_pos=block.y*CELL_SIZE
            block_rect=pygame.Rect(x_pos,y_pos,CELL_SIZE,CELL_SIZE)

            if index==0:
                screen.blit(self.head,block_rect)
            elif index==len(self.body)-1:
                screen.blit(self.tail,block_rect)
            else:
                prev_block=self.body[index+1]-block
                next_block=self.body[index-1]-block
                if prev_block.x==next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif prev_block.y==next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if (prev_block.x==-1 and next_block.y==-1) or (prev_block.y==-1 and next_block.x==-1):
                        screen.blit(self.body_tl,block_rect) 
                    elif (prev_block.x==-1 and next_block.y==1) or (prev_block.y==1 and next_block.x==-1):
                        screen.blit(self.body_bl,block_rect) 
                    elif (prev_block.x==1 and next_block.y==-1) or (prev_block.y==-1 and next_block.x==1):
                        screen.blit(self.body_tr,block_rect) 
                    elif (prev_block.x==1 and next_block.y==1) or (prev_block.y==1 and next_block.x==1):
                        screen.blit(self.body_br,block_rect) 
            
    
    def update_tail(self):
        tail_dir=self.body[len(self.body)-1]-self.body[len(self.body)-2]
        if tail_dir==Vector2(1,0):
            self.tail=self.tail_right
        elif tail_dir==Vector2(-1,0):
            self.tail=self.tail_left
        elif tail_dir==Vector2(0,-1):
            self.tail=self.tail_up
        elif tail_dir==Vector2(0,1):
            self.tail=self.tail_down

    def update_head(self):
        head_dir=self.body[1]-self.body[0]
        if head_dir==Vector2(1,0):
            self.head=self.head_left
            self.tail=self.tail_right
            self.middle=self.body_horizontal
        elif head_dir==Vector2(-1,0):
            self.head=self.head_right
            self.middle=self.body_horizontal
            self.tail=self.tail_left
        elif head_dir==Vector2(0,-1):
            self.head=self.head_down
            self.tail=self.tail_up
            self.middle=self.body_vertical
        elif head_dir==Vector2(0,1):
            self.head=self.head_up
            self.tail=self.tail_down
            self.middle=self.body_vertical
    def move_snake(self):
        if self.new:
            EATING_SOUND.play()
            body_copy=self.body[:]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body=body_copy[:]
            self.new=False
            self.draw_snake
        else:
            body_copy=self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body=body_copy[:]
    def add_block(self):
        self.new=True
class FRUIT():
    def __init__(self):
        self.randomise()

    def draw_fruit(self):
        fruit_rect=pygame.Rect(self.position.x*CELL_SIZE,self.position.y*CELL_SIZE,CELL_SIZE,CELL_SIZE)
        # pygame.draw.rect(screen,(255,0,0),fruit_rect)
        screen.blit(apple,fruit_rect)
    def randomise(self):
        self.x=random.randint(0,CELL_NUMBER-1)
        self.y=random.randint(0,CELL_NUMBER-1)
        self.position=Vector2(self.x,self.y)

class MAIN():
    def __init__(self):
        self.snake=SNAKE()
        self.fruit=FRUIT()
    def update(self ):
        # print('updated')
        self.snake.move_snake()
        self.check_collision()
        self.check_hit()
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
    def check_collision(self):
        if self.fruit.position==self.snake.body[0]:
            self.fruit.randomise()
            self.snake.add_block()
    def check_hit(self):
        if not 0<=self.snake.body[0].x<CELL_NUMBER or not 0<=self.snake.body[0].y<CELL_NUMBER:
            CRASH_SOUND.play()
            pygame.time.wait(1000)
            self.game_over()
        for block in self.snake.body[1:]:
            if block==self.snake.body[0]:
                CRASH_SOUND.play()
                pygame.time.wait(1000)
                self.game_over()
    def game_over(self):
        pygame.quit()
        sys.exit()
        # pygame.time.delay(3000)
        # self.reset()
    def draw_grass(self):

        grass_color=(167,209,61)
        # print(1)
        for row in range(CELL_NUMBER):
            if row % 2==0:
            #    print(f"EVEN {row}")
               for col in range(CELL_NUMBER):
                    if col % 2==0:
                        grass_rect=pygame.Rect(col*CELL_SIZE,row*CELL_SIZE,CELL_SIZE,CELL_SIZE)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                # print(f"ODD {row}")
                for col in range(CELL_NUMBER):
                    if col % 2 !=0:
                        grass_rect=pygame.Rect(col*CELL_SIZE,row*CELL_SIZE,CELL_SIZE,CELL_SIZE)
                        pygame.draw.rect(screen,grass_color,grass_rect)
    def draw_score(self):
        # score_text=str(len(self.snake.body)-3)
        score_text=f"SCORE: {len(self.snake.body)-3}"
        score_surface=display_font.render(score_text,True,(56,74,12))
        score_x=CELL_SIZE*CELL_NUMBER-100
        score_y=CELL_SIZE*CELL_NUMBER-40
        score_rect=score_surface.get_rect(center=(score_x,score_y))
        # apple_rect=apple.get_rect(midright=(score_rect.left,score_rect.centery))
        screen.blit(score_surface,score_rect)
        # screen.blit(score_surface,apple_rect)
    def reset(self):
        self.snake.body=self.body=[Vector2(7,10),Vector2(6,10),Vector2(5,10)]

screen=pygame.display.set_mode((CELL_SIZE*CELL_NUMBER,CELL_SIZE*CELL_NUMBER))
pygame.display.set_caption("SNAKE GAME")
clock=pygame.time.Clock()
apple=pygame.image.load("C:\\Users\\karti\\Desktop\\PYTHON\\SNAKE\\apple1.png").convert_alpha()
apple=pygame.transform.scale(apple,(CELL_SIZE,CELL_SIZE))
display_font=pygame.font.SysFont('freesansbold.ttf',35)
EATING_SOUND=pygame.mixer.Sound("C:\\Users\\karti\\Desktop\\PYTHON\\SNAKE\\Sound_crunch.wav")
CRASH_SOUND=pygame.mixer.Sound("C:\\Users\\karti\\Desktop\PYTHON\\SNAKE\\plate-break-1-36468.mp3")
main_game=MAIN()
fruit=FRUIT()
snake=SNAKE()
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            break
        if event.type==SCREEN_UPDATE:
            main_game.update()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and main_game.snake.direction.y!=1:
                main_game.snake.direction=Vector2(0,-1)
            if event.key==pygame.K_DOWN and main_game.snake.direction.y!=-1:
                main_game.snake.direction=Vector2(0,1)
            if event.key==pygame.K_LEFT and main_game.snake.direction.x!=1:
                main_game.snake.direction=Vector2(-1,0)
            if event.key==pygame.K_RIGHT and main_game.snake.direction.x!=-1:
                main_game.snake.direction=Vector2(1,0)
    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()