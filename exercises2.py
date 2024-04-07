import pygame
import sys
import random

pygame.init()

screen=pygame.display.set_mode((400,600))
clock=pygame.time.Clock()
going=1

current_x=0
current_y=0
prev_x=0
prev_y=0

#colours
red=(255,0,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
all_coloures=[red,blue,white]
print(len(all_coloures))

cnt_coloures=0

x_curr=0
y_curr=0
x_prev=0
y_prev=0

eraser=0
left_button_pressed=False

while going==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            going=0
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                
                if cnt_coloures==2:
                    cnt_coloures=0
                else:
                    cnt_coloures+=1
      
                
        if event.type==pygame.MOUSEBUTTONDOWN and event.button!=1:
            print("Hejenjen")
            x_curr=event.pos[0]
            y_curr=event.pos[1]
            x_prev=event.pos[0]
            y_prev=event.pos[1]
            eraser=True

        if event.type==pygame.MOUSEMOTION:
            if eraser:
             #pygame.draw.rect(screen,(255,0,0),(event.pos[0],event.pos[1],5,5))
             x_curr=event.pos[0]
             y_curr=event.pos[1]
             pygame.draw.rect(screen,black,(x_prev,y_prev,x_curr-x_prev,y_curr-y_prev))

        if event.type==pygame.MOUSEBUTTONUP and event.button!=1:
            eraser=False
            
    
    pygame.display.flip()
    clock.tick(60)
    

    if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
        print("hhh")
        current_x=event.pos[0]
        current_y=event.pos[1]
        prev_x=event.pos[0]
        prev_y=event.pos[1]
        left_button_pressed=True

    if event.type==pygame.MOUSEMOTION:
        print("Position of the mouse",event.pos)
        if left_button_pressed:
            #pygame.draw.rect(screen,(255,0,0),(event.pos[0],event.pos[1],5,5))
            current_x=event.pos[0]
            current_y=event.pos[1]
            pygame.draw.rect(screen,all_coloures[cnt_coloures],(prev_x,prev_y,current_x-prev_x,current_y-prev_y))
            

    if event.type==pygame.MOUSEBUTTONUP and event.button==1:
        left_button_pressed=False
        

    pygame.display.flip()
    clock.tick(60)
    