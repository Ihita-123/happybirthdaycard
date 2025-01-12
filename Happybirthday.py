import pygame
import time

pygame.init()

WIDTH=500
HEIGHT=600

display_surface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Happy birthday card")


img=pygame.image.load("Bg1.jpeg")
image= pygame.transform.scale(img,(WIDTH,HEIGHT))

img2=pygame.image.load("Bg2.jpg")
image2=pygame.transform.scale(img2,(WIDTH,HEIGHT))

img3=pygame.image.load("Bg3.png")
image3=pygame.transform.scale(img3,(WIDTH,HEIGHT))

font=pygame.font.SysFont("Ariel",70)
text=font.render("Happy birthday",True,(0,0,255))
text2=font.render("Have a great day",True,(255,0,0))
text3=font.render("Many happy returns",True,(0,255,0))
run=True
while run:
    display_surface.blit(image,(0,0))
    display_surface.blit(text,(100,300))
    pygame.display.update()
    time.sleep(2)
    # 2nd picture on screen
    display_surface.blit(image2,(0,0))
    display_surface.blit(text2,(100,250))
    pygame.display.update()
    time.sleep(2)
    #3rd picture on screen
    display_surface.fill(color=(255,255,255))
    display_surface.blit(image3,(0,0))
    display_surface.blit(text3,(100,350))
    pygame.display.update()
    time.sleep(2)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()

pygame.quit()