import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

icon = pygame.image.load("assets/Basket_with_apple_80_80",)
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

pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()