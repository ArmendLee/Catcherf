import pygame
gravity = 0.2
class Box(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self):
        self.sprite = pygame.image.load('images/box1.png').convert_alpha()
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        # You can choose tipe of image
        #if self.left:
        self.image = self.sprite.subsurface((0,0,31,32))
        #if not self.left: #right
        #    self.image = self.sprite.subsurface((0,0,64,100))
        #if fall:
        #if not fall:
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.onGround = False
        self.rect = self.image.get_rect()
        self.yvel = 0


    def draw_box(k):
        for d in dinamic_sprites:
        
            if d.yvel > 0:
                if k in range(0,9):
                    d.image = self.sprite.subsurface((0,0,31,32))
                if k in range(10,19):
                    d.image = self.sprite.subsurface((31,0,31,32))
                if k in range(20,29):
                    self.image = self.sprite.subsurface((62,0,31,32))
                if k in range(30,39):
                    d.image = self.sprite.subsurface((93,0,31,32))
                if k in range(40,49):
                    self.image = self.sprite.subsurface((124,0,31,32))
                if k in range(50,59):
                    d.image = self.sprite.subsurface((155,0,31,32))
                if k in range(60,69):
                    d.image = self.sprite.subsurface((186,0,31,32))
            

                
                
            
                
            
            
            
            
