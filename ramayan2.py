import pygame
import os
import math
class hero(pygame.sprite.Sprite):
    speed=5
    x=0
    y=0
    def __init__(self,sc,pos):
        pygame.sprite.Sprite.__init__(self)
        img=pygame.image.load(os.path.join("image","bullet5.png"))
        self.img=img
        self.rect=img.get_rect()
        self.x,self.y=pos
        self.w=sc.get_width()
        self.h=sc.get_height()
        self.sc=sc
        self.move()
        
    def draw(self):
        #img=pygame.image.load(os.path.join("image","bullet5.png"))   
        if self.speed<0:
            img=pygame.transform.flip(self.img,True,False)
        img=pygame.transform.scale(self.img,(50,50))
        self.sc.blit(img,(self.x,self.y))
    def move(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.x-=vilan.speed
        if key[pygame.K_RIGHT]:
            self.x+=vilan.speed
        if key[pygame.K_UP]:
            self.y-=vilan.speed
        if key[pygame.K_DOWN]:
            self.y+=vilan.speed

class vilan(pygame.sprite.Sprite):
    speed=10
    def __init__(self,sc,pos):
        pygame.sprite.Sprite.__init__(self)
        img=pygame.image.load(os.path.join("image","vilan1.jpg"))
        self.img=img
        self.rect=img.get_rect()
        self.x,self.y=pos
        self.w=sc.get_width()
        self.h=sc.get_height()
        self.sc=sc
        self.move()
        
    def draw(self):   
        if self.speed<0:
            img=pygame.transform.flip(self.img,True,False)
        img=pygame.transform.scale(self.img,(50,50))
        self.sc.blit(img,(self.x,self.y))
        self.rect=img.get_rect()

    def move(self):
        self.x+=self.speed
        if self.x>=self.w:
            self.speed=-self.speed
        elif self.x<0:
            self.speed=-self.speed
        

class fire(pygame.sprite.Sprite):
    def __init__(self):
        super.__init__(self)
    def draw():
        img=pygame.image.load(os.path.join("image","bullet2.jpg"))
        img2=pygame.transform.flip(img,True,False)
        return img2
class background(pygame.sprite.Sprite):
    def __init__(self):
        super.__init__(self)
    def draw():
        img=pygame.image.load(os.path.join("image","buildingblock.jpg"))
        return img
class obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super.__init__(self)
    def draw():
        img=pygame.image.load(os.path.join("image","images2.jpg"))
        return img


