import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("clock")
clock=pygame.time.Clock()

ramka=pygame.image.load('C:/Users/Ислам/Documents/week1/pp2-22B031195/py_game/images/ramka.png')
body=pygame.image.load('C:/Users/Ислам/Documents/week1/pp2-22B031195/py_game/images/body.jpeg')

minhand=pygame.image.load('C:/Users/Ислам/Documents/week1/pp2-22B031195/py_game/images/right_hand.jpeg')
minrec=minhand.get_rect()
minrec.center=(200,340)
mincnt=-5

sechand=pygame.image.load('C:/Users/Ислам/Documents/week1/pp2-22B031195/py_game/images/left_hand.jpeg')
secrec=sechand.get_rect()
secrec.center=(520,310)
seccnt=-5

currt=datetime.datetime.now()

seccnt=currt.second
mincnt=currt.minute

running = True

while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running=False
                        
        screen.blit(ramka,(0,0))

        minhand1=pygame.transform.rotate(minhand, -1*((6*mincnt)%360))
        minrec1=minhand1.get_rect()
        minrec1.center=minrec.center
        screen.blit(minhand1, minrec1)

        screen.blit(body,(260,170))

        sechand1=pygame.transform.rotate(sechand, -1*((6*seccnt+270)%360))
        secrec1=sechand1.get_rect()
        secrec1.center=secrec.center
        screen.blit(sechand1, secrec1)

        currt=datetime.datetime.now()
        seccnt=currt.second
        mincnt=currt.minute


        pygame.display.update()
        clock.tick(60)
