# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 22:44:03 2020

@author: user
"""



import pygame
import bulletClass
import wall

soldier_T1 = r"..\image\action.png"
soldier_T2 = r"..\image\action.png"
Square_size = ( 60 , 60)
Square_size_up = (49,59)
Square_size_down = (49,59)
Square_size_left = (57 , 61)
Square_size_right = (57 , 61)


class MySoldier(pygame.sprite.Sprite):
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber
        pygame.sprite.Sprite.__init__(self)
        self.life = True
        if playerNumber == 1:
            self.soldier_image = pygame.image.load(soldier_T1).convert_alpha()
            
        if playerNumber == 2:
            self.soldier_image = pygame.image.load(soldier_T2).convert_alpha()
        self.soldier = self.soldier_image
        

        self.soldier_R0 = self.soldier.subsurface((555,41),Square_size_down )
        self.soldier_R1 = self.soldier.subsurface((555,41),Square_size_down )
        self.rect = self.soldier_R0.get_rect()
        
        #player1、player2起始位置
        if playerNumber == 1:
            self.rect.left, self.rect.top = 42,  631
            self.clip = 30
            self.speed = 2
        if playerNumber == 2:
            self.rect.left, self.rect.top = 1447 , 211
            self.clip = 7
            self.speed = 2
            
        self.dir_x, self.dir_y = 0, 1
        self.life = 100

        self.bulletNotCooling = True
        self.bullet = bulletClass.Bullet()
        self.action = 0 #0~5
        self.continuous_count = 0
        self.bgmap = wall.Map()

    #這裡
        
    def shoot(self):

        self.bullet.life = True
        self.clip -= 1
        self.bullet.changeImage(self.dir_x, self.dir_y)
        
        if self.dir_x == 0 and self.dir_y == -1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.bottom = self.rect.top + 1
            if pygame.sprite.spritecollideany(self.bullet, self.bgmap.blockGroup):
                self.bullet.life = False
        elif self.dir_x == 0 and self.dir_y == 1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.top = self.rect.bottom -1
            if pygame.sprite.spritecollideany(self.bullet, self.bgmap.blockGroup):
                self.bullet.life = False
        elif self.dir_x == -1 and self.dir_y == 0:
            self.bullet.rect.right = self.rect.left + 20
            self.bullet.rect.top = self.rect.top + 25
            if pygame.sprite.spritecollideany(self.bullet, self.bgmap.blockGroup):
                self.bullet.life = False
        elif self.dir_x == 1 and self.dir_y == 0:
            self.bullet.rect.left = self.rect.right -20
            self.bullet.rect.top = self.rect.top + 25
            if pygame.sprite.spritecollideany(self.bullet, self.bgmap.blockGroup):
                self.bullet.life = False

    def moveUp(self , re, allsoldierGroup , blockGroup):
        self.rect = self.rect.move(self.speed * 0, self.speed * -1)
        #判斷是否連續走上，是的話走路動畫
        if re == 1:
            self.continuous_count += 1
            if  self.action == 5 :
              self.action = 0
            
            if self.continuous_count % 15 == 0:
                self.action += 1
                self.continuous_count == 0
        else:
            self.continuous = 0
            self.action = 0
        self.soldier_R0 = self.soldier_image.subsurface((27, 41 + 100*self.action),Square_size_up )
        self.dir_x, self.dir_y = 0, -1     
        if self.rect.top < 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            return True
        if  pygame.sprite.spritecollide(self, allsoldierGroup, False, None):  
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            return True
        if  pygame.sprite.spritecollide(self, blockGroup, False, None):  
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            return True
        return False
    def moveDown(self , re , allsoldierGroup , blockGroup ):     
        if re == 1:
            self.continuous_count += 1
            if  self.action == 5 :
              self.action = 0
              
            if self.continuous_count % 15 == 0:
                self.action += 1
                self.continuous_count == 0
        else:           
            self.continuous = 0
            self.action = 0
        self.rect = self.rect.move(self.speed * 0, self.speed * 1)
        self.soldier_R0 = self.soldier_image.subsurface((553, 41 + 100*self.action),Square_size_down )
        self.dir_x, self.dir_y = 0, 1
        if self.rect.bottom > 900 - 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            return True 
        if  pygame.sprite.spritecollide(self, allsoldierGroup, False, None):  
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            return True
        if  pygame.sprite.spritecollide(self,blockGroup, False, None):  
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            return True        
        return False         
    def moveLeft(self , re, allsoldierGroup , blockGroup):
        if re == 1:
            self.continuous_count += 1
            if  self.action == 5 :
              self.action = 0
            
            if self.continuous_count % 15 == 0:
                self.action += 1
                self.continuous_count == 0
            

        else:
            self.continuous = 0
            self.action = 0        
    
        self.rect = self.rect.move(self.speed * -1, self.speed * 0)
        self.soldier_R0 = self.soldier_image.subsurface((185, 41 + 100*self.action),Square_size_left )
        self.dir_x, self.dir_y = -1, 0   
        if self.rect.left < 3:
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            return True        
        if  pygame.sprite.spritecollide(self, allsoldierGroup, False, None):  
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            return True  
        if  pygame.sprite.spritecollide(self, blockGroup, False, None):  
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            return True  
        return False       
    def moveRight(self , re, allsoldierGroup , blockGroup):
        
        if re == 1:
            self.continuous_count += 1
            if  self.action == 5 :
              self.action = 0
            
            if self.continuous_count % 15 == 0:
                self.action += 1
                self.continuous_count == 0
        else:
            self.continuous_count = 0
            self.action = 0            
        self.rect = self.rect.move(self.speed * 1, self.speed * 0)
        self.soldier_R0 = self.soldier_image.subsurface((365, 41 + 100*self.action),Square_size_right )
        self.dir_x, self.dir_y = 1, 0
        if self.rect.right > 1600 - 3:
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            return True
        if  pygame.sprite.spritecollide(self, allsoldierGroup, False, None):  
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            return True 
        if  pygame.sprite.spritecollide(self, blockGroup, False, None):  
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            return True 
        return False

        
        
        
        
        
        
        
        
        
        