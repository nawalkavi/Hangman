# Importing the necessary libraries.
import pygame
colourArray = ["Black", "Blue", "Cyan", "Gold", "Gray", "Green", "Orange", "Purple", "Red", "Violet", "Yellow", "White"]

# Menu.
class TextButton:

    def __init__(self, text, pColour, sColour, xPos, yPos, size, screen):  # Constructor for the class; takes all the necessary parameters.
        self.__text = text
        if type(self.__text) != str:
            self.__text = ""
        self.__colourArray = colourArray
        self.__pColour = pColour
        if self.__pColour not in self.__colourArray:
            self.__pColour = "Black"
        self.__sColour = sColour
        if self.__sColour not in self.__colourArray:
            self.__sColour = "Yellow"
        self.__currentColour = pColour
        self.__xPos = xPos
        if not 0 <= self.__xPos <= 1200:
            self.__xPos = 600
        self.__yPos = yPos
        if not 0 <= self.__yPos <= 800:
            self.__xPos = 200
        self.__size = size
        if self.__size > 300:
            self.__size = 60
        self.__screen = screen
        self.__menuFont = pygame.font.Font("Assets//Fonts//Mighty Souly.ttf", self.__size)  # Loads the font for the menu.

    def detectMouse(self):
        self.__mousePos = pygame.mouse.get_pos()  # Returns the current position of the mouse cursor.
        if self.__menuTextRect.collidepoint(self.__mousePos):
            return True
        else:
            return False

    def renderText(self):
        self.__renderedText = self.__menuFont.render(self.__text, True, self.__currentColour)  # Renders the text.

    def createRect(self):
        self.__menuTextRect = self.__renderedText.get_rect(center=(self.__xPos, self.__yPos))  # Creates the text into a rectangle, which makes blitting and collision detection easier.

    def returnRender(self):
        return self.__renderedText

    def returnRect(self):
        return self.__menuTextRect

    def hoverEffect(self):  #  Changes text colour based on mouse position.
        if self.detectMouse():
            self.__currentColour = self.__sColour  # Changes the text colour to yellow if the mouse cursor is hovering over it.
            return True
        if not self.detectMouse():
            self.__currentColour = self.__pColour  # Defaults back to white if not.
            return False

    def blitText(self):
        self.__screen.blit(self.returnRender(), self.__menuTextRect)  # Blits to the screen.

    def setText(self, newText):
        self.__text = newText

    def returnText(self):
        return self.__text

    def setColour(self, newColour):
        self.__currentColour = newColour

    def returnColour(self):
        return self.__currentColour