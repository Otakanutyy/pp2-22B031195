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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if(pos_x-45>=-40):
             pos_x -= 5
    if keys[pygame.K_RIGHT]:
        if(pos_x+45<=480):
             pos_x += 5
    if keys[pygame.K_UP]:
        if(pos_y-45>=-40):
             pos_y -= 5
    if keys[pygame.K_DOWN]:
        if(pos_y+45<=380):
             pos_y += 5
        

    screen.fill('black')
    pygame.draw.circle(screen, (255,255,255), (pos_x+25, pos_y+25), 25)
    pygame.display.flip()
    clock.tick(60)