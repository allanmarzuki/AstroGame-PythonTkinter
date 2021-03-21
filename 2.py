import pygame
import time
import random

pygame.init()

lebar_layar = 800
tinggi_layar = 600

hitam = (0, 0, 0)
putih = (255, 255, 255)

warna_meteor = (255, 0, 0)

ukuran_anjing = 360

layar = pygame.display.set_mode((lebar_layar, tinggi_layar))
pygame.display.set_caption("Awas Meteor Anjing!")
waktu = pygame.time.Clock()

gambar_anjing = pygame.image.load('anjing.png')


def meteor(hitung):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Jumlah Meteor : " + str(hitung), True, hitam)
    layar.blit(text, (0, 0))


def posisi_meteor(posisi_x, posisi_y, lebar, tinggi, warna):
    pygame.draw.rect(layar, warna, [posisi_x, posisi_y, lebar, tinggi])


def koordinat_anjing(x, y):
    layar.blit(gambar_anjing, (x, y))


def teks(text, font):
    format_teks = font.render(text, True, hitam)
    return format_teks, format_teks.get.rect()


def pesan_layar(text, font):
    ukuran_teks = pygame.font.SysFont('Calibri', 50)
    form_teks, box_teks = teks(text, ukuran_teks)
    box_teks.center = ((lebar_layar / 2), (tinggi_layar / 2))
    layar.blit(form_teks, box_teks)

    pygame.display.update()
    time.sleep(2)
    game_ulang()


def tabrakan():
    pesan_layar("Anjing! Kejatuhan Meteor")


def game_ulang():
    x = (lebar_layar * 0.5)
    y = (tinggi_layar * 0.8)
    x_baru = 0

    benda_posisi_x = random.randrange(0, lebar_layar)
    benda_posisi_y = -600
    benda_kecepatan = 4
    benda_lebar = 100
    benda_tinggi = 100
    jumlah_meteor = 0
    game_selesai = False

    while not game_selesai:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_baru = -5
                elif event.key == pygame.K_RIGHT:
                    x_baru = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_baru = 0
                x_baru += x_baru
    layar.fill(putih)
    posisi_meteor(benda_posisi_x, benda_posisi_y, benda_lebar, benda_tinggi, warna_meteor)
    benda_posisi_y += benda_kecepatan
    koordinat_anjing(x_baru, y)
    meteor(jumlah_meteor)

    if x_baru > lebar_layar - ukuran_anjing or x_baru < 0:
        tabrakan()
    if benda_posisi_y > tinggi_layar:
        benda_posisi_y = 0 - benda_tinggi
        benda_posisi_x = random.randrange(0, lebar_layar)
        jumlah_meteor += 1
        benda_kecepatan += 1
        benda_lebar += (jumlah_meteor * 1.2)

    if y < benda_posisi_y + benda_tinggi:
        if x > benda_posisi_x and x < benda_posisi_x + benda_lebar or x + ukuran_anjing > benda_posisi_x and x + ukuran_anjing < benda_posisi_x + benda_lebar:
            tabrakan()

            pygame.display.update()
            waktu.tick(60)


game_ulang()
pygame.quit()
quit()


