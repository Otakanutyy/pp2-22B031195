import pygame

screen=pygame.display.set_mode((490,390))
pygame.display.set_caption("ball")
clock=pygame.time.Clock()

bg_1=pygame.Surface((490,390))
bg_2=pygame.Surface((490,390))
pygame.Surface.fill(bg_2,(255,255,255))

pos_x=0
pos_y=0

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                if(pos_y+45<=375):
                    pos_y+=20
            if event.key==pygame.K_UP:
                if(pos_y-45>=-25):
                    pos_y-=20
            if event.key==pygame.K_RIGHT:
                if(pos_x+45<=475):
                    pos_x+=20
            if event.key==pygame.K_LEFT:
                if(pos_x-45>=-25):
                    pos_x-=20
        

    screen.fill('white')
    pygame.draw.circle(screen, (255,204,204), (pos_x+25, pos_y+25), 25)
    pygame.display.flip()
    clock.tick(60)