import pygame
import random
import copy
import os
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
class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image=pygame.image.load(os.path.join("images","3.png"))
        image=pygame.transform.scale(image,(60,50))
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=width/2
        self.rect.y=height-80

    def update(self):
        self.speedx=0
        self.speedy=0
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.speedx=-5
        if key[pygame.K_RIGHT]:
            self.speedx=+5
        if key[pygame.K_UP]:
            self.speedy=-5
        if key[pygame.K_DOWN]:
            self.speedy=+5
        if key[pygame.K_SPACE]:
            p.shoot()
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
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
        self.rect.x=random.randrange(0,200)
        self.rect.y=0
    def update(self):
        self.rect.y+=self.speed
        if (self.rect.y>width):
            self.rect.x=random.randrange(0,width)
            self.rect.y=0
            
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
        self.rect.y-=self.speed
        if self.rect.y==0:
            self.kill()

class bground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image=pygame.image.load(os.path.join("images","1.png"))
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
eny.add(elist)
all.add(b)
all.add(p)
all.add(elist)


while run:
    now=pygame.time.Clock()
    o=oclock.tick(fps)
    print(o)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    screen.fill((0,0,0))
    all.draw(screen)
    hit=pygame.sprite.spritecollide(p,eny,None)
    if hit:
        p.kill()
        run=False
        
    hit1=pygame.sprite.groupcollide(eny,bul,True,True)
    
    for ht in hit1:
        print(ht.rect.center)
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
