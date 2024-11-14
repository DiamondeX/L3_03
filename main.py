from math import floor

import pygame.freetype
import random

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
WHITE = pygame.Color(255, 255, 255, 192)
GREEN = pygame.Color(31, 180, 61, 255)
RED = pygame.Color(255, 0, 0, 255)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

icon = pygame.image.load("assets/Basket_with_apple_80_80.png",)
pygame.display.set_icon(icon)
pygame.display.set_caption("Gather Fruits")

fruit_names = [
    "Apple",
    "Banana",
    "BloodOrange",
    "Durian",
    "Feijoa",
    "Fig",
    "Grapefruit",
    "Kiwi",
    "Lemon",
    "Lime",
    "Lychee",
    "Mandarin",
    "Mango",
    "Orange",
    "Peach",
    "Pear",
]

fruit_images = {}
for fruit_name in fruit_names:
    fruit_images[fruit_name] = pygame.image.load(f"assets/fruits/{fruit_name}.png").convert_alpha()

bg_image = pygame.image.load("assets/Background.jpg")
crosshair = pygame.image.load("assets/Crosshair_80_80.png").convert_alpha()
basket = pygame.image.load("assets/Basket_80_80.png").convert_alpha()
hit_range_img = pygame.image.load("assets/HitRange.png").convert_alpha()
fruit_image = fruit_images[random.choice(fruit_names)]
target_x = 0
target_y = 0

# Инициализация pygame.freetype
pygame.freetype.init()

# Загрузка шрифта. Для примера используется системный шрифт.
# Вы можете использовать любой TTF шрифт, который у вас есть.
font = pygame.freetype.SysFont("Comic Sans MS", 48, bold=True)  # "Arial" - имя шрифта, 48 - размер шрифта

pygame.init()

round_start_time = 0
score = 0
last_hit_score = 0

running = True
while running:
    current_time = pygame.time.get_ticks()

    # new round - new target
    if current_time - round_start_time > 2000:
        fruit_image = fruit_images[random.choice(fruit_names)]
        target_x = random.randint(0, SCREEN_WIDTH - 100) + 50
        target_y = random.randint(0, SCREEN_HEIGHT - 100) + 50
        round_start_time = current_time
    k = min(1.0, (current_time - round_start_time) / 2000)

    # half_size = 60
    # hit_range = 50
    half_size = floor(60 * k)
    hit_range = floor(50 * k)
    full_size = half_size * 2

    target = pygame.transform.scale(fruit_image, (full_size, full_size))
    target_hit_range = pygame.transform.scale(hit_range_img, (full_size, full_size))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            distance = pow(pow((mouse_x - target_x), 2) + pow((mouse_y - target_y), 2), 0.5)
            if distance > hit_range:
                last_hit_score = -200
            else:
                last_hit_score = 70 - hit_range
                round_start_time -= 2000
            score += last_hit_score

    score_color = RED if score < 0 else GREEN
    score_caption, sc_rect = font.render("Score:", WHITE)
    score_text, st_rect = font.render(f"{score}", score_color)

    hit_caption, hc_rect = font.render("Last hit:", WHITE)
    hit_color = RED if last_hit_score < 0 else GREEN
    hit_text, ht_rect = font.render(f"{last_hit_score}", hit_color)

    screen.blit(bg_image, (0, 0))
    screen.blit(target, (target_x - half_size, target_y - half_size))
    screen.blit(target_hit_range, (target_x - half_size, target_y - half_size))
    screen.blit(score_caption, (20, 20))
    screen.blit(score_text, (20 + sc_rect.width + 10, 20))
    screen.blit(hit_caption, (20, 20 + sc_rect.height + 20))
    screen.blit(hit_text, (20 + hc_rect.width + 10, 20 + sc_rect.height + 20))
    screen.blit(crosshair, (mouse_x-40, mouse_y-40))
    screen.blit(basket, (mouse_x-40, mouse_y+40))
    pygame.display.update()

pygame.quit()