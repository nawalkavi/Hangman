# Importing the necessary libraries and classes.
import pygame
from Button import TextButton  # Imports the TextButton class.
from GameScreen import GameScreen


# Initialising and setting up.
pygame.init()  # Initialises Pygame.
screen = pygame.display.set_mode((1200, 800))  # Sets the dimensions of the game screen; 1200x800 pixels.
pygame.display.set_caption("Hangman")  # Sets a name to the game window.
clock = pygame.time.Clock()  # Creates a clock to later set the FPS.
menuActive = True  # Starts the menu screen; the default screen to open with.
helpActive = False  # Starts the help screen.
gameActive = False  # Starts the game screen.


# Image dictionary.
hangmanImages = {
    "1": pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman 1.png"), (150, 150)).convert_alpha(),
    "2": pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman 2.png"), (150, 150)).convert_alpha(),
    "3": pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman 3.png"), (150, 150)).convert_alpha()
}


# Text button objects.
hangmanText = TextButton("Hangman", "White", 600, 200, 100, screen)  # Creates an object for the TextButton class.
playText = TextButton("Play", "White", 600, 350, 70, screen)
helpText = TextButton("Help", "White", 600, 450, 70, screen)

yesText = TextButton("Yes", "Black", 900, 500, 70, screen)
noText = TextButton("No", "Black", 900, 600, 70, screen)


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

        gameActive = False  # Stops the other two screens from running and displaying at the same time.
        helpActive = False

        screen.fill("Black")  # Fills the screen with the colour black.

        # Menu text objects.
        hangmanText.renderText()  # Hangman text.
        hangmanText.createRect()
        hangmanText.blitText()

        playText.renderText()  # Play text.
        playText.createRect()
        playText.detectMouse()
        playText.hoverEffect()
        playText.blitText()

        helpText.renderText()  # Help text.
        helpText.createRect()
        helpText.detectMouse()
        helpText.hoverEffect()
        helpText.blitText()

        # Changing screens.
        if playText.detectMouse() and event.type == pygame.MOUSEBUTTONDOWN:  # Checks if the play button is pressed by the user.
            gameActive = True
            menuActive = False
            helpActive = True

    # Game screen.
    if gameActive:

        menuActive = False
        helpActive = False

        screen.fill("White")

        yesText.renderText()
        yesText.createRect()
        yesText.detectMouse()
        yesText.hoverEffect()
        yesText.blitText()

        noText.renderText()
        noText.createRect()
        noText.detectMouse()
        noText.hoverEffect()
        noText.blitText()

    pygame.display.update()  # Updates the display.
    clock.tick(60)  # Sets the framerate; 60FPS has been set as the target FPS.