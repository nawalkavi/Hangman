# Importing the necessary libraries.
import pygame


# Menu.
class TextButton:

    def __init__(self, text, colour, xPos, yPos, size, screen):  # Constructor for the class; takes all the necessary parameters.
        self.__text = text
        self.__colour = colour
        self.__xPos = xPos
        self.__yPos = yPos
        self.__size = size
        self.__screen = screen
        self.__menuFont = pygame.font.Font("Assets//Fonts//Mighty Soul.ttf", self.__size)  # Loads the font for the menu.

    def detectMouse(self):
        self.__mousePos = pygame.mouse.get_pos()  # Returns the current position of the mouse cursor.
        if self.__menuTextRect.collidepoint(self.__mousePos):
            return True

    def renderText(self):
        self.__renderedText = self.__menuFont.render(self.__text, True, self.__colour)  # Renders the text.

    def createRect(self):
        self.__menuTextRect = self.__renderedText.get_rect(center=(self.__xPos, self.__yPos))  # Creates the text into a rectangle, which makes blitting and collision detection easier.

    def returnRender(self):
        return self.__renderedText

    def returnRect(self):
        return self.__menuTextRect

    def hoverEffect(self):  #  Changes text colour based on mouse position.
        if self.detectMouse():
            self.__colour = "Yellow"  # Changes the text colour to yellow if the mouse cursor is hovering over it.
            return True
        if not self.detectMouse():
            self.__colour = "White"  # Defaults back to white if not.
            return False

    def blitText(self):
        self.__screen.blit(self.returnRender(), self.__menuTextRect)  # Blits to the screen.