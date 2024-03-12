# Importing the necessary libraries.
import pygame
import random


# Initialising and setting up.
pygame.init()  # Initialises Pygame.
screen = pygame.display.set_mode((1200, 800))  # Sets the dimensions of the game screen; 1200x800 pixels.
pygame.display.set_caption("Hangman")  # Sets a name to the game window.
clock = pygame.time.Clock()  # Creates a clock to later set the FPS.
menuActive = True  # Starts the menu screen; the default screen to open with.
gameActive = False  # Starts the game screen.


# Menu.
class Menu:

    def __init__(self, text, colour, xPos, yPos, size):  # Constructor for the class; takes all the necessary parameters.
        self.__text = text
        self.__colour = colour
        self.__xPos = xPos
        self.__yPos = yPos
        self.__size = size
        self.__menuFont = pygame.font.Font("Assets//Fonts//Mighty Soul.ttf", self.__size)  # Loads the font for the menu.
        self.__renderedText = self.__menuFont.render(self.__text, True, self.__colour)  # Renders the text and stores it in self.__renderedText.
        self.__mousePos = pygame.mouse.get_pos()  # Returns the current position of the mouse cursor.
        self.__menuTextRect = self.__renderedText.get_rect(center=(self.__xPos, self.__yPos))  # Creates the text into a rectangle, which makes blitting and collision detection easier.
        self.__scaledText = None

    def detectMouse(self):
        if self.__menuTextRect.collidepoint(self.__mousePos):
            return True

    def returnRender(self):
        return self.__renderedText

    def returnRect(self):
        return self.__menuTextRect

    def enlargeText(self):
        if self.detectMouse():
            self.__scaledText = pygame.transform.scale(self.__renderedText, self.__renderedText.get_height() * 2)

    def blitText(self):
        screen.blit(self.returnRender(), self.__menuTextRect)  # Blits to the screen.

hangmanText = Menu("Hangman", "White", 600, 200, 60)  # Creates an object for the Menu class.


# Reading the .txt file.
with open("Assets//Word Dictionary//words_alpha.txt", "r") as f:  # Opens the .txt file and automatically closes it afterward.
    data = f.read()  # File is read.
dataList = data.split("\n")  # The data is split at every next line break and converted into a list with each individual word as a list item.
dataList = [word.upper() for word in dataList]  # Converts all the data in the list into all capital letters.


# User input for word length.
print("Think of a word! How many letters does it have?")
wordLength = int(input("Answer: "))  # Getting input from the user about the length of the word.


# Game lists.
matchedWords = []  # Will store all the words with the same length as that of the user.
wordMaster = []  # Will store the correct guesses to progressively form the answer.
guessedLetters = []  # Will store every letter that has been used as a guess.


# Word matching.
for i in range(0, len(dataList)):  # Traverses through the list storing every word.
    if len(dataList[i]) == wordLength:  # Checks if a word is the same length as that of the user's input.
        matchedWords.append(dataList[i])  # Appends it to the matchedWords list if it is the same length.


# Blank word grid.
gridCount = wordLength + 0
while gridCount > 0:
    wordMaster.append("_")  # Replaces every item in the wordMaster list with an underscore to create the Hangman blank word grid.
    gridCount -= 1


while True:  # Runs the main game loop.

    for event in pygame.event.get():  # Retrieves all events running.
        if event.type == pygame.QUIT:  # Checks if the current event is the same as the quit button of the game window.
            pygame.quit()  # If so, closes the window and stops running.

    # Menu screen.
    if menuActive:
        screen.fill("Black")  # Fills the screen with the colour black.
        hangmanText.detectMouse()
        hangmanText.enlargeText()
        hangmanText.blitText()


    pygame.display.update()  # Updates the display.
    clock.tick(60)  # Sets the framerate; 60FPS has been set as the target FPS.