import ramayan2 as r
import pygame
import os
import sys
#game engine-------------

 
def gameloop():
    global x
    global y
    global run
    global speed
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        x-=speed
    if key[pygame.K_RIGHT]:
        x+=speed
    if key[pygame.K_UP]:
        y-=speed
    if key[pygame.K_DOWN]:
        y+=speed
    if key[pygame.K_ESCAPE]:
        run=False
       # sys.exit()
    sc.fill((0,0,0))
    ############################
    #draw everything here######
    v1.draw()
    v1.move()
    v2.draw()
    v2.move()
    h1.draw()
    h1.move()
    #end drawing##############
    ##############################
    p=pygame.sprite.groupcollide(her,vil,False,False)
    print(p)




    #print(vil)
    pygame.display.update()
    clock.tick(5)    
###########################################
#end of gameloop####################
width=500
height=500
sc=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()
pygame.display.set_caption("Ramayan")
run =True
x=50
y=80
speed=10
##create game object here#####
#############
v1=r.vilan(sc,(50,350))
v2=r.vilan(sc,(350,350))
h1=r.hero(sc,(350,350))
vil=pygame.sprite.Group()
her=pygame.sprite.Group()
vil.add(v1)
vil.add(v2)
her.add(h1)


###################end object#############
#########################################
while run:
    gameloop()
print("bye")
pygame.quit()
