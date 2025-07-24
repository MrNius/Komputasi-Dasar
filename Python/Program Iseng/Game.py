import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
width = 800
height = 600

# Warna
white = (255, 255, 255)

# Inisialisasi layar
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animasi Bergerak")

# Koordinat awal objek
x = 50
y = height // 2

# Kecepatan pergerakan
speed = 5

clock = pygame.time.Clock()

# Loop utama
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Bersihkan layar
    screen.fill(white)

    # Gambar objek
    pygame.draw.rect(screen, (0, 0, 255), (x, y, 50, 50))

    # Update tampilan
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
