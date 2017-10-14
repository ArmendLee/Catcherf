import pygame
sprite = pygame.image.load('images/player.png')
move_speed = 1
gravity = 0.02
power_jump = 2
class Player(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self):
        self.sprite = pygame.image.load('images/player.png').convert_alpha()
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        # You can choose tipe of image
        self.left = False
        #if self.left:
        self.image = self.sprite.subsurface((0,0,19,39)).convert_alpha()
        #if not self.left: #right
        #    self.image = self.sprite.subsurface((0,0,64,100))
        #if fall:
        #if not fall:
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.move_right = False
        self.move_left = False
        self.move_stop = True
        self.onGround = False
        self.move_up = False
        self.rect = self.image.get_rect()
        self.yvel = 0
        self.xvel = 0
        self.fire = 0
        self.firefire = False
    def move_player(self,i):

        if self.move_up:
            if self.onGround:
                self.onGround = False
                self.yvel = - power_jump
                self.rect.y += self.yvel   
        if self.move_right:
            self.rect.centerx += move_speed 
            self.left = False
            if self.onGround:
                if i in range(0,9):
                    self.image = self.sprite.subsurface((0,39,19,39))
                if i in range(10,19):
                    self.image = self.sprite.subsurface((19,39,19,39))
                if i in range(20,29):
                    self.image = self.sprite.subsurface((38,39,19,39))
                if i in range(30,39):
                    self.image = self.sprite.subsurface((19,39,19,39))
            if self.yvel > 0:
                if i in range(0,39):
                    self.image = self.sprite.subsurface((114,43,19,43))
            if self.yvel < 0:
                if i in range(0,39):
                    self.image = self.sprite.subsurface((114,0,19,43))

                    
                
        if self.move_left:
            self.rect.centerx -= move_speed
            self.left = True
            if self.onGround:
                if i in range(0,4):
                    self.image = self.sprite.subsurface((57,39,19,39))
                if i in range(5,9):
                    self.image = self.sprite.subsurface((76,39,19,39))
                if i in range(10,14):
                    self.image = self.sprite.subsurface((95,39,19,39))
                if i in range(15,19):
                    self.image = self.sprite.subsurface((76,39,19,39))
            if self.yvel > 0:
                if i in range(0,39):
                    self.image = self.sprite.subsurface((133,43,19,43))
            if self.yvel < 0:
                if i in range(0,39):
                    self.image = self.sprite.subsurface((133,0,19,43))
            
                
        if not self.move_right and not self.move_left:
            self.rect.x += int(0)
            if self.left:
                if i in range(0,19):
                    self.image = self.sprite.subsurface((57,0,19,39))
                if i in range(10,19):
                    self.image = self.sprite.subsurface((76,0,19,39))
                if self.yvel > 0:
                    if i in range(0,39):
                        self.image = self.sprite.subsurface((133,43,19,43))
                if self.yvel < 0:
                    if i in range(0,39):
                        self.image = self.sprite.subsurface((133,0,19,43))
            if not self.left:
                if i in range(20,39):
                    self.image = self.sprite.subsurface((0,0,19,39))
                if i in range(10,19):
                    self.image = self.sprite.subsurface((19,0,19,39))
                if self.yvel > 0:
                    if i in range(0,39):
                        self.image = self.sprite.subsurface((114,43,19,43))
                if self.yvel < 0:
                    if i in range(0,39):
                        self.image = self.sprite.subsurface((114,0,19,43))
                    
                    
        if not self.onGround:
            self.yvel +=  gravity
            self.rect.y += self.yvel
        if  self.onGround:
            self.yvel = 0
            self.rect.y += self.yvel
         
    
