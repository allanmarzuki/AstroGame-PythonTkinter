import pygame

pygame.init()
layar = pygame.display.set_mode((600, 400))
selesai = False
x = 50
y = 50

waktu = pygame.time.Clock()

while not selesai:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            selesai = True

    tombol = pygame.key.get_pressed()
    if tombol[pygame.K_UP]: y -= 10
    if tombol[pygame.K_DOWN]: y += 10
    if tombol[pygame.K_LEFT]: x -= 10
    if tombol[pygame.K_RIGHT]: x += 10

    layar.fill((0, 0, 0))
    pygame.draw.rect(layar, (0, 100, 250), pygame.Rect(x, y, 100, 100))

    pygame.display.flip()
    waktu.tick(60)
