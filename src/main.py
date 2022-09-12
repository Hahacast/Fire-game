# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:49:23 2020

@author: user
"""

import sys
import pygame 
import mySoldier
import wall

def main():
    pygame.mixer.pre_init(44100,-16,2,2048)
    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load(r"..\music\background_music.ogg")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)
    
    resolution = 1600 , 900
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("maringLord ")
    #初始化字體

    #加載圖片
    background_image = pygame .image.load(r"..\image\地圖\main_map.png").convert_alpha()
    clip1_image = pygame.image.load(r"..\image\clip1.png").convert_alpha()
    clip2_image = pygame.image.load(r"..\image\clip2.png").convert_alpha()


    #加載音效
    sniper_fire = pygame.mixer.Sound(r"..\music\狙擊槍_fire.wav")
    sniper_switch = pygame.mixer.Sound(r"..\music\狙擊槍_換彈.wav")
    gun_fire = pygame.mixer.Sound(r"..\music\機槍_fire.wav")
    gun_switch = pygame.mixer.Sound(r"..\music\機槍_換彈.wav")
    

    allsoldierGroup   = pygame.sprite.Group()

    
    mySoldier_T1 = mySoldier.MySoldier(1)
    allsoldierGroup.add(mySoldier_T1)

    mySoldier_T2 = mySoldier.MySoldier(2)
    allsoldierGroup.add(mySoldier_T2)
    
    bgmap = wall.Map()
    
    
    
    
    
    
    
    #創建player1射擊延遲 1秒     
       
    MYBULLETNOTCOOLINGEVENT_1 = pygame.constants.USEREVENT
    pygame.time.set_timer(MYBULLETNOTCOOLINGEVENT_1, 150)
    #創建player2射擊延遲 2秒
#    MYBULLETNOTCOOLINGEVENT_2 = pygame.constants.USEREVENT+1
#    pygame.time.set_timer(MYBULLETNOTCOOLINGEVENT_2, 1000)  
    

    
    continuous_1 = 0
    continuous_2 = 0
    movdir  = 0
    movdir2 = 0
    enemyNumber = 3
    enemyCouldMove      = True
    switch_R1_R2_image  = True
    homeSurvive         = True
    running_T1          = True
    running_T2          = True
    clip1_flag = 0 #是否換彈
    clip2_flag = 0
    clip1_clock = 0#換彈計時
    clip2_clock = 0
    
    bullet2_cool_flag = 0
    bullet2_cool_clock = 0
    clock = pygame .time.Clock()
    
    h_flag = 0
    h_clock = 0 #技能t的秒數  1秒
    h_delay_flag = 0 #f技能延遲
    h_delay_clock = 0    

   
    
    while True:
        for event in pygame .event.get():
            if event.type == pygame .QUIT:
                pygame .quit()
                sys.exit()
            # 我方子弹冷却事件
            if event.type == MYBULLETNOTCOOLINGEVENT_1:
                mySoldier_T1.bulletNotCooling = True
 #           if event.type == MYBULLETNOTCOOLINGEVENT_2:
 #               mySoldier_T2.bulletNotCooling = True
                

                
        #檢查玩家的鍵盤操作        
        key_pressed = pygame .key.get_pressed()    
        #玩家1的移動操作
                  
        if key_pressed[pygame.K_w]:
            movdir = 0
            running_T1 = True
            allsoldierGroup.remove(mySoldier_T1)
            if continuous_1 == 0:
               mySoldier_T1.moveUp(1, allsoldierGroup ,bgmap.blockGroup )
            else:
                mySoldier_T1.moveUp(0, allsoldierGroup,bgmap.blockGroup)
            allsoldierGroup.add(mySoldier_T1)
        if key_pressed[pygame.K_s]:
            moving = 7
            movdir = 1
            running_T1 = True
            allsoldierGroup.remove(mySoldier_T1)
            if continuous_1 == movdir:
                mySoldier_T1.moveDown(1, allsoldierGroup  ,bgmap.blockGroup)

            else:
                mySoldier_T1.moveDown(0, allsoldierGroup ,bgmap.blockGroup)

            allsoldierGroup.add(mySoldier_T1)
        if key_pressed[pygame.K_a]:
            moving = 7
            movdir = 2
            running_T1 = True
            allsoldierGroup.remove(mySoldier_T1)
            if continuous_1 == movdir:
                mySoldier_T1.moveLeft(1, allsoldierGroup ,bgmap.blockGroup) 

            else:
                mySoldier_T1.moveLeft(0, allsoldierGroup ,bgmap.blockGroup)

            allsoldierGroup.add(mySoldier_T1)
        if key_pressed[pygame.K_d]:
            moving = 7
            movdir = 3
            running_T1 = True
            allsoldierGroup.remove(mySoldier_T1)
            if continuous_1 == movdir:
                mySoldier_T1.moveRight(1, allsoldierGroup ,bgmap.blockGroup)

            else:
                mySoldier_T1.moveRight(0, allsoldierGroup ,bgmap.blockGroup)

            allsoldierGroup.add(mySoldier_T1)

        if key_pressed[pygame.K_j]:
            if not mySoldier_T1.bullet.life and mySoldier_T1.bulletNotCooling and clip1_flag != 1 and mySoldier_T1.clip > 0:
                gun_fire.play()               
                mySoldier_T1.shoot()
                mySoldier_T1.bulletNotCooling = False
        if key_pressed[pygame.K_f]:
            if clip1_flag == 0:
                clip1_flag = 1
                gun_switch.play()
        if key_pressed[pygame.K_h]:
            if h_delay_flag == 0:
                h_flag = 1
                h_delay_flag = 1
                mySoldier_T1.speed = 5
            
        
        #疾跑時間
        if h_flag == 1:
            h_clock += 1
            if h_clock >= 30:
                mySoldier_T1.speed = 2
                h_flag = 0
                h_clock = 0
        #疾跑延遲
        if h_delay_flag == 1:
            h_delay_clock += 1
            if h_delay_clock >= 144*2.5:
                h_delay_flag = 0
                h_delay_clock = 0
        #換彈延遲    
        if clip1_flag  == 1:
            clip1_clock += 1
            if clip1_clock >= 144*3:
                mySoldier_T1.clip = 30
                clip1_clock = 0
                clip1_flag = 0 
                
            
               
               
               
               
               
        #玩家2的移動操作 

        if key_pressed[pygame.K_UP]:
            movdir2 = 0
            running_T2 = True
            allsoldierGroup.remove(mySoldier_T2)
            if continuous_2 == movdir2:
                mySoldier_T2.moveUp(1, allsoldierGroup ,bgmap.blockGroup) 
            else:
                mySoldier_T2.moveUp(0, allsoldierGroup ,bgmap.blockGroup)
            allsoldierGroup.add(mySoldier_T2)
        if key_pressed[pygame.K_DOWN]:
            movdir2 = 1
            running_T2 = True
            allsoldierGroup.remove(mySoldier_T2)
            if continuous_2 == movdir2:
                mySoldier_T2.moveDown(1, allsoldierGroup ,bgmap.blockGroup)
            else:
                mySoldier_T2.moveDown(0, allsoldierGroup ,bgmap.blockGroup)
            allsoldierGroup.add(mySoldier_T2)
        if key_pressed[pygame.K_LEFT]:
            movdir2 = 2
            running_T2 = True
            allsoldierGroup.remove(mySoldier_T2)
            
            if continuous_2 == movdir2:
                mySoldier_T2.moveLeft(1, allsoldierGroup ,bgmap.blockGroup)
            else:
                mySoldier_T2.moveLeft(0, allsoldierGroup ,bgmap.blockGroup)
            allsoldierGroup.add(mySoldier_T2)
        if key_pressed[pygame.K_RIGHT]:
            movdir2 = 3
            running_T2 = True
            allsoldierGroup.remove(mySoldier_T2)
            if continuous_2 == movdir2:
                mySoldier_T2.moveRight(1, allsoldierGroup ,bgmap.blockGroup)
            else:
                mySoldier_T2.moveRight(0, allsoldierGroup ,bgmap.blockGroup)
            allsoldierGroup.add(mySoldier_T2)                       
        if key_pressed[pygame.K_KP3]:
            if not mySoldier_T2.bullet.life and clip2_flag != 1 and bullet2_cool_flag == 0 and mySoldier_T2.clip > 0:
               bullet2_cool_flag = 1
               sniper_fire.play()
               mySoldier_T2.shoot()
               mySoldier_T2.bulletNotCooling = True
        #換彈       
        if key_pressed[pygame.K_KP2]:
            if clip2_flag == 0:
                sniper_switch.play()
                clip2_flag = 1
        #換彈延遲 狙擊延遲
#        print("bullet2_cool_flag = " , bullet2_cool_flag)   
        if bullet2_cool_flag == 1:
#            print("bullet2_cool_clock = " , bullet2_cool_clock)
            
            bullet2_cool_clock += 1
            if bullet2_cool_clock >= 144*2:
                bullet2_cool_clock = 0
                bullet2_cool_flag = 0  
        if clip2_flag == 1:
            clip2_clock += 1
            if clip2_clock >= 144*4:
                mySoldier_T2.clip = 7
                clip2_clock = 0
                clip2_flag = 0
                bullet2_cool_flag = 0 
                
                
                
                
                
                
                
                
                
                
                
        #繪製背景
        screen.blit(background_image, (0, 0))
        #繪製子彈1
        if mySoldier_T1.bullet.life:
            mySoldier_T1.bullet.move()
            # 子彈1是否射到玩家2
            if pygame.sprite.spritecollideany(mySoldier_T1.bullet, bgmap.blockGroup):
                 mySoldier_T1.bullet.life = False
            elif  pygame.sprite.collide_rect(mySoldier_T1.bullet,mySoldier_T2):
                mySoldier_T2.life -= 15
                mySoldier_T1.bullet.life = False
                if mySoldier_T2.life <= 0:
                    mySoldier_T2.soldier_R0 = pygame.image.load(r"..\image\dead.png").convert_alpha()
            #子彈1與牆壁

            else:
                screen.blit(mySoldier_T1.bullet.bullet, mySoldier_T1.bullet.rect)
            
                
                
        #繪製子彈2    
        if mySoldier_T2.bullet.life:
            mySoldier_T2.bullet.move()  
            if pygame.sprite.spritecollideany(mySoldier_T2.bullet, bgmap.blockGroup):
                 mySoldier_T2.bullet.life = False
            # 子彈2與玩家1
            elif  pygame.sprite.collide_rect(mySoldier_T2.bullet,mySoldier_T1):
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
        
        if h_delay_flag != 0:        
            font3 = pygame.font.SysFont("arial", 16) #槍兵1的疾跑延遲
            font3_surface = font3.render(str( round((144*2.5-h_delay_clock)/144 , 2)), True, (78, 78, 78))
            screen.blit(font3_surface , (mySoldier_T1.rect.left+15  ,mySoldier_T1.rect.top-40) )
    
        if bullet2_cool_flag != 0:        
            font4 = pygame.font.SysFont("arial", 16) #槍兵2的射擊冷卻
            font4_surface = font4.render(str( round((144*2-bullet2_cool_clock)/144 , 2)), True, (78, 78, 78))
            screen.blit(font4_surface , (mySoldier_T2.rect.left+15  ,mySoldier_T2.rect.top-40) )   
        
    
        
        #槍兵1彈夾
        font3 = pygame.font.SysFont("arial", 30) #槍兵1的彈夾
        font3_surface = font3.render(str(mySoldier_T1.clip), True, (67, 89, 171))
        screen.blit(font3_surface , ( 180, 830 ))
        screen.blit(clip1_image , (10 , 830 ))
        
        #槍兵2彈夾
        
        font4 = pygame.font.SysFont("arial", 30) #槍兵1的彈夾
        font4_surface = font4.render(str(mySoldier_T2.clip), True, (227,23, 13))
        screen.blit(font4_surface , (1550, 840 ))
        screen.blit(clip2_image , (1280 , 800 ))
        
        
        
        
        continuous_1 = movdir
        continuous_2 = movdir2
        pygame.display.update()
        if mySoldier_T1.life <= 0 or mySoldier_T2.life <= 0:
            gameover()
        clock.tick(144)
        


def gameover():
    pygame.time.delay(3000)
    main()

if __name__ == "__main__":
        main()

        
        