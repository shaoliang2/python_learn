# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 20:21:39 2018

@author: Administrator
"""

import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建一艘飞船、一个子弹编组和一个外星人编组
    ship=Ship(ai_settings,screen)
    bullets=Group()
    aliens=Group()
        
    #创建外星人群
    gf.create_fleet(ai_settings,screen,aliens)
    #aline=Alien(ai_settings,screen)
    
    #开始主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
        
run_game()