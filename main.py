import pygame
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((510,510))
pygame.display.set_caption('gradient')
clock = pygame.time.Clock()

for i in range(255):
    for x in range(255):
        #y= randint(0,255)
        pygame.draw.rect(screen,(0,i,x),pygame.Rect(2*i,2*x,2,2))
        print(i,x,0)
        pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit
#             exit()  
#     pygame.display.update()
#     clock.tick(60)