# Importing the necessary libraries.
import pygame


# Array storing all the predefined string constants for colours inside Pygame.
colourArray = ["Black", "Blue", "Cyan", "Gold", "Gray", "Green", "Orange", "Purple", "Red", "Violet", "Yellow", "White"]


# TextButton.
class TextButton:

    def __init__(self, text, pColour, sColour, xPos, yPos, size, hoverEffect, enabled, screen):  # Constructor for the class; takes all the necessary parameters.
        self.__text = text
        if type(self.__text) != str:  # Validates that the value entered for self.__text is a string data type.
            self.__text = ""  # Assigns it a default value of an empty string if it isn't.
        self.__colourArray = colourArray
        self.__pColour = pColour
        if self.__pColour not in self.__colourArray:  # Validates that the string entered for self.__pColour is inside self.__colourArray.
            self.__pColour = "Black"  # Assigns it a default colour of black if it isn't.
        self.__sColour = sColour
        if self.__sColour not in self.__colourArray:  # Validates that the string entered for self.__sColour is inside self.__colourArray.
            self.__sColour = "Yellow"  # Assigns it a default colour of yellow if it isn't.
        self.__currentColour = pColour
        self.__xPos = xPos
        if not 0 <= self.__xPos <= 1200:  # Validates that the value entered for self.__xPos is within the screen dimensions.
            self.__xPos = 600  # Assigns it a default position of 600 if it isn't.
        self.__yPos = yPos
        if not 0 <= self.__yPos <= 800:  # Validates that the value entered for self.__yPos is within the screen dimensions.
            self.__xPos = 200  # Assigns it a default position of 200 if it isn't.
        self.__size = size
        if self.__size > 300:  # Validates that the value entered for self.__size isn't large enough to exceed screen borders.
            self.__size = 60  # Assigns it a default font size of 60 if it does.
        self.__screen = screen
        self.__menuFont = pygame.font.Font("Assets//Fonts//Mighty Souly.ttf", self.__size)  # Loads the font for the text.
        self.__hover = hoverEffect
        self.__enabled = enabled

    def renderText(self):
        self.__renderedText = self.__menuFont.render(self.__text, True, self.__currentColour)  # Renders the text.

    def createRect(self):
        self.__menuTextRect = self.__renderedText.get_rect(center=(self.__xPos, self.__yPos))  # Creates a rectangular hitbox around the text.

    def returnRender(self):
        return self.__renderedText  # Returns the rendered text.

    def returnRect(self):
        return self.__menuTextRect  # Returns the rendered text complete with its hitbox.

    def detectMouse(self):
        if self.__enabled:
            self.__mousePos = pygame.mouse.get_pos()  # Returns the current position of the mouse cursor.
            if self.__menuTextRect.collidepoint(self.__mousePos):  # Detects a collision between the mouse cursor and the text hitbox.
                return True  # True if there is a collision.
            else:
                return False  # False if there is no collision.
        else:
            return False

    def hoverEffect(self):  #  Changes text colour based on mouse position.
        if self.__hover:
            if self.detectMouse():  # If self.detectMouse() returns True, meaning there is a collision.
                self.__currentColour = self.__sColour  # Changes the text colour to the secondary colour if the mouse cursor is hovering over it.
            if not self.detectMouse():  # If self.detectMouse() returns False, meaning there is no collision.
                self.__currentColour = self.__pColour  # Defaults text colour back to the primary colour.

    def setText(self, newText):
        self.__text = newText  # Allows the text to be displayed to be changed when necessary.

    def returnText(self):
        return self.__text  # Returns the currently specified text to be displayed.

    def setColour(self, newColour):
        self.__currentColour = newColour  # Allows the current text colour to be changed when necessary.

    def returnColour(self):
        return self.__currentColour  # Returns the currently specified text colour.

    def setEnabled(self, newEnabledState):
        self.__enabled = newEnabledState

    def returnEnabled(self):
        return self.__enabled

    def setPos(self, newX, newY):
        self.__xPos = newX
        self.__yPos = newY

    def blitText(self):
        self.__screen.blit(self.returnRender(), self.__menuTextRect)  # Blits to the screen.