import pygame
import time

pygame.init()

WIDTH=500
HEIGHT=600

display_surface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Happy birthday card")

img=pygame.image.load("Bg1.jpeg")
image= pygame.transform.scale(img,(WIDTH,HEIGHT))
font=pygame.font.SysFont=("Ariel",70)
text=font.render("Happy birthday",True,(0,0,255))
run=True
while run:
    display_surface.blit(image,(0,0))
    display_surface.blt(text,(250,300))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()

pygame.quit()