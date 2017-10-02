#alien_invasion.py
import sys 
import pygame
from setting import Settings
from ship import Ship
import  game_functions as gf 
from Alien import Alien

from pygame.sprite import Group
from game_stats import Gamestats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("alien invasion")
    play_button=Button(ai_settings,screen,"play")
    stats=Gamestats(ai_settings)
    ship=Ship(ai_settings,screen)
    bullets=Group()
    #alien=Alien(ai_settings,screen)
    aliens=Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    sb=Scoreboard(ai_settings,screen,stats)

    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            #bullets.update()
            
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            
            #for bulle in bullets.copy():
                #if bullet.rect.bottom<=0:
                    #bullets.remove(bullet)
            #print(len(bullets))
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets) 

        gf.update_screen(ai_settings,screen,stats,  sb, ship,aliens,bullets,play_button) 
				

run_game()

