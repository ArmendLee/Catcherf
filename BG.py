import pygame

pygame.init()

class BG:
    size_w = 800
    size_h = 600

    def Load_BG(file,size_w,size_h):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap,(size_w,size_h))
        surface = pygame.Surface((size_w,size_h), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0,0))
        return surface

    
    BG_1 = Load_BG("images\BG.png",size_w,size_h)
