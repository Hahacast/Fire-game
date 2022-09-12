# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 11:32:23 2020

@author: user
"""


import pygame

import wall
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.bullet_up = pygame.image.load(r"..\image\bullet_down.png")
        self.bullet_down = pygame.image.load(r"..\image\bullet_down.png")
        self.bullet_left = pygame.image.load(r"..\image\bullet_right.png")
        self.bullet_right = pygame.image.load(r"..\image\bullet_right.png")
        
        self.dir_x, self.dir_y = 0, 0
        self.speed  = 50
        self.life   = False
        self.strong = False


        self.rect = self.bullet_down.get_rect()
        self.rect.left, self.rect.right = 0,0
    def changeImage(self, dir_x, dir_y):
        self.dir_x, self.dir_y = dir_x, dir_y
        if self.dir_x == 0 and self.dir_y == -1:
            self.rect = self.bullet_up.get_rect()
            self.bullet = self.bullet_up
        elif self.dir_x == 0 and self.dir_y == 1:
            self.rect = self.bullet_down.get_rect()
            self.bullet = self.bullet_down
        elif self.dir_x == -1 and self.dir_y == 0:
            self.rect = self.bullet_down.get_rect()
            self.rect = self.bullet_left.get_rect()
            self.bullet = self.bullet_left
        elif self.dir_x == 1 and self.dir_y == 0:
            self.rect = self.bullet_right.get_rect()
            self.bullet = self.bullet_right
            
    def move(self):
     
        self.rect = self.rect.move(self.speed * self.dir_x,
                                   self.speed * self.dir_y)
                
        # Åö×²µØÍ¼±ßÔµ
        if self.rect.top < 3:
            self.life = False
        #    self.rect.left, self.rect.right = 3 + 12 * 24, 3 + 24 * 24
        if self.rect.bottom > 900 - 3:
            self.life = False
        #    self.rect.left, self.rect.right = 3 + 12 * 24, 3 + 24 * 24
        if self.rect.left < 3:
            self.life = False
        #    self.rect.left, self.rect.right = 3 + 12 * 24, 3 + 24 * 24
        if self.rect.right > 1600 - 3:
            self.life = False