import pygame

pygame.init()

layar = pygame.display.set_mode((500, 200))
selesai = False

waktu = pygame.time.Clock()

while not selesai:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            selesai = True

    layar.fill((255, 255, 255))

    huruf = pygame.font.SysFont('Broadway', 25, True, True)

    teks = huruf.render("The New Project", True, (0, 0, 0))

    layar.blit(teks, [50, 50])
    pygame.display.flip()
    waktu.tick(60)
