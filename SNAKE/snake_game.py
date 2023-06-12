import pygame as py
import sys
from settings import Settings
from snake import Snake
import game_functions as gf

def run_game():
    ai_settings=Settings()
    py.init()
    screen=py.display.set_mode((ai_settings.width,ai_settings.height))
    snake=Snake(ai_settings,screen)
    while True:
        screen.fill(ai_settings.bg_color)
        snake.blitme()
        gf.check_events(snake)
        snake.update()
        py.display.flip()


run_game()
     


