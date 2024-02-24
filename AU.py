import pygame


def animationAU():
    global purpleAU_index, purpleAU_surface
    if purpleAU_rect.left > 1200:
        purpleAU_index += 0.1
        if purpleAU_index >= len(purpleAU_list):
            purpleAU_index = 0
        purpleAU_surface = purpleAU_list[int(purpleAU_index)]


purpleAU1 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Purple/Frame 1.png"), (60, 70)).convert_alpha()
purpleAU2 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Purple/Frame 2.png"), (60, 70)).convert_alpha(),
purpleAU3 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Purple/Frame 3.png"), (60, 70)).convert_alpha(),
purpleAU4 = pygame.transform.scale(pygame.image.load("Assets/Sprites/Purple/Frame 4.png"), (60, 70)).convert_alpha(),

purpleAU_list = [purpleAU1, purpleAU2, purpleAU3, purpleAU4]
purpleAU_index = 0
purpleAU_surface = purpleAU_list[purpleAU_index]

# AU Positions.
purpleAU_xPos = -70  # Purple.
purpleAU_yPos = 700

purpleAU_rect = purpleAU_surface.get_rect(midbottom=(purpleAU_xPos, purpleAU_yPos))


