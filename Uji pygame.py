import pygame

pygame=pygame.display.set_mode((300,300))
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

pygame.draw.rect(layar, (255, 0, 0), pygame.Rect(50, 50, 100, 100))
pygame.display.flip()