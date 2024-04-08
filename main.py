# Importing the necessary libraries and classes.
import pygame  # Imports the Pygame library.
import sys  # Imports the sys module.
import time
from Text import TextButton  # Imports the TextButton object from Text.py
from GameScreen import Question, Hangman, User  # Imports the Question, Hangman and User objects from GameScreen.py


# Initialising and setting up.
pygame.init()  # Initialises Pygame.
screen = pygame.display.set_mode((1200, 800))  # Sets the dimensions of the game screen; 1200x800 pixels.
pygame.display.set_caption("Hangman")  # Sets a name to the game window.
clock = pygame.time.Clock()  # Creates a clock to later set the FPS.
menuActive = True  # Controls displaying the menu screen; the default screen to open with.
helpActive = False  # Controls displaying the help screen.
gamemodeChooseActive = False  # Controls displaying the gamemode choosing screen.
stagingActive = False  # Controls displaying the staging screen.
computerGameActive = False  # Controls displaying the game screen when the AI is guessing.
userGameActive = False  # Controls displaying the game screen when the user is guessing.
blanksGridDoneOnce = False  # Prevents the blanks grid from being appended to and blitted more than once.
guessShown = False  # Whether the AI's guess is currently being displayed on screen.
userDecisionMade = False  # Whether the user has clicked on either the yesText or noText objects.
userGuessMade = False
displayingAnswerOptions = False  # Controls displaying the yesText and noText objects on the game screen.
pressedYes = False  # Whether the user has answered yes to the AI's guess.
gameComplete = False  # Game was won by the AI.
endgameTextDisplayed = False  # Whether the endgame text is displayed.
userGuesses = False
computerGuesses = False


# Reading the .txt file.
with open("Assets//Word Dictionary//words_alpha.txt", "r") as f:  # Opens the .txt file and automatically closes it afterward.
    words = f.read()  # File is read.
wordList = words.split("\n")  # The data is split at every next line break and converted into a list with each individual word as a list item.
wordList = [word.upper() for word in wordList]  # Converts all the data in the list into all capital letters.


# Images.
hangmanImages = {  # Hangman image dictionary, using convert_alpha() slightly optimises the file to work better with Python.
    "0": pygame.transform.scale(pygame.image.load("Assets//Images//Blank Image.png"), (600, 600)).convert_alpha(),  # Blank filler image.
    "1": pygame.transform.scale(pygame.image.load("Assets//Images//Hangman//Hangman 1.png"), (600, 600)).convert_alpha(),  # Scales the image to a size of 600x600.
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
# Gamemode choosing screen images.
userImage = pygame.transform.scale(pygame.image.load("Assets//Images//User Image.png"), (200, 200)).convert_alpha()
userImageRect = userImage.get_rect(center = (300, 310))
computerImage = pygame.transform.scale(pygame.image.load("Assets//Images//Computer Image.png"), (200, 200)).convert_alpha()
computerImageRect = computerImage.get_rect(center = (900, 330))

# Misc.
graveyardGreen = "#1b2421"  # Colour hex codes.
buttonGrey = "#757575"
alphabetString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # String storing all the possible letters for guesses


# TextButton objects.
hangmanMenuText = TextButton("Hangman", "White", "Yellow", 600, 100, 100, False, True, screen)  # Menu screen.
playMenuText = TextButton("Play", "White", "Yellow", 600, 330, 70, True, True, screen)
helpMenuText = TextButton("Help", "White", "Yellow", 600, 420, 70, True, True, screen)
quitMenuText = TextButton("QUiT", "White", "Yellow", 596, 510, 70, True, True, screen)

infoText1 = TextButton("Choose a word", "White", "Yellow", 600, 100, 80, False, True, screen)  # Help screen.
infoText2 = TextButton("and the AI will", "White", "Yellow", 600, 200, 80, False, True, screen)
infoText3 = TextButton("attempt to guess it!", "White", "Yellow", 600, 300, 80, False, True, screen)
backHelpText = TextButton("Back", "White", "Yellow", 600, 720, 60, True, True, screen)

chooseGamemodeText = TextButton("Who should guess?", "White", "Yellow", 600, 100, 80, False, True, screen)  # Gamemode choosing screen.
userGuessesText = TextButton("I want to guess!", "White", "Yellow", 300, 450, 60, True, True, screen)
computerGuessesText = TextButton("AI should guess!", "White", "Yellow", 900, 450, 60, True, True, screen)
backGamemodeText = TextButton("Back", "White", "Yellow", 600, 720, 60, True, True, screen)

lengthQuestion1 = TextButton("How many letters", "White", "Yellow", 600, 100, 80, False, True, screen)  # Staging screen.
lengthQuestion2 = TextButton("are in", "White", "Yellow", 600, 200, 80, False, True, screen)
lengthQuestion3 = TextButton("your word?", "White", "Yellow", 600, 300, 80, False, True, screen)
lengthInputText = TextButton("", "Yellow", "White", 600, 550, 80, False, True, screen)
confirmStagingText = TextButton("Confirm", "White", "Yellow", 1050, 720, 60, True, True, screen)
backStagingText = TextButton("Back", "White", "Yellow", 110, 720, 60, True, True, screen)

yesText = TextButton("Yes", "White", "Yellow", 810, 600, 70, True, True, screen)  # AI game screen.
noText = TextButton("No", "White", "Yellow", 990, 600, 70, True, True, screen)
computerPositionText = TextButton("What position?", "White", "Yellow", 900, 550, 70, False, False, screen)
computerPositionInputText = TextButton("", "Yellow", "White", 900, 630, 70, False, False, screen)
confirmGameText = TextButton("Confirm", "White", "Yellow", 900, 720, 60, True, False, screen)
backGameText = TextButton("Back", "White", "Yellow", 110, 720, 60, True, True, screen)
computerGuessText1 = TextButton("Is", "White", "Yellow", 875, 300, 70, False, True, screen)
computerGuessText2 = TextButton("in your word?", "White", "Yellow", 900, 400, 70, False, True, screen)
computerGuessText3 = TextButton("", "Yellow", "White", 950, 300, 70, False, True, screen)
blanksText = TextButton("", "White", "Yellow", 900, 140, 80, False, True, screen)
winText = TextButton("Your word is", "White", "Yellow", 900, 300, 70, False, False, screen)
outOfAttemptsText = TextButton("Out of attempts!", "White", "Yellow", 900, 400, 70, False, False, screen)

userGuessPromptText = TextButton("Make a guess!", "White", "Yellow", 900, 300, 70, False, True, screen)  # User game screen.
userLetterGuessInputText = TextButton("", "Yellow", "White", 900, 380, 70, False, True, screen)
correctGameText = TextButton("Correct", buttonGrey, "Yellow", 750, 600, 60, False, True, screen)
incorrectGameText = TextButton("Incorrect", buttonGrey, "Yellow", 1050, 600, 60, False, True, screen)

# Other objects.
question = Question(alphabetString)
hangman = Hangman(hangmanImages, 300, 370, screen)
user = User(wordList)

# TextButton object arrays.
menuObjectArray = [hangmanMenuText, playMenuText, helpMenuText, quitMenuText]  # Stores all the TextButton objects for the menu screen.
helpObjectArray = [infoText1, infoText2, infoText3, backHelpText]  # Stores all the TextButton objects for the help screen.
gamemodeChooseObjectArray = [chooseGamemodeText, userGuessesText, computerGuessesText, backGamemodeText]  # Stores all the TextButton objects for the gamemode choosing screen.
stagingObjectArray = [lengthQuestion1, lengthQuestion2, lengthQuestion3, lengthInputText, confirmStagingText, backStagingText]  # Stores all the TextButton objects for the staging screen.
computerGameObjectArray = [yesText, noText, backGameText, blanksText, outOfAttemptsText, computerPositionText, computerPositionInputText, confirmGameText, computerGuessText1, computerGuessText2, computerGuessText3, winText, outOfAttemptsText]  # Stores all the TextButton objects for the game screen.
userGameObjectArray = [userGuessPromptText, userLetterGuessInputText, blanksText, backGameText, confirmGameText, correctGameText, incorrectGameText, outOfAttemptsText, winText]

# Function used to call all the methods inside the primary game loop common to every TextButton object.
def renderScreenTextObjects(objectArray):  # Takes an array of all TextButton objects on each screen.
    for object in objectArray:  # Loops through each object in the array passed in.
        if object.returnEnabled():  # Checks if the object is currently enabled.
            object.renderText()  # Calls the renderText() function.
            object.createRect()  # Calls the createRect() function.
            object.hoverEffect()  # Calls the hoverEffect() function.
            object.blitText()  # Calls the blitText() function.


# Main game loop.
while True:  # Runs the main game loop.

    # Menu screen.
    if menuActive:  # Runs only if the menu screen is being displayed.
        screen.blit(graveyardImage, graveyardImageRect)  # Sets the menu background.
        renderScreenTextObjects(menuObjectArray)  # Calls all the common methods for menu screen TextButton objects.

    # Help screen.
    elif helpActive:  # Runs only if the help screen is being displayed.
        screen.fill(graveyardGreen)  # Fills the background with the specified shade of green.
        renderScreenTextObjects(helpObjectArray)  # Calls all the common methods for help screen TextButton objects.

    elif gamemodeChooseActive:  # Runs only if the gamemode choosing screen is being displayed.
        screen.fill(graveyardGreen)
        renderScreenTextObjects(gamemodeChooseObjectArray)
        screen.blit(userImage, userImageRect)
        screen.blit(computerImage, computerImageRect)

    # Staging screen.
    elif stagingActive:  # Runs only if the staging screen is being displayed.
        screen.fill(graveyardGreen)  # Fills the background with the specified shade of green.
        renderScreenTextObjects(stagingObjectArray)  # Calls all the common methods for staging screen TextButton objects.
        if question.returnWordLength() is None:  # Checks if the user has entered an input for the length of their chosen word.
            confirmStagingText.setColour(buttonGrey)  # Changes the colour of confirmStagingText to grey if there is no input or if the input is 0.

    # Game screen.
    elif computerGameActive:  # Runs only if the game screen is being displayed.
        screen.fill(graveyardGreen)  # Fills the background with the specified shade of green.
        renderScreenTextObjects(computerGameObjectArray)  # Calls all the common methods for game screen TextButton objects.
        if not blanksGridDoneOnce:  # Checks if the blanks grid have been generated.
            question.generateBlanks()  # If not, the grid is generated.
            blanksText.setText(question.returnBlanks())  # The grid is set as the text to be displayed for blanksText.
            blanksGridDoneOnce = True  # Prevents the grid from being continuously generated.
        userDecisionMade = False  # Checks if the user has made a full answer.
        if not guessShown and not userDecisionMade:  # Only generates a guess if the user has not made a decision and there is no current guess displayed.
            question.generateGuess()  # Generates a guess.
        guessShown = True  # Prevents a guess from being continuously generated.

        if not gameComplete:  # Checks if the game hasn't been won by the AI.
            if question.returnAttemptsMade() == 10:  # Checks if the AI has run out of attempts.
                displayingAnswerOptions = False  # Prevents the detection of mouse collisions with answer TextButton objects.
                outOfAttemptsText.setEnabled(True)  # Enables outOfAttempts to be displayed.
                yesText.setEnabled(False)  # Disables yesText from being displayed.
                noText.setEnabled(False)  # Disables noText from being displayed.
                computerGuessText1.setEnabled(False)  # Disables guessText1 from being displayed.
                computerGuessText2.setEnabled(False)  # Disables guessText2 from being displayed.
                computerGuessText3.setEnabled(False)  # Disables guessLetter from being displayed.
            elif question.returnAttemptsMade() != 10:  # Checks if the AI still has attempts left.
                computerGuessText3.setText(question.returnCurrentGuess())  # Displays a new guess.
                displayingAnswerOptions = True  # Allows the detection of mouse collisions with answer TextButton objects.
                if question.returnGreyState() or computerPositionInputText.returnText() == "":  # Checks if the user has made a position input or if the input is out of range.
                    confirmGameText.setColour(buttonGrey)  # Changes the colour of confirmGameText to grey.
            hangman.renderHangman(question.returnAttemptsMade())  # Renders the appropriate hangman image and creates a hitbox for it.
            hangman.displayHangman()  # Displays the hangman image.

        if gameComplete:  # Checks if the game has been won by the AI.
            winText.setEnabled(True)  # Enables winText to be displayed.
            yesText.setEnabled(False)  # Disables yesText from being displayed.
            noText.setEnabled(False)  # Disables noText from being displayed.
            computerGuessText1.setEnabled(False)  # Disables guessText1 from being displayed.
            computerGuessText2.setEnabled(False)  # Disables guessText2 from being displayed.
            computerGuessText3.setEnabled(False)  # Disables guessLetter from being displayed.
            hangman.renderHangman(11)  # Renders the final "win" image of the hangman and creates a hitbox for it.
            hangman.displayHangman()  # Displays the final "win" hangman.
            if not endgameTextDisplayed:  # Checks if the endgame text has been displayed.
                blanksText.setPos(900, 400)  # Moves the blanks grid downwards.
                blanksText.setText(f"{blanksText.returnText()}!")  # Adds an exclamation point to the end of the word.
                blanksText.setColour("Yellow")  # Changes the colour of blanksText to yellow.
                endgameTextDisplayed =  True  # Prevents the exclamation point from continuously being added to the end of blanksText.

    elif userGameActive:
        screen.fill(graveyardGreen)  # Fills the background with the specified shade of green.
        renderScreenTextObjects(userGameObjectArray)
        confirmGameText.setEnabled(True)
        userGuessPositionSpecified = False
        userGuessMade = False
        if not blanksGridDoneOnce:  # Checks if the blanks grid have been generated.
            user.chooseWord()
            print(user.returnChosenWord())
            while not user.checkLetterDuplicates():
                user.chooseWord()
            print(user.returnChosenWord())
            user.generateBlanks()  # If not, the grid is generated.
            blanksText.setText(user.returnBlanks())  # The grid is set as the text to be displayed for blanksText.
            blanksGridDoneOnce = True  # Prevents the grid from being continuously generated.
        if userLetterGuessInputText.returnText() == "":
            confirmGameText.setColour(buttonGrey)
        if user.returnAttemptsMade() == 10:
            userGuessPromptText.setEnabled(False)
            userLetterGuessInputText.setEnabled(False)
            blanksText.setEnabled(False)
            backGameText.setEnabled(False)
            confirmGameText.setEnabled(False)
            correctGameText.setEnabled(False)
            incorrectGameText.setEnabled(False)
            outOfAttemptsText.setEnabled(True)
        hangman.renderHangman(user.returnAttemptsMade())  # Renders the appropriate hangman image and creates a hitbox for it.
        hangman.displayHangman()
        if user.returnAttemptsMade() != 10:
            if user.checkIfComplete():
                hangman.renderHangman(11)  # Renders the final "win" image of the hangman and creates a hitbox for it.
                hangman.displayHangman()  # Displays the final "win" hangman.
                userGuessPromptText.setEnabled(False)
                userLetterGuessInputText.setEnabled(False)
                backGameText.setEnabled(False)
                confirmGameText.setEnabled(False)
                correctGameText.setEnabled(False)
                incorrectGameText.setEnabled(False)
                winText.setEnabled(True)
                winText.setText("The word was")
                if not endgameTextDisplayed:  # Checks if the endgame text has been displayed.
                    blanksText.setPos(900, 400)  # Moves the blanks grid downwards.
                    blanksText.setText(f"{blanksText.returnText()}!")  # Adds an exclamation point to the end of the word.
                    blanksText.setColour("Yellow")  # Changes the colour of blanksText to yellow.
                    endgameTextDisplayed = True  # Prevents the exclamation point from continuously being added to the end of blanksText.

    # Event loop.
    for event in pygame.event.get():  # Retrieves all events running.
        if event.type == pygame.QUIT:  # Checks if the current event is the same as the quit button of the game window.
            pygame.quit()  # If so, closes the window and stops running.
            sys.exit()  # Terminates the Python script.

        elif event.type == pygame.KEYDOWN:  # Detects a keyboard input.

            if stagingActive:  # Keyboard input for the staging screen.

                # Detects which key was pressed and assigns it to self.__wordLength accordingly.
                if event.key == pygame.K_0:  # If the input key is a 0.
                    question.resetWordLength()  # Resets the word length, which prevents the user from entering the game without a valid input.
                    lengthInputText.setText("")  # Makes the input text blank.
                elif event.key == pygame.K_1:  # If the input key is 1.
                    question.setWordLength(1)
                    lengthInputText.setText("1")
                elif event.key == pygame.K_2:  # If the input key is 2.
                    question.setWordLength(2)
                    lengthInputText.setText("2")
                elif event.key == pygame.K_3:  # If the input key is 3.
                    question.setWordLength(3)
                    lengthInputText.setText("3")
                elif event.key == pygame.K_4:  # If the input key is 4.
                    question.setWordLength(4)
                    lengthInputText.setText("4")
                elif event.key == pygame.K_5:  # If the input key is 5.
                    question.setWordLength(5)
                    lengthInputText.setText("5")
                elif event.key == pygame.K_6:  # If the input key is 6
                    question.setWordLength(6)
                    lengthInputText.setText("6")
                elif event.key == pygame.K_7:  # If the input key is 7.
                    question.setWordLength(7)
                    lengthInputText.setText("7")
                elif event.key == pygame.K_8:  # If the input key is 8.
                    question.setWordLength(8)
                    lengthInputText.setText("8")
                elif event.key == pygame.K_9:  # If the input key is 9.
                    question.setWordLength(9)
                    lengthInputText.setText("9")

            elif computerGameActive:  # Keyboard input for the game screen.

                if event.key == pygame.K_0:  # If the input key is a 0.
                    computerPositionInputText.setText("15")
                    question.setGreyState(True)
                elif event.key == pygame.K_1:  # If the input key is 1.
                    computerPositionInputText.setText("1")
                    question.setGreyState(False)
                elif event.key == pygame.K_2:  # If the input key is 2.
                    computerPositionInputText.setText("2")
                    question.setGreyState(False)
                elif event.key == pygame.K_3:  # If the input key is 3.
                    computerPositionInputText.setText("3")
                    question.setGreyState(False)
                elif event.key == pygame.K_4:  # If the input key is 4.
                    computerPositionInputText.setText("4")
                    question.setGreyState(False)
                elif event.key == pygame.K_5:  # If the input key is 5.
                    computerPositionInputText.setText("5")
                    question.setGreyState(False)
                elif event.key == pygame.K_6:  # If the input key is 6
                    computerPositionInputText.setText("6")
                    question.setGreyState(False)
                elif event.key == pygame.K_7:  # If the input key is 7.
                    computerPositionInputText.setText("7")
                    question.setGreyState(False)
                elif event.key == pygame.K_8:  # If the input key is 8.
                    computerPositionInputText.setText("8")
                    question.setGreyState(False)
                elif event.key == pygame.K_9:  # If the input key is 9.
                    computerPositionInputText.setText("9")
                    question.setGreyState(False)
                if int(computerPositionInputText.returnText()) > len(blanksText.returnText()):  # Checks if the position input is greater than the total length of the word.
                    computerPositionInputText.setText("")  # If so, doesn't show the input on screen.
                    question.setGreyState(True)  # Sets the confirm button to be greyed out.

            elif userGameActive:
                if not userGuessMade:

                    if event.key == pygame.K_a:
                        user.letterGuess("A")
                        userLetterGuessInputText.setText("A")
                    elif event.key == pygame.K_b:
                        user.letterGuess("B")
                        userLetterGuessInputText.setText("B")
                    elif event.key == pygame.K_c:
                        user.letterGuess("C")
                        userLetterGuessInputText.setText("C")
                    elif event.key == pygame.K_d:
                        user.letterGuess("D")
                        userLetterGuessInputText.setText("D")
                    elif event.key == pygame.K_e:
                        user.letterGuess("E")
                        userLetterGuessInputText.setText("E")
                    elif event.key == pygame.K_f:
                        user.letterGuess("F")
                        userLetterGuessInputText.setText("F")
                    elif event.key == pygame.K_g:
                        user.letterGuess("G")
                        userLetterGuessInputText.setText("G")
                    elif event.key == pygame.K_h:
                        user.letterGuess("H")
                        userLetterGuessInputText.setText("H")
                    elif event.key == pygame.K_i:
                        user.letterGuess("I")
                        userLetterGuessInputText.setText("I")
                    elif event.key == pygame.K_j:
                        user.letterGuess("J")
                        userLetterGuessInputText.setText("J")
                    elif event.key == pygame.K_k:
                        user.letterGuess("K")
                        userLetterGuessInputText.setText("K")
                    elif event.key == pygame.K_l:
                        user.letterGuess("L")
                        userLetterGuessInputText.setText("L")
                    elif event.key == pygame.K_m:
                        user.letterGuess("M")
                        userLetterGuessInputText.setText("M")
                    elif event.key == pygame.K_n:
                        user.letterGuess("N")
                        userLetterGuessInputText.setText("N")
                    elif event.key == pygame.K_o:
                        user.letterGuess("O")
                        userLetterGuessInputText.setText("O")
                    elif event.key == pygame.K_p:
                        user.letterGuess("P")
                        userLetterGuessInputText.setText("P")
                    elif event.key == pygame.K_q:
                        user.letterGuess("Q")
                        userLetterGuessInputText.setText("Q")
                    elif event.key == pygame.K_r:
                        user.letterGuess("R")
                        userLetterGuessInputText.setText("R")
                    elif event.key == pygame.K_s:
                        user.letterGuess("S")
                        userLetterGuessInputText.setText("S")
                    elif event.key == pygame.K_t:
                        user.letterGuess("T")
                        userLetterGuessInputText.setText("T")
                    elif event.key == pygame.K_u:
                        user.letterGuess("U")
                        userLetterGuessInputText.setText("U")
                    elif event.key == pygame.K_v:
                        user.letterGuess("V")
                        userLetterGuessInputText.setText("V")
                    elif event.key == pygame.K_w:
                        user.letterGuess("W")
                        userLetterGuessInputText.setText("W")
                    elif event.key == pygame.K_x:
                        user.letterGuess("X")
                        userLetterGuessInputText.setText("X")
                    elif event.key == pygame.K_y:
                        user.letterGuess("Y")
                        userLetterGuessInputText.setText("Y")
                    elif event.key == pygame.K_z:
                        user.letterGuess("Z")
                        userLetterGuessInputText.setText("Z")

        elif event.type == pygame.MOUSEBUTTONDOWN:  # Checks if there is a mouse input.
            if event.button == 1:  # Checks if the mouse input was the left mouse button.

                if menuActive:  # Mouse input for the menu screen.
                    if playMenuText.detectMouse():  # Checks if the play button is pressed by the user.
                        gamemodeChooseActive = True  # Changes screen to the staging screen.
                        menuActive = False
                    elif helpMenuText.detectMouse():  # Checks if the help button is pressed by the user.
                        helpActive = True  # Changes screen to the help screen.
                        menuActive = False
                    elif quitMenuText.detectMouse():
                        pygame.quit()
                        sys.exit()

                elif helpActive:  # Mouse input for the help screen.
                    if backHelpText.detectMouse():  # Checks if the back button on the help screen is pressed by the user.
                        menuActive = True  # Changes screen to the menu screen.
                        helpActive = False

                elif gamemodeChooseActive:
                    if backGamemodeText.detectMouse():
                        menuActive = True
                        gamemodeChooseActive = False
                    elif userGuessesText.detectMouse():
                        userGuesses = True
                        computerGuesses = False
                        userGameActive = True
                        gamemodeChooseActive = False
                    elif computerGuessesText.detectMouse():
                        computerGuesses = True
                        userGuesses = False
                        stagingActive = True
                        gamemodeChooseActive = False

                elif stagingActive:  # Mouse input for the staging screen.
                    if backStagingText.detectMouse():  # Checks if the back button on the staging screen is pressed by the user.
                        gamemodeChooseActive = True  # Changes screen to the menu screen.
                        stagingActive = False
                    if confirmStagingText.detectMouse():  # Checks if the confirm button on the staging screen is pressed by the user.
                        if confirmStagingText.returnColour() == buttonGrey:  # Checks if the confirm button is greyed out.
                            stagingActive = True  # If so, keeps the user on the staging screen.
                        else:
                            computerGameActive = True  # If not, changes screen to the game screen.
                            stagingActive = False

                elif computerGameActive:  # Mouse input for the game screen when the AI is guessing.
                    if guessShown:  # Checks if the AI's guess is currently being shown.
                        if displayingAnswerOptions:  # Checks if the answer options for the user are being displayed.
                            if yesText.detectMouse():  # Checks if the yes button is pressed by the user.
                                yesText.setEnabled(False)  # Disables the yes button.
                                noText.setEnabled(False)  # Disables the no button.
                                computerPositionText.setEnabled(True)  # Enables the position question text.
                                computerPositionInputText.setEnabled(True)  # Enables the user to make an input about the position of the AI's guess.
                                confirmGameText.setEnabled(True)  # Enables the confirm button.
                                guessShown = True  # Keeps the AI's guess on the screen.
                            elif confirmGameText.detectMouse():  # Checks if the confirm button is pressed by the user.
                                if confirmGameText.returnColour() == buttonGrey:  # Checks if the confirm button is greyed out.
                                    userDecisionMade = False  # If so, user is not allowed to confirm their position input.
                                else:  # If the confirm button is not greyed out.
                                    question.setAnswerPosition(int(computerPositionInputText.returnText()))  # User input sent to Question so that blanks can be updated.
                                    blanksText.setText(question.returnBlanks())  # Blanks are updated.
                                    confirmGameText.setEnabled(False)  # Disables the confirm button.
                                    computerPositionText.setEnabled(False)  # Disables the position question text.
                                    computerPositionInputText.setEnabled(False)  # Disables the position input text.
                                    yesText.setEnabled(True)  # Enables the yes button.
                                    noText.setEnabled(True)  # Enables the no button.
                                    guessShown = False  # Removes the AI's guess so that a new one can be generated.
                                    userDecisionMade = True  # Set to True because the user has made their decision.
                            elif noText.detectMouse():  # Checks if the no button is pressed by the user.
                                question.attemptMade()  # Removes an attempt from the AI.
                                guessShown = False  # Removes the AI's guess so that a new one can be generated.
                                userDecisionMade = True  # Set to True because the user has made their decision.
                    if question.checkIfComplete():  # If the AI has guessed the word fully.
                        gameComplete = True  # Initiates the win screen.
                    if backGameText.detectMouse():  # Checks if the back button on the game screen is pressed by the user.
                        stagingActive = True  # Changes screen to the staging screen.
                        computerGameActive = False
                        blanksGridDoneOnce = False  # Allows the blanks to be updated.

                elif userGameActive:
                    if backGameText.detectMouse():
                        gamemodeChooseActive = True
                        userGameActive = False
                    if confirmGameText.detectMouse():
                        correctGameText.setColour(buttonGrey)
                        incorrectGameText.setColour(buttonGrey)
                        if not userGuessMade:
                            if confirmGameText.returnColour() == buttonGrey:
                                break
                            else:
                                userGuessMade = True
                                userLetterGuessInputText.setText("")
                            if not user.checkLetter():
                                user.attemptMade()
                                incorrectGameText.setColour("Yellow")
                            if user.checkLetter():
                                print(f"Letter: {user.returnLetterGuessed()}")
                                user.updateBlanks()
                                blanksText.setText(user.returnBlanks())
                                correctGameText.setColour("Yellow")
                    print(user.returnChosenWord())


    pygame.display.update()  # Updates the display.
    clock.tick(60)  # Sets the framerate; 60FPS has been set as the target FPS.