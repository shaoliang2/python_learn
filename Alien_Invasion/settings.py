# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 20:54:10 2018

@author: Administrator
"""

class Settings():
    """存储所有设置的类"""
    
    def __init__(self):
        """初始化设置"""
        #屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)

        #飞船的设置
        self.ship_speed_factor=1.5

        self.bullet_speed_factor=3
        self.bullet_width=300
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullets_allowed=10

        #外星人设置
        self.alien_speed_factor=1
        self.fleet_drop_speed=100
        #fleet_direction=1向右，-1向左
        self.fleet_direction=1