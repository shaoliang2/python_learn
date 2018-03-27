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
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建一艘飞船
    ship=Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets=Group()
        
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        #print(len(bullets))

        gf.update_screen(ai_settings,screen,ship,bullets)
        
run_game()