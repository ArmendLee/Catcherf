import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        self.sprite = pygame.image.load('images/knife.png').convert_alpha()
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        # You can choose tipe of image
        #if self.left:
        self.image = self.sprite.subsurface((0,0,30,9))
        #if not self.left: #right
        #    self.image = self.sprite.subsurface((0,0,64,100))
        #if fall:
        #if not fall:
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.xvel = 0
        self.left = True
        self.fire = False


        
        
        
    
