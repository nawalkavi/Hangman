# Importing libraries.
import pygame
import sys

# Initialising and setting up.
pygame.init()
screen = pygame.display.set_mode((1200, 800))  # Creates a window with the dimensions specified.
pygame.display.set_caption("CS Coursework")
clock = pygame.time.Clock()
menuFont = pygame.font.Font("Assets/Fonts/minecraft.ttf", 60)

# Dictionaries.
imageDictionary = {
    "ground": pygame.transform.scale(pygame.image.load("Assets/Images/Ground.png"), (1200, 800)).convert_alpha()
}

auDictionary = {  # Dictionary storing all the frames of each individual Among Us colour.
    "purple": {
        1: pygame.transform.scale(pygame.image.load("Assets/Sprites/Purple/Frame 1.png"), (60, 70)).convert_alpha(),  # Converts the image to something Pygame can work with easier.
        2: pygame.transform.scale(pygame.image.load("Assets/Sprites/Purple/Frame 2.png"), (60, 70)).convert_alpha(),
        3: pygame.transform.scale(pygame.image.load("Assets/Sprites/Purple/Frame 3.png"), (60, 70)).convert_alpha(),
        4: pygame.transform.scale(pygame.image.load("Assets/Sprites/Purple/Frame 4.png"), (60, 70)).convert_alpha(),
        "currentFrame": 1
    },
    "red": {
        1: pygame.transform.scale(pygame.image.load("Assets/Sprites/Red/Frame 1.png"), (60, 70)).convert_alpha(),
        2: pygame.transform.scale(pygame.image.load("Assets/Sprites/Red/Frame 2.png"), (60, 70)).convert_alpha(),
        3: pygame.transform.scale(pygame.image.load("Assets/Sprites/Red/Frame 3.png"), (60, 70)).convert_alpha(),
        4: pygame.transform.scale(pygame.image.load("Assets/Sprites/Red/Frame 4.png"), (60, 70)).convert_alpha(),
        "currentFrame": 1
    }
}

# Positions.
purpleAU_xPos = -70
purpleAU_yPos = 700

# Rectangles.
purpleAU_rect = auDictionary["purple"][1].get_rect(midbottom=(purpleAU_xPos, purpleAU_yPos))

# Surfaces.
menuTempBackground = pygame.Surface((1200, 800))
menuText = menuFont.render("SUSUSUSUS", False, "White")

'''
class MenuAU(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = auDictionary["purple"][1]
        self.rect = purpleAU_rect


MenuAU_sprite = MenuAU()
'''

counter = 0
# Game loop.
while True:
    for event in pygame.event.get():  # Retrieves all events running.
        if event.type == pygame.QUIT:  # Checks if the current event is the same as the quit button of a window.
            pygame.quit()
            sys.exit()

    # Blitting.
    screen.blit(menuTempBackground, (0, 0))
    screen.blit(menuText, (450, 300))

    purpleAU_rect.left += 2
    if purpleAU_rect.left > 1200:
        purpleAU_rect.left = -70
    screen.blit(auDictionary["purple"][auDictionary["purple"]["currentFrame"]], purpleAU_rect)

    if counter < 10:
        counter += 1
    else:
        counter = 0
        for image in auDictionary:
            image = auDictionary[image]
            if image["currentFrame"] < len(image) - 1:
                image["currentFrame"] += 1
            else:
                image["currentFrame"] = 1

    pygame.display.update()
    clock.tick(60)  # Sets the framerate; here, 60fps has been set as the target.
