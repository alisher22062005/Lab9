import pygame 
import random,time

pygame.init()

going=True
FPS=pygame.time.Clock()
FPS.tick(60)
length=400
width=600
screen=pygame.display.set_mode((length,width))
screen.fill((255,255,255))

#image_player_car
image=pygame.image.load(r"C:\Users\acer-\OneDrive\Рабочий стол\Lab8\car.png")
rect=image.get_rect()
rect.center=(300,500)

#image_enemy_car
image2=pygame.image.load("car2.png")
rect2=image2.get_rect()
rect2.center=(random.randint(40,370),0)

#image_coin
image3=pygame.image.load("coin.png")
image3=pygame.transform.scale(image3,(50,50))
rect3=image3.get_rect()
rect3.center=(random.randint(150,370),0)

#road
image_road=pygame.image.load(r"C:\Users\acer-\OneDrive\Рабочий стол\Lab8\road.png")
#image_road=pygame.transform.scale(image_road,(400,600))
#road_rect=image_road.get_rect(center=(200,300))

#speed
speed=5
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#font
game_over_font = pygame.font.SysFont('output_GAME_OVER', 60)
game_over_cnt=pygame.font.SysFont("number_of_points",60)


def move_enemy_car():
     rect2.move_ip(0,speed)
     if (rect2.top > 600):
      rect2.top = 0
      rect2.center = (random.randint(30, 370), 0)

def move_player_car():
    pressed_keys=pygame.key.get_pressed()
    if rect.left > 0:
          if pressed_keys[pygame.K_LEFT]:
              rect.move_ip(-5,0)
    if rect.right <370 :       
          if pressed_keys[pygame.K_RIGHT]:
               rect.move_ip(5,0)
def move_coin():
     rect3.move_ip(0,10)
     if (rect3.top>600):
      rect3.top=0
      #rect3.center=(random.randint(30,370),0)

              
   

cnt=0
while going==True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              speed += 2
        if event.type==pygame.QUIT:
            going=False


    #if car_player collide with enemy_car
    screen.blit(image_road,(0,0))  
    if rect.colliderect(rect2):
            screen.fill((255,0,0))
            n=game_over_font.render("Game Over", True, (0,0,0))
            c=game_over_cnt.render("Points: "+str(cnt),False,(0,0,0))
            screen.blit(n, (80,250))
            screen.blit(c,(200,40))
            pygame.display.update()
            time.sleep(4)
            pygame.quit()


    move_player_car()
    move_enemy_car()
    move_coin()
    if rect.colliderect(rect3):
         rect3.top=0
         screen.blit(image_road,(0,0))
         #screen.fill((255,0,0))
         pygame.display.update()
         cnt+=1

    #screen.fill((255,255,255))
    screen.blit(image_road,(0,0))  
    screen.blit(image,rect)
    screen.blit(image2,rect2)
    screen.blit(image3,rect3)
    #screen.blit(image2.rect2)
    pygame.display.update()
    FPS.tick(60)