import pygame

pygame.init()
selesai = False
waktu = pygame.time.Clock()
layar = pygame.display.set_mode((600, 600))
gambar = pygame.image.load('anjing.png')
gambar = pygame.transform.scale(gambar, (450, 500))


def tampil_gambar(x, y):
    layar.blit(gambar, (x, y))


x = 50
y = 50

while not selesai:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            selesai = True

        layar.fill((255, 255, 255))
        tampil_gambar(x, y)

        pygame.display.update()
        waktu.tick(60)
