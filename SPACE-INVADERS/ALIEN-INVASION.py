import sys
from game_stats import GameStats
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from button import Button
from pygame.sprite import Group
from time import sleep
from bullet import Bullet
from alien import Alien
def run_game():
    pygame.init()
    bullets = Group()
    aliens=Group()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    play_button = Button(ai_settings, screen, "Play")
    pygame.display.set_caption("Alien Invasion")
    ship=Ship(ai_settings,screen)
    alien = Alien(ai_settings, screen)
    gf.create_fleet(ai_settings, screen,ship, aliens)
    stats=GameStats(ai_settings)

    while True:
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        gf.check_events(ai_settings, screen,stats, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings ,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings, screen,stats, ship,aliens, bullets,play_button)
        # pygame.display.flip()
   

run_game()