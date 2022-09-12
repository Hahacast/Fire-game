# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 21:58:59 2020

@author: user
"""


import pygame

class block (pygame.sprite.Sprite):
    def __init__(self , left , top , width , height):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(left , top , width , height)

class Map():
    def __init__(self):
        self.blockGroup = pygame.sprite.Group()
        #房子的外牆 由左下3開始屬
        self.wall = block( 203 , 642 ,29 , 89 )
        self.blockGroup.add(self.wall)
        
        self.wall = block( 203 , 731 ,634 , 29 )
        self.blockGroup.add(self.wall)    
        
        self.wall = block( 957 , 731 ,418 , 34 )
        self.blockGroup.add(self.wall)
        
        self.wall = block( 1345 , 517 ,31 , 247 )
        self.blockGroup.add(self.wall)    

        self.wall = block( 1345 , 127 ,28 , 269 )
        self.blockGroup.add(self.wall)

        self.wall = block( 732 , 127 ,641 , 28 )
        self.blockGroup.add(self.wall)

        self.wall = block( 205 , 127 ,406 , 28 )
        self.blockGroup.add(self.wall)

        self.wall = block( 205 , 127 ,28, 151 )
        self.blockGroup.add(self.wall)   

        self.wall = block( 205 , 404 ,30, 92 )
        self.blockGroup.add(self.wall)                        
        #door
        self.door = block( 102 , 492 ,130, 29 )
        self.blockGroup.add(self.door)              
        self.door= block( 595 , 149 ,19, 124 )
        self.blockGroup.add(self.door)  
        
        #箱子
        self.wood= block( 613 , 734 ,84, 73 )
        self.blockGroup.add(self.wood)  

        self.wood= block( 270 , 821 ,88, 79 )
        self.blockGroup.add(self.wood)          
        
        #室內設計
        
        self.design= block(224 , 404 ,251, 37 ) #橫的內牆
        self.blockGroup.add(self.design)  

        self.design= block(429 , 147 ,40, 155 ) #橫的內牆
        self.blockGroup.add(self.design)  

        self.design= block(900 , 148 ,38, 256 ) #橫的內牆
        self.blockGroup.add(self.design)    

        self.design= block(1027 , 472 ,165, 78 ) #橫的內牆
        self.blockGroup.add(self.design)           
        
        #柱子
        
        self.design= block(278 , 190 ,46, 44 ) 
        self.blockGroup.add(self.design) 
        
        self.design= block(347 , 578 ,55, 52 ) 
        self.blockGroup.add(self.design)   

        
        
        