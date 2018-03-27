# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 20:21:39 2018

@author: Administrator
"""

import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建一艘飞船
    ship=Ship(screen)
    
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)
        
run_game()