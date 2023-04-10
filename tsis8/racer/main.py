import pygame as pg
from pygame import mixer as mix
import random

pg.init()
mix.init()
clock=pg.time.Clock()

#CONSTANTS
SCR_W=400
SCR_H=600
ENEMYSPEED=3
RACERSPEED=5
SCORECOINS=0
SCORE=0
RACERMODE=False

f1 = pg.font.Font('C:/Users/Ислам/Documents/week1//pp2-22B031195/lab8/racer/Mono.ttf', 20)
f2 = pg.font.Font('C:/Users/Ислам/Documents/week1//pp2-22B031195/lab8/racer/Mono.ttf', 36)

screen=pg.display.set_mode((SCR_W, SCR_H))
pg.display.set_caption("1racer")

icon=pg.image.load("C:/Users/Ислам/Documents/week1//pp2-22B031195/lab8/racer/iconn.jpg")

pg.display.set_icon(icon)
mix.music.load("C:/Users/Ислам/Documents/week1//pp2-22B031195/lab8/racer/bgmusicloop.mp3")
mix.music.set_volume(0.2)
mix.music.play(-1)

bg=pg.image.load("C:/Users/Ислам/Documents/week1//pp2-22B031195/lab8/racer/background.png")
bg1=pg.image.load("C:/Users/Ислам/Documents/week1//pp2-22B031195/lab8/racer/bgcaught.jpg")


deadscreen=False

#setting enemy class
class Enemy(pg.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pg.image.load("C:/Users/Ислам/Documents/week1//pp2-22B031195/lab8/racer/police.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCR_W-40),0) 
 
      def move(self):
        self.rect.move_ip(0,ENEMYSPEED)
        if (self.rect.bottom > 650):
            global SCORE
            SCORE+=5
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect)

#setting class of player
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pg.image.load("C:/Users/Ислам/Documents/week1//pp2-22B031195/lab8/racer/redcar.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pg.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[pg.K_LEFT]:
                  self.rect.move_ip(-1*(RACERSPEED+SCORECOINS//10), 0)
        if self.rect.right < SCR_W:        
              if pressed_keys[pg.K_RIGHT]:
                  self.rect.move_ip(RACERSPEED+SCORECOINS//10, 0)
    def draw(self, surface):
        if RACERMODE:
            surface.blit(self.imagecool, self.rect)
        else:
            surface.blit(self.image, self.rect)  

RACER=Player()

#setiing class of money
class Coins(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pg.image.load("C:/Users/Ислам/Documents/week1//pp2-22B031195/lab8/racer/money.jpg")
        self.rect = self.image.get_rect()
        mylist1=[*range(20, max(RACER.rect.center[0]-50,20))]
        mylist2=[*range(min(RACER.rect.center[0]+50, SCR_W-20), SCR_W-20)]
        mylist1.extend(mylist2)
        self.rect.center=(int(random.choice(mylist1)),525) 
    def update(self):
        mylist1=[*range(20, max(RACER.rect.center[0]-50,20))]
        mylist2=[*range(min(RACER.rect.center[0]+50, SCR_W-20), SCR_W-20)]
        mylist1.extend(mylist2)
        self.rect.center=(int(random.choice(mylist1)),525)
    def draw(self, surface):
        surface.blit(self.image, self.rect)  
 


E1=Enemy()
MONEY=Coins()

enemies = pg.sprite.Group()
enemies.add(E1)

regards=pg.sprite.Group()
regards.add(MONEY)

all_sprites = pg.sprite.Group()
all_sprites.add(RACER)
all_sprites.add(E1)

#Adding a new User event 
INC_SPEED = pg.USEREVENT + 1
pg.time.set_timer(INC_SPEED, 10000)
running=True
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        if event.type==INC_SPEED:
            ENEMYSPEED+=1
    text1 = f1.render("x{}".format(str(SCORE)),False,(0, 0, 0))
    text2 = f1.render("x{}".format(str(SCORECOINS)),False,(0, 0, 0))
    if deadscreen:
        screen.blit(bg1,(0,0))
        tex1=f2.render("TOTAL SCORE:{}".format(str(SCORE)),True,(0, 0, 0))
        rect=tex1.get_rect()
        rect.center=(200,480)
        tex2=f2.render("MONEY:{}".format(str(SCORECOINS)),True,(0, 0, 0))
        rect2=tex2.get_rect()
        rect2.center=(200,530)
        screen.blit(tex1, rect)
        screen.blit(tex2,rect2)
    else:
        screen.blit(bg, (0,0))
        screen.blit(MONEY.image, MONEY.rect)
        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
            entity.move()
        screen.blit(text1, (7,35))
        screen.blit(icon, (3,3))
        screen.blit(text2, (38,7))

    if pg.sprite.spritecollideany(RACER, regards):
          MONEY.update()
          SCORECOINS+=1
          RACERMODE=1
 
    #if collision occurs between Player and Enemy
    if pg.sprite.spritecollideany(RACER, enemies):
          pg.display.update()
          mix.music.stop()
          mix.music.load("C:/Users/Ислам/Documents/week1//pp2-22B031195/lab8/racer/policecaught.mp3")
          mix.music.set_volume(0.1)
          mix.music.play(-1)
          for entity in all_sprites:
                entity.kill() 
          deadscreen=True

    
    pg.display.update()
    clock.tick(60)