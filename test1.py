import pygame
import random
import copy
import os
vec=pygame.math.Vector2
width=500
height=500
fps=120
score=0
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((width,height))
oclock=pygame.time.Clock()
pygame.display.set_caption("Game1")
run =True
kl=6
d=1
class platform(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        image=pygame.Surface((100,20))
        image.fill((255,0,0))
        self.image=image
        #self.image.set_colorkey((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def update(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x-=3
        if key[pygame.K_d]:
            self.rect.x+=3
        if key[pygame.K_w]:
            self.rect.y-=3
        if key[pygame.K_s]:
            self.rect.y+=3

class player(pygame.sprite.Sprite):
    
    def __init__(self):
##        self.image6=pygame.image.load(os.path.join("images","6.png"))
##        self.image7=pygame.image.load(os.path.join("images","7.png"))
##        self.image8=pygame.image.load(os.path.join("images","8.png"))
##        self.image9=pygame.image.load(os.path.join("images","9.png"))
        global kl
        pygame.sprite.Sprite.__init__(self)
        image=pygame.image.load(os.path.join("images",str(kl)+".png"))
        image=pygame.transform.scale(image,(60,50))
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=width/2
        self.rect.y=height
        self.rect.center=(width/2,height/2)
        self.pos=vec(width/2,height/2)
        self.acc=vec(0,0)
        self.vel=vec(0,0)
        self.friction=0.1
        self.mass=10

    def update(self):
        oclock.tick(30)
        global kl
        global d
        self.image=pygame.image.load(os.path.join("images",str(kl)+".png")).convert()
        self.image.set_colorkey((0,0,0))
        #self.image.set_clip(100,100)
        im=pygame.transform.chop(self.image,(0,0,120,200))
        self.f=10
        self.speedx=0
        self.speedy=0
        self.acc=vec(0,0.5)
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.acc.x=-.5
            d=2
        if key[pygame.K_RIGHT]:
            d=1
            self.acc.x=.5
        if key[pygame.K_UP]:
            self.acc.y=-0.5
        if key[pygame.K_DOWN]:
            self.acc.y=+0.5
        if key[pygame.K_SPACE]:
            hit=pygame.sprite.spritecollide(p,pl,False)
            if hit:
             p.vel.y=-10
        self.vel+=self.acc*self.friction
        self.pos+=self.vel+0.5*self.acc
        self.rect.center=self.pos
        #print(self.vel)
        if(kl>9):
            kl=6
        if (d==1):
            self.image=pygame.transform.flip(self.image,True,False)
        if(d==2):
            pass
            #self.image=pygame.transform.flip(self.image,True,False)
        self.image=pygame.transform.scale(self.image,(60,50))
        
    def shoot(self):
        fire.play()
        b=bullet(self.rect.x+20,self.rect.y-10)
        bul.add(b)
        all.add(b)
    
class enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image=pygame.image.load(os.path.join("images","4.png"))
        self.image=image
        self.image=pygame.transform.scale(self.image,(50,80))
        self.speed=random.randrange(2,10)
        self.rect=self.image.get_rect()
        self.rect.x=500
        self.rect.y=random.randrange(0,900)
    def update(self):
        self.rect.x-=self.speed
        if (self.rect.x<0):
            self.rect.x=width
            self.rect.y=random.randrange(0,height)
            
############
class bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        image=pygame.image.load(os.path.join("images","explosion2.png"))
        self.image=image
        self.image=pygame.transform.scale(self.image,(40,20))
        self.image=pygame.transform.rotate(self.image,90)
        self.speed=10
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def update(self):
        self.rect.x+=self.speed
        if self.rect.x==width:
            self.kill()

class bground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image=pygame.image.load(os.path.join("images","2.png"))
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
expimg=pygame.image.load(os.path.join("images","explosion2.png"))
expimg=pygame.transform.scale(expimg,(100,100))
    
b=bground()        
p=player()
elist=[]
def drawtext(score):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(score), True,(255,255,255),(0,0,0)) 
    textRect = text.get_rect()   
    textRect.center = (width// 2,20)
    screen.blit(text, textRect)
screen.fill((255,50,50))  
##############
bmusic=pygame.mixer.music.load(os.path.join("music","spaceship.wav"))
pygame.mixer.music.play(-1)
laser=pygame.mixer.Sound(os.path.join("music","explosion.wav"))
fire=pygame.mixer.Sound(os.path.join("music","explod.wav"))
for i in range(5):
    e=enemy()
    elist.append(e)
all=pygame.sprite.Group()
eny=pygame.sprite.Group()
bul=pygame.sprite.Group()
pl=pygame.sprite.Group()
eny.add(elist)
plt=platform(0,418)
plt1=platform(0,100)
plt2=platform(200,418)
pl.add(plt1)
pl.add(plt2)

pl.add(plt)
all.add(b)
all.add(p)
all.add(plt)
all.add(plt1)
all.add(plt2)
all.add(elist)


while run:
    now=pygame.time.Clock()
    o=oclock.tick(fps)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    screen.fill((0,0,0))
    all.draw(screen)
    hit=pygame.sprite.spritecollide(p,pl,False)
    for ht in hit:
##        p.vel.y=0
##        p.vel.x=0
##        p.acc=(0,0)
        #print(ht.rect.collidedict)
        p.pos.y=ht.rect.top-30
        #p.rect.collidedict
        #p.acc.y=0
    if p.pos.y<=height/4:
        p.pos.y+=abs(p.vel.y)
        for prt in all:
            prt.rect.y+=abs(p.vel.y)
    if p.pos.y>=height/4-100:
        p.pos.y-=abs(p.vel.y)
        for prt in all:
            prt.rect.y-=abs(p.vel.y)
            
    hit1=pygame.sprite.groupcollide(eny,bul,True,True)
    
    for ht in hit1:
        e=enemy()
        eny.add(e)
        all.add(e)
        laser.play()
        score+=2
        screen.blit(expimg,ht.rect.center)
    drawtext(score)
    
    all.update()
    
    pygame.display.flip()
print("bye")
pygame.quit()
