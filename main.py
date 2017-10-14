import pygame, sys, random, time, math
from Block import *
from player import *
from pygame.locals import *
from box import*
from BG import *
from bullet import *

pygame.init()
width = 800
height = 608
w_cube = 32
h_cube = 32
cSec = 0
cFrame = 0
FPS = 0
i = 0#parametr otvechaushiy za animaciu 
j = 0#parametr za padenie boxov d
k = 0#obnovlenie cadrov boxov

fps_font = pygame.font.Font("C:\Windows\Fonts\8514fix.fon",20)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
static_sprites = pygame.sprite.Group()
dinamic_sprites = pygame.sprite.Group()#box sprites
bullet_sprites = pygame.sprite.Group()
bullet_player_sprites = pygame.sprite.Group()
player_sprites = pygame.sprite.Group()
player = Player()
player.rect.x = 600
player.rect.y = 500
player_sprites.add(player)
b = Bullet()
bullet_player_sprites.add(b)
# 1-8 - bottom, 9 - 16 - right, 17 - 24 -left
####################3Play_area
for i in range(0,25):
    j = 18
    pf = Block(random.randint(1, 8))
    pf.rect.x = i*32
    pf.rect.y = j*32
    static_sprites.add(pf)
for j in range(0,18):
    i = 0
    pf = Block(random.randint(9, 16))
    pf.rect.x = i*32
    pf.rect.y = j*32
    static_sprites.add(pf)
for j in range(0,18):
    i = 24
    pf = Block(random.randint(17, 24))
    pf.rect.x = i*32
    pf.rect.y = j*32
    static_sprites.add(pf)
########################
def bullet_move():
     for b in bullet_player_sprites:   
        if b.fire:
            if b.left:
                b.xvel = - 2
            if not b.left:
                b.xvel =   2
            b.rect.x += b.xvel
            #bullet_player_sprites.remove(b)
            bullet_sprites.add(b)
def player_fire(player,b):
    if not b.fire: 
        if player.left:
            b.left = True
            b.image = b.sprite.subsurface((30,0,30,9))
            b.rect.x = player.rect.centerx - 30
            b.rect.y = player.rect.centery
        if not player.left:
            b.left = False
            b.image = b.sprite.subsurface((0,0,30,9))
            b.rect.x = player.rect.centerx
            b.rect.y = player.rect.centery
            
            
            
            
    
def draw_box(k):
        for d in dinamic_sprites:
        
            if d.yvel > 0:
                if k in range(0,29):
                    d.image = d.sprite.subsurface((0,0,31,32))
                if k in range(30,59):
                    d.image = d.sprite.subsurface((31,0,31,32))
                if k in range(60,89):
                    d.image = d.sprite.subsurface((62,0,31,32))
                if k in range(90,119):
                    d.image = d.sprite.subsurface((124,0,31,32))
                if k in range(120,149):
                    d.image = d.sprite.subsurface((155,0,31,32))
                if k in range(150,179):
                    d.image = d.sprite.subsurface((186,0,31,32))

def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, (0,0,0))
    screen.blit(fps_overlay, (0,0))

def count_fps():
    global cSec,cFrame, FPS, deltatime
    if cSec == time.strftime("%S"):
        cFrame +=1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")
        if FPS > 0:
            deltatime = 1 / FPS 
    
def box_update(j):
    if j%500 == 0:
        box = Box()
        box.rect.x = random.randint(33,743)
        box.rect.y = -32
        dinamic_sprites.add(box) 

def collide():
    for p in static_sprites :
        for f in bullet_sprites:
            if pygame.sprite.spritecollide(p ,bullet_sprites, False):
                if pygame.sprite.spritecollide(f ,static_sprites, False):
                    f.fire = False
                    
            
        for d in dinamic_sprites:
            if pygame.sprite.spritecollide(p ,dinamic_sprites, True):
                if pygame.sprite.spritecollide(d ,static_sprites, False):
                    if d.yvel > 0:
                            d.rect.bottom = p.rect.top + 2
                            d.onGround = True
        for h in player_sprites:
            if pygame.sprite.spritecollide(p ,player_sprites, False):
                if pygame.sprite.spritecollide(h ,static_sprites, False):
                    if p.name == 1:
                        if h.yvel > 0:
                            h.rect.bottom = p.rect.top + 2
                            h.onGround = True
                if not pygame.sprite.spritecollide(h ,static_sprites, False):
                                h.onGround = False
                if p.name == 2:
                    if h.xvel <= 0:
                        h.rect.left = p.rect.right
                if p.name == 3:
                        if h.xvel >= 0:
                            h.rect.right = p.rect.left
                            
        
def dinamic_sprites_move():
    for h in dinamic_sprites:
        if not h.onGround:
            h.yvel = 1
        if h.onGround:
            h.yvel = 0
        h.rect.y += h.yvel
        
def control(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_LEFT:
            left = True
            player.move_left = True 
            player.move_stop = False
        if event.type == KEYUP and event.key == K_LEFT:
            left = True
            player.move_left = False
            player.move_stop = True
        if event.type == KEYDOWN and event.key == K_RIGHT:
            left = False
            player.move_right = True
            player.move_stop = False
        if event.type == KEYUP and event.key == K_RIGHT:
            left = False
            player.move_right = False
            player.move_stop = True
        if event.type == KEYDOWN:
            if event.key == K_UP:
                player.move_up = True
                    
        if event.type == KEYUP:
            if event.key == K_UP:
                player.move_up = False
        
        if event.type == KEYDOWN and event.key == K_SPACE:
            
                b.fire = True

                
        if event.type == KEYUP and event.key == K_SPACE:
            player.firefire =  False
                
             

while True:
    
    if player.fire >=1: 
        player.fire+=1
    if player.fire ==100:
        player.fire = 0
        
        
    
    k+=1
    if k == 179:
        k = 0
    j+=1
    i+=1
    if i == 39:
        i = 0
    draw_box(k)
    screen.blit(BG.BG_1,(0,0))
    box_update(j)
    control(player)
    bullet_move()
    dinamic_sprites_move()
    player.move_player(i)
    player_fire(player,b)
    #screen.fill((255,255,255))
    static_sprites.draw(screen)
    #static_sprites.update()
    dinamic_sprites.draw(screen)
    bullet_player_sprites.draw(screen)
    bullet_sprites.draw(screen)
    collide()
    #dinamic_sprites.update()
    show_fps()
    screen.blit(player.image,(player.rect.x, player.rect.y))
    pygame.display.update()
    count_fps()
    
    #time.sleep(0.005)
    
    
    
    

