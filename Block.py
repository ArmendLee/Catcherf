import pygame
sprite = pygame.image.load('images/block2.png')
class Block(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self,name): 
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        # You can choose tipe of image
        #bottom
        if name is 1:
            self.image = sprite.subsurface((0, 0,32,32))
            self.name = 1
        if name is 2:
            self.image = sprite.subsurface((32,0,32,32))
            self.name = 1
        if name is 3:
            self.image = sprite.subsurface((64,0,32,32))
            self.name = 1
        if name is 4:
            self.image = sprite.subsurface((96,0,32,32))
            self.name = 1
        if name is 5:
            self.image = sprite.subsurface((32,32,32,32))
            self.name = 1
        if name is 6:
            self.image = sprite.subsurface((64,32,32,32))
            self.name = 1
        if name is 7:
            self.image = sprite.subsurface((96,32,32,32))
            self.name = 1
        if name is 8:
            self.image = sprite.subsurface((0,32,32,32))
            self.name = 1
        #right
        if name is 9:
            self.image = sprite.subsurface((0,64,32,32))
            self.name = 2
        if name is 10:
            self.image = sprite.subsurface((0,96,32,32))
            self.name = 2
        if name is 11:
            self.image = sprite.subsurface((0,128,32,32))
            self.name = 2
        if name is 12:
            self.image = sprite.subsurface((0,160,32,32))
            self.name = 2
        if name is 13:
            self.image = sprite.subsurface((32,64,32,32))
            self.name = 2
        if name is 14:
            self.image = sprite.subsurface((32,96,32,32))
            self.name = 2
        if name is 15:
            self.image = sprite.subsurface((32,128,32,32))
            self.name = 2
        if name is 16:
            self.image = sprite.subsurface((32,160,32,32))
            self.name = 2
        #left
        if name is 17:
            self.image = sprite.subsurface((64, 64,32,32))
            self.name = 3
        if name is 18:
            self.image = sprite.subsurface((64,96,32,32))
            self.name = 3
        if name is 19:
            self.image = sprite.subsurface((64,128,32,32))
            self.name = 3
        if name is 20:
            self.image = sprite.subsurface((64,160,32,32))
            self.name = 3
        if name is 21:
            self.image = sprite.subsurface((96,64,32,32))
            self.name = 3
        if name is 22:
            self.image = sprite.subsurface((96,96,32,32))
            self.name = 3
        if name is 23:
            self.image = sprite.subsurface((96,128,32,32))
            self.name = 3
        if name is 24:
            self.image = sprite.subsurface((96,160,32,32))
            self.name = 3
            
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        
         
