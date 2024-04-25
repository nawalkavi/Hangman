# Hangman.
class Hangman:

    def __init__(self, hangmanDictionary, xPos, yPos, screen):
        self.__hangmanDictionary = hangmanDictionary
        if type(self.__hangmanDictionary) != dict:  # Validates that the value entered for self.__hangmanDictionary is a dictionary data type.
            self.__hangmanDictionary = {}  # If not, assigns it a default value of an empty dictionary.
        self.__xPos = xPos
        if not (0 <= self.__xPos <= 1200):  # Validates that the value entered for self.__xPos is within the screen dimensions.
            self.__xPos = 300  # If not, assigns it a default value of 300.
        self.__yPos = yPos
        if not (0 <= self.__yPos <= 800):  # Validates that the value entered for self.__yPos is within the screen dimensions.
            self.__xPos = 350  # If not, assigns it a default value of 350.
        self.__screen = screen

    def renderHangman(self, attemptsMade):  # Allows the hangman images to be rendered.
        self.__attemptsMade = str(attemptsMade)  # The value held inside attemptsMade is converted into a string.
        self.__currentHangmanImage = self.__hangmanDictionary[self.__attemptsMade]  # The value is then used as an index position for the hangman dictionary.
        self.__hangmanRect = self.__currentHangmanImage.get_rect(center=(self.__xPos, self.__yPos))  # Creates a rectangular hitbox around the image.

    def displayHangman(self):
        self.__screen.blit(self.__currentHangmanImage, self.__hangmanRect)  # Displays the image to the screen.