# Importing the necessary libraries and classes.
import pygame
import sys
from Text import TextButton  # Imports the TextButton object from Text.py
from GameScreen import Question, Hangman  # Imports the Question and Hangman objects from GameScreen.py


# Initialising and setting up.
pygame.init()  # Initialises Pygame.
screen = pygame.display.set_mode((1200, 800))  # Sets the dimensions of the game screen; 1200x800 pixels.
pygame.display.set_caption("Hangman")  # Sets a name to the game window.
clock = pygame.time.Clock()  # Creates a clock to later set the FPS.
menuActive = True  # Controls displaying the menu screen; the default screen to open with.
helpActive = False  # Controls displaying the help screen.
stagingActive = False  # Controls displaying the staging screen.
gameActive = False  # Controls displaying the game screen.
gridDoneOnce = False  # Prevents the blanks grid from being appended to and blitted more than once.
guessShown = False  # Whether the AI's guess is currently being displayed on screen.
userDecisionMade = False  # Whether the user has clicked on either the yesText or noText objects.
displayingAnswerOptions = False  # Controls displaying the yesText and noText objects on the game screen.
pressedYes = False
gameComplete = False
endgameText = False


# Reading the .txt file.
with open("Assets//Word Dictionary//words_alpha.txt", "r") as f:  # Opens the .txt file and automatically closes it afterward.
    words = f.read()  # File is read.
wordList = words.split("\n")  # The data is split at every next line break and converted into a list with each individual word as a list item.
wordList = [word.upper() for word in wordList]  # Converts all the data in the list into all capital letters.


# Images.
hangmanImages = {  # Hangman image dictionary, using convert_alpha() slightly optimises the file to work better with Python.
    "0": pygame.transform.scale(pygame.image.load("Assets//Images//Blank Image.png"), (600, 600)).convert_alpha(),  # Scales the image to a size of 600x600.
    "1": pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman 1.png"), (600, 600)).convert_alpha(),
    "2": pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman 2.png"), (600, 600)).convert_alpha(),
    "3": pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman 3.png"), (600, 600)).convert_alpha(),
    "4": pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman 4.png"), (600, 600)).convert_alpha(),
    "5": pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman 5.png"), (600, 600)).convert_alpha(),
    "6": pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman 6.png"), (600, 600)).convert_alpha(),
    "7": pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman 7.png"), (600, 600)).convert_alpha(),
    "8": pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman 8.png"), (600, 600)).convert_alpha(),
    "9": pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman 9.png"), (600, 600)).convert_alpha(),
    "10": pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman 10.png"), (600, 600)).convert_alpha(),
    "11": pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman Win.png"), (600, 600)).convert_alpha()
}
# Graveyard menu background.
graveyardImage = pygame.transform.scale(pygame.image.load("Assets//Images//Graveyard.png"), (1230, 800)).convert_alpha()
graveyardImageRect = graveyardImage.get_rect(center = (615, 400))


# Misc.
graveyardGreen = "#1b2421"  # Colour hex codes.
buttonGrey = "#757575"
alphabetString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # String storing all the possible letters for guesses


# Menu screen text objects.
hangmanMenuText = TextButton("Hangman", "White", "Yellow", 600, 100, 100, False, True, screen)  # Creates an object for the TextButton class.
playMenuText = TextButton("Play", "White", "Yellow", 600, 350, 70, True, True, screen)
helpMenuText = TextButton("Help", "White", "Yellow", 600, 450, 70, True, True, screen)


# Help screen text objects.
infoText1 = TextButton("Choose a word", "Black", "Yellow", 600, 100, 80, False, True, screen)
infoText2 = TextButton("and the AI will", "Black", "Yellow", 600, 200, 80, False, True, screen)
infoText3 = TextButton("attempt to guess it!", "Black", "Yellow", 600, 300, 80, False, True, screen)
backHelpText = TextButton("Back", "Black", "Yellow", 600, 720, 60, True, True, screen)


# Staging screen text objects.
lengthQuestion1 = TextButton("How many letters", "White", "Yellow", 600, 100, 80, False, True, screen)
lengthQuestion2 = TextButton("are in", "White", "Yellow", 600, 200, 80, False, True, screen)
lengthQuestion3 = TextButton("your word?", "White", "Yellow", 600, 300, 80, False, True, screen)
lengthInputText = TextButton("", "Yellow", "White", 600, 550, 80, False, True, screen)
question = Question(wordList, alphabetString, screen)
confirmStagingText = TextButton("Confirm", "White", "Yellow", 1050, 720, 60, True, True, screen)
backStagingText = TextButton("Back", "White", "Yellow", 110, 720, 60, True, True, screen)


# Game screen text objects.
yesText = TextButton("Yes", "White", "Yellow", 810, 600, 70, True, True, screen)
noText = TextButton("No", "White", "Yellow", 990, 600, 70, True, True, screen)
positionText = TextButton("What position?", "White", "Yellow", 900, 550,60, False, False, screen)
positionInputText = TextButton("", "Yellow", "White", 900, 630, 60, False, False, screen)
confirmGameText = TextButton("Confirm", "White", "Yellow", 900, 720, 60, True, False, screen)
backGameText = TextButton("Back", "White", "Yellow", 110, 720, 60, True, True, screen)
guessText1 = TextButton("Is", "White", "Yellow", 875, 300, 70, False, True, screen)
guessText2 = TextButton("in your word?", "White", "Yellow", 900, 400, 70, False, True, screen)
guessLetter = TextButton("", "Yellow", "White", 950, 300, 70, False, True, screen)
blanksText = TextButton("", "White", "Yellow", 910, 140, 80, False, True, screen)
winText = TextButton("Your word is", "White", "Yellow", 900, 400, 70, False, False, screen)
outOfAttemptsText = TextButton("Out of attempts!", "White", "Yellow", 900, 400, 70, False, False, screen)
hangman = Hangman(hangmanImages, 300, 370, screen)


# Object arrays.
menuObjectArray = [hangmanMenuText, playMenuText, helpMenuText]
helpObjectArray = [infoText1, infoText2, infoText3, backHelpText]
stagingObjectArray = [lengthQuestion1, lengthQuestion2, lengthQuestion3, lengthInputText, confirmStagingText, backStagingText]
gameObjectArray = [yesText, noText, backGameText, blanksText, outOfAttemptsText, positionText, positionInputText, confirmGameText, guessText1, guessText2, guessLetter, winText]


def renderScreen(objectArray):
    for object in objectArray:
        if object.returnEnabled():
            object.renderText()
            object.createRect()
            object.hoverEffect()
            object.blitText()


# Main game loop.
while True:  # Runs the main game loop.

    # Menu screen.
    if menuActive:

        screen.blit(graveyardImage, graveyardImageRect)  # Sets the menu background.
        renderScreen(menuObjectArray)


    # Help screen.
    if helpActive:

        screen.fill(graveyardGreen)
        renderScreen(helpObjectArray)

    # Staging screen.
    if stagingActive:

        screen.fill(graveyardGreen)
        renderScreen(stagingObjectArray)
        if question.returnWordLength() is None:
            confirmStagingText.setColour(buttonGrey)

    # Game screen.
    if gameActive:

        screen.fill(graveyardGreen)

        renderScreen(gameObjectArray)

        if not gridDoneOnce:
            question.generateBlanks()
            blanksText.setText(question.returnBlanks())
            gridDoneOnce = True
        userDecisionMade = False
        if not guessShown and not userDecisionMade:
            question.generateGuess()
        guessShown = True

        if not gameComplete:

            if question.returnAttemptsMade() == 10:

                displayingAnswerOptions = False

                outOfAttemptsText.renderText()
                outOfAttemptsText.createRect()
                outOfAttemptsText.blitText()

                yesText.setEnabled(False)
                noText.setEnabled(False)
                guessText1.setEnabled(False)
                guessText2.setEnabled(False)
                guessLetter.setEnabled(False)

            if question.returnAttemptsMade() != 10:

                guessLetter.setText(question.returnCurrentGuess())
                displayingAnswerOptions = True

            hangman.createHangmanRect(question.returnAttemptsMade())
            hangman.displayHangman()

        if gameComplete:

            winText.setEnabled(True)
            yesText.setEnabled(False)
            noText.setEnabled(False)
            guessText1.setEnabled(False)
            guessText2.setEnabled(False)
            guessLetter.setEnabled(False)

            hangman.createHangmanRect(11)
            hangman.displayHangman()

            if not endgameText:

                blanksText.setPos(900, 500)
                blanksText.setText(f"{blanksText.returnText()}!")
                endgameText =  True

    for event in pygame.event.get():  # Retrieves all events running.
        if event.type == pygame.QUIT:  # Checks if the current event is the same as the quit button of the game window.
            pygame.quit()  # If so, closes the window and stops running.
            sys.exit()

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

            elif gameActive:

                if event.key == pygame.K_0:
                    positionInputText.setText("")
                    confirmGameText.setColour(buttonGrey)
                elif event.key == pygame.K_1:
                    positionInputText.setText("1")
                elif event.key == pygame.K_2:
                    positionInputText.setText("2")
                elif event.key == pygame.K_3:
                    positionInputText.setText("3")#
                elif event.key == pygame.K_4:
                    positionInputText.setText("4")
                elif event.key == pygame.K_5:
                    positionInputText.setText("5")
                elif event.key == pygame.K_6:
                    positionInputText.setText("6")
                elif event.key == pygame.K_7:
                    positionInputText.setText("7")
                elif event.key == pygame.K_8:
                    positionInputText.setText("8")
                elif event.key == pygame.K_9:
                    positionInputText.setText("9")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                if menuActive:
                    if playMenuText.detectMouse():  # Checks if the play button is pressed by the user.
                        stagingActive = True
                        menuActive = False
                    elif helpMenuText.detectMouse():  # Checks if the help button is pressed by the user.
                        helpActive = True
                        menuActive = False

                elif helpActive:
                    if backHelpText.detectMouse():
                        helpActive = False
                        menuActive = True

                elif stagingActive:
                    if backStagingText.detectMouse():
                        menuActive = True
                        stagingActive = False
                    if confirmStagingText.detectMouse():
                        if confirmStagingText.returnColour() == buttonGrey:
                            stagingActive = True
                        else:
                            stagingActive = False
                            gameActive = True

                elif gameActive:
                    if guessShown:
                        if displayingAnswerOptions:
                            if yesText.detectMouse():
                                yesText.setEnabled(False)
                                noText.setEnabled(False)
                                positionText.setEnabled(True)
                                positionInputText.setEnabled(True)
                                confirmGameText.setEnabled(True)
                                guessShown = True
                            elif confirmGameText.detectMouse():
                                question.setAnswerPosition(int(positionInputText.returnText()))
                                blanksText.setText(question.returnBlanks())
                                confirmGameText.setEnabled(False)
                                positionText.setEnabled(False)
                                positionInputText.setEnabled(False)
                                yesText.setEnabled(True)
                                noText.setEnabled(True)
                                guessShown = False
                                userDecisionMade = True
                            elif noText.detectMouse():
                                question.attemptMade()
                                guessShown = False
                                userDecisionMade = True
                    if question.checkIfComplete():
                        gameComplete = True
                    if backGameText.detectMouse():
                        gameActive = False
                        stagingActive = True
                        gridDoneOnce = False

    pygame.display.update()  # Updates the display.
    clock.tick(60)  # Sets the framerate; 60FPS has been set as the target FPS.