import pygame as py
import sys

def draw(ai_settings):
    py.display.set_mode((ai_settings.width,ai_settings.height))
    py.display.set_caption('SNAKE GAME')
def check_events(snake):
    for event in py.event.get():
        if event.type==py.QUIT:
            sys.exit()
        elif event.type == py.KEYDOWN:
            check_keydown_events(event,snake)

def check_keydown_events(event,snake):
    if event.key==py.K_UP and not snake.moving_down:
        snake.moving_right=False
        snake.moving_left=False
        snake.moving_down=False
        snake.moving_up=True
    elif event.key==py.K_DOWN and not snake.moving_up:
        snake.moving_up=False
        snake.moving_right=False
        snake.moving_left=False
        snake.moving_down=True
    elif event.key==py.K_RIGHT and not snake.moving_left:
        snake.moving_up=False
        snake.moving_left=False
        snake.moving_down=False
        snake.moving_right=True
    elif event.key==py.K_LEFT and not snake.moving_right:
        snake.moving_up=False
        snake.moving_right=False
        snake.moving_down=False
        snake.moving_left=True