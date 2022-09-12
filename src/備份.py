# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:49:23 2020

@author: user
"""

import sys
import pygame 
import mySoldier

def main():
    pygame.init()
    
    resolution = 1400 , 800
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("fire game ")
    #初始化字體

    #加載圖片
    background_image = pygame .image.load(r"..\image\白背景.png").convert_alpha()



    allsoldierGroup   = pygame.sprite.Group()

    
    mySoldier_T1 = mySoldier.MySoldier(1)
    allsoldierGroup.add(mySoldier_T1)

    mySoldier_T2 = mySoldier.MySoldier(2)
    allsoldierGroup.add(mySoldier_T2)
  
    
    
    
    
    
    
    #創建player1射擊延遲 1秒     
       
    MYBULLETNOTCOOLINGEVENT_1 = pygame.constants.USEREVENT
    pygame.time.set_timer(MYBULLETNOTCOOLINGEVENT_1, 200)
    #創建player2射擊延遲 1秒
    MYBULLETNOTCOOLINGEVENT_2 = pygame.constants.USEREVENT+1
    pygame.time.set_timer(MYBULLETNOTCOOLINGEVENT_2, 1000)  
    

    delay = 100
    moving = 0
    
    continuous_1 = 0
    continuous_2 = 0
    movdir = 0
    moving2 = 0
    movdir2 = 0
    enemyNumber = 3
    enemyCouldMove      = True
    switch_R1_R2_image  = True
    homeSurvive         = True
    running_T1          = True
    running_T2          = True
    clock = pygame .time.Clock()



   
    
    while True:
        for event in pygame .event.get():
            if event.type == pygame .QUIT:
                pygame .quit()
                sys.exit()
            # 我方子弹冷却事件
            if event.type == MYBULLETNOTCOOLINGEVENT_1:
                mySoldier_T1.bulletNotCooling = True
            if event.type == MYBULLETNOTCOOLINGEVENT_2:
                mySoldier_T2.bulletNotCooling = True
                

                
        #檢查玩家的鍵盤操作        
        key_pressed = pygame .key.get_pressed()    
        #玩家1的移動操作
        
        if moving:
            moving -= 1
            if movdir == 0:
                allsoldierGroup.remove(mySoldier_T1)
                if continuous_1 == movdir:
                    mySoldier_T1.moveUp(1, allsoldierGroup)
                else:
                    mySoldier_T1.moveUp(0, allsoldierGroup)
                allsoldierGroup.add(mySoldier_T1)
                running_T1 = True      
            if movdir == 1:
                allsoldierGroup.remove(mySoldier_T1)
                if continuous_1 == movdir:
                    mySoldier_T1.moveDown(1, allsoldierGroup)
                else:
                    mySoldier_T1.moveDown(0, allsoldierGroup)
                allsoldierGroup.add(mySoldier_T1)
                running_T1 = True
            if movdir == 2:
                allsoldierGroup.remove(mySoldier_T1)
                if continuous_1 == movdir:
                    mySoldier_T1.moveLeft(1, allsoldierGroup)
                else:
                    mySoldier_T1.moveLeft(0, allsoldierGroup)
                allsoldierGroup.add(mySoldier_T1)
                running_T1 = True
            if movdir == 3:
                allsoldierGroup.remove(mySoldier_T1)
                if continuous_1 == movdir:
                    mySoldier_T1.moveRight(1, allsoldierGroup)
                else:
                    mySoldier_T1.moveRight(0, allsoldierGroup) 
                allsoldierGroup.add(mySoldier_T1)
                running_T1 = True

        if not moving:
            
            if key_pressed[pygame.K_w]:
                moving = 7
                movdir = 0
                running_T1 = True
                allsoldierGroup.remove(mySoldier_T1)
                if continuous_1 == movdir:
                    if mySoldier_T1.moveUp(1, allsoldierGroup):
                        moving = 0 
                else:
                    if mySoldier_T1.moveUp(0, allsoldierGroup):
                        moving = 0
                allsoldierGroup.add(mySoldier_T1)
            if key_pressed[pygame.K_s]:
                moving = 7
                movdir = 1
                running_T1 = True
                allsoldierGroup.remove(mySoldier_T1)
                if continuous_1 == movdir:
                    if mySoldier_T1.moveDown(1, allsoldierGroup):
                        moving = 0 
                else:
                    if mySoldier_T1.moveDown(0, allsoldierGroup):
                        moving = 0
                allsoldierGroup.add(mySoldier_T1)
            if key_pressed[pygame.K_a]:
                moving = 7
                movdir = 2
                running_T1 = True
                allsoldierGroup.remove(mySoldier_T1)
                if continuous_1 == movdir:
                    if mySoldier_T1.moveLeft(1, allsoldierGroup):
                        moving = 0 
                else:
                    if mySoldier_T1.moveLeft(0, allsoldierGroup):

                        moving = 0
                allsoldierGroup.add(mySoldier_T1)
            if key_pressed[pygame.K_d]:
                moving = 7
                movdir = 3
                running_T1 = True
                allsoldierGroup.remove(mySoldier_T1)
                if continuous_1 == movdir:
                    if mySoldier_T1.moveRight(1, allsoldierGroup):
                        moving = 0 
                else:
                    if mySoldier_T1.moveRight(0, allsoldierGroup):
                        moving = 0
                allsoldierGroup.add(mySoldier_T1)
                
        if key_pressed[pygame.K_j]:
            if not mySoldier_T1.bullet.life and mySoldier_T1.bulletNotCooling:
               mySoldier_T1.shoot()
               mySoldier_T1.bulletNotCooling = False
               
               
               
               
        #玩家2的鍵盤操作
        #玩家2的移動操作 
#        if moving2:
#            moving2 -= 1
#            if movdir2 == 0:
#                allsoldierGroup.remove(mySoldier_T2)
#                if continuous_2 == movdir2:
#                    mySoldier_T2.moveUp(1, allsoldierGroup)
#                else:
###                    mySoldier_T2.moveUp(0, allsoldierGroup)
##                allsoldierGroup.add(mySoldier_T2)
#                running_T2 = True
##            if movdir2 == 1:
#                allsoldierGroup.remove(mySoldier_T2)
#                if continuous_2 == movdir2:
#                    mySoldier_T2.moveDown(1, allsoldierGroup)
#                else:
#                    mySoldier_T2.moveDown(0, allsoldierGroup)
#                allsoldierGroup.add(mySoldier_T2)
#                running_T2 = True
#            if movdir2 == 2:
#                allsoldierGroup.remove(mySoldier_T2)
#                if continuous_2 == movdir2:
#                    mySoldier_T2.moveLeft(1, allsoldierGroup)
#                else:
#                    mySoldier_T2.moveLeft(0, allsoldierGroup)
##                allsoldierGroup.add(mySoldier_T2)
#            if movdir2 == 3:
#                allsoldierGroup.remove(mySoldier_T2)
#                if continuous_2 == movdir2:
#                    mySoldier_T2.moveRight(1, allsoldierGroup)
#                else:
##                    mySoldier_T2.moveRight(0, allsoldierGroup)
#                allsoldierGroup.add(mySoldier_T2)
#                running_T2 = True
        
        if 1:
            if key_pressed[pygame.K_UP]:
                moving2 = 7
                movdir2 = 0
                running_T2 = True
                allsoldierGroup.remove(mySoldier_T2)
                if continuous_2 == movdir2:
                    mySoldier_T2.moveUp(1, allsoldierGroup)
                    moving2 = 0 
                else:
                    mySoldier_T2.moveUp(0, allsoldierGroup)
                    moving2 = 0
                allsoldierGroup.add(mySoldier_T2)
            if key_pressed[pygame.K_DOWN]:
                moving2 = 7
                movdir2 = 1
                running_T2 = True
                allsoldierGroup.remove(mySoldier_T2)
                if continuous_2 == movdir2:
                    mySoldier_T2.moveDown(1, allsoldierGroup)
                    moving2 = 0 
                else:
                    mySoldier_T2.moveDown(0, allsoldierGroup)
                    moving2 = 0
                allsoldierGroup.add(mySoldier_T2)
            if key_pressed[pygame.K_LEFT]:
                moving2 = 7
                movdir2 = 2
                running_T2 = True
                allsoldierGroup.remove(mySoldier_T2)
                       
                if continuous_2 == movdir2:
                    mySoldier_T2.moveLeft(1, allsoldierGroup)
                    moving2 = 0 
                else:
                    mySoldier_T2.moveLeft(0, allsoldierGroup)
                    moving2 = 0
                allsoldierGroup.add(mySoldier_T2)
            if key_pressed[pygame.K_RIGHT]:
                moving2 = 7
                movdir2 = 3
                running_T2 = True
                allsoldierGroup.remove(mySoldier_T2)
                if continuous_2 == movdir2:
                    mySoldier_T2.moveRight(1, allsoldierGroup)
                    moving2 = 0 
                else:
                    mySoldier_T2.moveRight(0, allsoldierGroup)
                    moving2 = 0
                allsoldierGroup.add(mySoldier_T2)                       
        if key_pressed[pygame.K_KP0]:
            if not mySoldier_T2.bullet.life and mySoldier_T2.bulletNotCooling:
               mySoldier_T2.shoot()
               mySoldier_T2.bulletNotCooling = False
               
               

        #繪製背景
        screen.blit(background_image, (0, 0))
        #繪製子彈1
        if mySoldier_T1.bullet.life:
            mySoldier_T1.bullet.move()
            # 子彈1是否射到玩家2
            if  pygame.sprite.collide_rect(mySoldier_T1.bullet,mySoldier_T2):
                mySoldier_T2.life -= 15
                mySoldier_T1.bullet.life = False
                if mySoldier_T2.life <= 0:
                    mySoldier_T2.soldier_R0 = pygame.image.load(r"..\image\dead.png").convert_alpha()
            else:
                screen.blit(mySoldier_T1.bullet.bullet, mySoldier_T1.bullet.rect)
            
                
                
        #繪製子彈2    
        if mySoldier_T2.bullet.life:
            mySoldier_T2.bullet.move()  
            # 子彈2與玩家1
            if  pygame.sprite.collide_rect(mySoldier_T2.bullet,mySoldier_T1):
                mySoldier_T1.life -= 50
                mySoldier_T2.bullet.life = False  
                if mySoldier_T1.life <= 0:
                    mySoldier_T1.soldier_R0 = pygame.image.load(r"..\image\dead.png").convert_alpha()
            else:
                screen.blit(mySoldier_T2.bullet.bullet, mySoldier_T2.bullet.rect)
            
    
         
               
    
        #繪製槍兵            
        screen.blit(mySoldier_T1.soldier_R0, (mySoldier_T1.rect.left, mySoldier_T1.rect.top))
        
        
        
        screen.blit(mySoldier_T2.soldier_R0, (mySoldier_T2.rect.left, mySoldier_T2.rect.top))
        
        #繪製文字
        font1 = pygame.font.SysFont("arial", 16) #槍兵1的血量
        font1_surface = font1.render(str(mySoldier_T1.life), True, (67, 89, 171))
        screen.blit(font1_surface , (mySoldier_T1.rect.left+15  ,mySoldier_T1.rect.top-20) )
        
        
        font2 = pygame.font.SysFont("arial", 16) #槍兵2的血量
        font2_surface = font2.render(str(mySoldier_T2.life), True, (227,23, 13))
        screen.blit(font2_surface , (mySoldier_T2.rect.left+15  ,mySoldier_T2.rect.top-20) )
        
        
        
        
        
        
        
        delay -= 1
        if not delay:
            delay = 100
        
        continuous_1 = movdir
        continuous_2 = movdir2
        pygame.display.update()
        if mySoldier_T1.life <= 0 or mySoldier_T2.life <= 0:
            gameover()
        clock.tick(144)
        


def gameover():
    pygame.time.delay(5000)
    main()

if __name__ == "__main__":
        main()
