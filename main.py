# Importing the necessary libraries and classes.
import pygame
from Text import TextButton  # Imports the TextButton class.
from GameScreen import Question, Hangman


# Initialising and setting up.
pygame.init()  # Initialises Pygame.
screen = pygame.display.set_mode((1200, 800))  # Sets the dimensions of the game screen; 1200x800 pixels.
pygame.display.set_caption("Hangman")  # Sets a name to the game window.
clock = pygame.time.Clock()  # Creates a clock to later set the FPS.
menuActive = True  # Starts the menu screen; the default screen to open with.
helpActive = False  # Starts the help screen.
gameActive = False  # Starts the game screen.
stagingActive = False  # Starts the staging screen.
gridDoneOnce = False  # Prevents the grid from being appended to and blitted more than once.


# Reading the .txt file.
with open("Assets//Word Dictionary//words_alpha.txt", "r") as f:  # Opens the .txt file and automatically closes it afterward.
    words = f.read()  # File is read.
wordList = words.split("\n")  # The data is split at every next line break and converted into a list with each individual word as a list item.
wordList = [word.upper() for word in wordList]  # Converts all the data in the list into all capital letters.


# Image dictionary.
hangmanImages = {
    "1": pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman 1.png"), (150, 150)).convert_alpha(),
    "2": pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman 2.png"), (150, 150)).convert_alpha(),
    "3": pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman 3.png"), (150, 150)).convert_alpha()
}


# Dictionary that will store all the Hangman images in each stage.
hangmanDictionary = {
    1: pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman 1.png"), (100, 80)).convert_alpha(),
    2: pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman 2.png"), (100, 80)).convert_alpha()
}


# Menu screen text objects.
hangmanText = TextButton("Hangman", "Black", "Yellow", 600, 200, 100, screen)  # Creates an object for the TextButton class.
playText = TextButton("Play", "Black", "Yellow", 600, 350, 70, screen)
helpText = TextButton("Help", "Black", "Yellow", 600, 450, 70, screen)

# Help screen text objects.
infoText1 = TextButton("Choose a word", "Black", "Yellow", 600, 100, 80, screen)
infoText2 = TextButton("and the AI will", "Black", "Yellow", 600, 200, 80, screen)
infoText3 = TextButton("attempt to guess it!", "Black", "Yellow", 600, 300, 80, screen)
backHelpText = TextButton("Back", "Black", "Yellow", 600, 700, 60, screen)

# Staging screen text objects.
lengthQuestion1 = TextButton("How many letters", "Black", "Yellow", 600, 100, 80, screen)
lengthQuestion2 = TextButton("are in", "Black", "Yellow", 600, 200, 80, screen)
lengthQuestion3 = TextButton("your word?", "Black", "Yellow", 600, 300, 80, screen)
lengthInputText = TextButton("", "Yellow", "Black", 600, 550, 80, screen)
question = Question(wordList, screen)
confirmStagingText = TextButton("Confirm", "Black", "Yellow", 1050, 700, 60, screen)
backStagingText = TextButton("Back", "Black", "Yellow", 110, 700, 60, screen)

# Game screen text objects.
yesText = TextButton("Yes", "Black", "Yellow", 800, 600, 70, screen)
noText = TextButton("No", "Black", "Yellow", 1000, 600, 70, screen)
guessText1 = TextButton("Is", "Black", "Yellow", 875, 300, 70, screen)
guessText2 = TextButton("in your word?", "Black", "Yellow", 900, 400, 70, screen)
# guessLetter = TextButton("", "Yellow", "Black", )
gridText = TextButton("", "Black", "Yellow", 900, 100, 80, screen)
hangman = Hangman(hangmanImages, screen)


while True:  # Runs the main game loop.

    for event in pygame.event.get():  # Retrieves all events running.
        if event.type == pygame.QUIT:  # Checks if the current event is the same as the quit button of the game window.
            pygame.quit()  # If so, closes the window and stops running.

        elif event.type == pygame.KEYDOWN:  # Detects a keyboard input.

            if stagingActive:  # Ensures user can only input inside the staging screen.

                # Detects which key was pressed and assigns it to self.__wordLength accordingly.
                if event.key == pygame.K_0:
                    question.resetWordLength()
                    lengthInputText.setText("")
                elif event.key == pygame.K_1:
                    question.setWordLength(1)
                    lengthInputText.setText("1")
                elif event.key == pygame.K_2:
                    question.setWordLength(2)
                    lengthInputText.setText("2")
                elif event.key == pygame.K_3:
                    question.setWordLength(3)
                    lengthInputText.setText("3")
                elif event.key == pygame.K_4:
                    question.setWordLength(4)
                    lengthInputText.setText("4")
                elif event.key == pygame.K_5:
                    question.setWordLength(5)
                    lengthInputText.setText("5")
                elif event.key == pygame.K_6:
                    question.setWordLength(6)
                    lengthInputText.setText("6")
                elif event.key == pygame.K_7:
                    question.setWordLength(7)
                    lengthInputText.setText("7")
                elif event.key == pygame.K_8:
                    question.setWordLength(8)
                    lengthInputText.setText("8")
                elif event.key == pygame.K_9:
                    question.setWordLength(9)
                    lengthInputText.setText("9")

    # Menu screen.
    if menuActive:

        gameActive = False  # Stops the other two screens from running and displaying at the same time.
        helpActive = False
        stagingActive = False

        screen.fill("White")  # Fills the screen with the colour black.

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
            stagingActive = True
        elif helpText.detectMouse() and event.type == pygame.MOUSEBUTTONDOWN:  # Checks if the help button is pressed by the user.
            helpActive = True

    # Help screen.
    if helpActive:

        menuActive = False
        gameActive = False
        stagingActive = False

        screen.fill("White")

        infoText1.renderText()  # First line of information text.
        infoText1.createRect()
        infoText1.blitText()

        infoText2.renderText()  # Second line of information text.
        infoText2.createRect()
        infoText2.blitText()

        infoText3.renderText()  # Third line of information text.
        infoText3.createRect()
        infoText3.blitText()

        backHelpText.renderText()  # Back button.
        backHelpText.createRect()
        backHelpText.detectMouse()
        backHelpText.hoverEffect()
        backHelpText.blitText()

        # Changing screens.
        if backHelpText.detectMouse() and event.type == pygame.MOUSEBUTTONDOWN:  # Checks if the back button is pressed by the user.
            menuActive = True

    # Staging screen.
    if stagingActive:

        menuActive = False
        gameActive = False
        helpActive = False

        screen.fill("White")

        lengthQuestion1.renderText()
        lengthQuestion1.createRect()
        lengthQuestion1.blitText()

        lengthQuestion2.renderText()
        lengthQuestion2.createRect()
        lengthQuestion2.blitText()

        lengthQuestion3.renderText()
        lengthQuestion3.createRect()
        lengthQuestion3.blitText()

        lengthInputText.renderText()
        lengthInputText.createRect()
        lengthInputText.blitText()

        confirmStagingText.renderText()
        confirmStagingText.createRect()
        confirmStagingText.detectMouse()
        confirmStagingText.hoverEffect()
        if question.returnWordLength() is None:
            confirmStagingText.setColour("Gray")
        confirmStagingText.blitText()

        backStagingText.renderText()
        backStagingText.createRect()
        backStagingText.detectMouse()
        backStagingText.hoverEffect()
        backStagingText.blitText()

        if backStagingText.detectMouse() and event.type == pygame.MOUSEBUTTONDOWN:
            menuActive = True
        if confirmStagingText.detectMouse() and event.type == pygame.MOUSEBUTTONDOWN:
            if confirmStagingText.returnColour() == "Gray":
                stagingActive = True
            else:
                gameActive = True

    # Game screen.
    if gameActive:

        menuActive = False
        helpActive = False
        stagingActive = False

        screen.fill("White ")

        question.scaleAttempts()
        if not gridDoneOnce:
            question.generateGrid()
            gridDoneOnce = True
        question.matchWords()
        question.generateGuess()
        question.checkIfGuessed()

        hangman.returnCurrentHangmanCount(question.returnAttemptsLeft())
        # hangman.createHangmanRect()
        # hangman.displayHangman()

        guessText1.renderText()
        guessText1.createRect()
        guessText1.blitText()

        guessText2.renderText()
        guessText2.createRect()
        guessText2.blitText()

        gridText.setText(question.returnGrid())
        gridText.renderText()
        gridText.createRect()
        gridText.blitText()

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