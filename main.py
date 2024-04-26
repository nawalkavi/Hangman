# Importing the necessary libraries and classes.
import pygame  # Imports the Pygame library.
import sys  # Imports the sys module.
from Text import TextButton  # Imports the TextButton object from Text.py
from Hangman import Hangman  # Imports the Hangman object from Hangman.py
from Question import Question  # Imports the Question object from Question.py
from User import User  # Imports the User object from User.py


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
userGuessMade = False  # Whether the user has guessed a letter and confirmed their guess.
displayingAnswerOptions = False  # Controls displaying the yesText and noText objects on the game screen.
pressedYes = False  # Whether the user has answered yes to the AI's guess.
gameComplete = False  # Game was won by the AI.
endgameTextDisplayed = False  # Whether the endgame text is displayed.
displayResultTicker = 0
gameplayMusicPlaying = False
musicPlayedOnce = False


# Reading the .txt file.
with open("Assets//Word Dictionary//words.txt", "r") as f:  # Opens the .txt file and automatically closes it afterward.
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
# Game mode choosing screen images.
userImage = pygame.transform.scale(pygame.image.load("Assets//Images//User Image.png"), (200, 200)).convert_alpha()
userImageRect = userImage.get_rect(center = (300, 310))
computerImage = pygame.transform.scale(pygame.image.load("Assets//Images//Computer Image.png"), (200, 200)).convert_alpha()
computerImageRect = computerImage.get_rect(center = (900, 330))


# Misc.
graveyardGreen = "#1b2421"  # Background colour hex code.
buttonGrey = "#757575"  # Greyed out text colour hex code.
vowelsString = "AEIOU"  # String storing all the vowels for guesses.
consonantsString = "BCDFGHJKLMNPQRSTVWXYZ"  # String storing all the consonants for guesses.
backgroundMusic = pygame.mixer.Sound("Assets//Music//Background Music.wav")  # Opens and assigns the .wav file for background music.
gameplayMusic = pygame.mixer.Sound("Assets//Music//Gameplay Music.wav")  # Opens and assigns the .wav file for gameplay music.
buttonHover = pygame.mixer.Sound("Assets//Music//Button Hover.wav")  # Opens and assigns the .wav file for the text hovering sound effect.
buttonClick = pygame.mixer.Sound("Assets//Music//Button Click.wav")  # Opens and assigns the .wav file for the text clicking sound effect.


# TextButton objects.
hangmanMenuText = TextButton("Hangman", "White", "Yellow", 600, 100, 100, False, True, screen)  # Menu screen.
playMenuText = TextButton("Play", "White", "Yellow", 600, 330, 70, True, True, screen)
helpMenuText = TextButton("Help", "White", "Yellow", 600, 420, 70, True, True, screen)
quitText = TextButton("QUiT", "White", "Yellow", 596, 510, 70, True, False, screen)

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

yesText = TextButton("Yes", "White", "Yellow", 810, 600, 70, True, True, screen)  # Computer game screen.
noText = TextButton("No", "White", "Yellow", 990, 600, 70, True, True, screen)
computerPositionText = TextButton("What position?", "White", "Yellow", 900, 550, 70, False, False, screen)
computerPositionInputText = TextButton("", "Yellow", "White", 900, 630, 70, False, False, screen)
letterDuplicatesText1 = TextButton("How many times", "White", "Yellow", 900, 550, 70, False, False, screen)
letterDuplicatesText2 = TextButton("does it appear?", "White", "Yellow", 900, 650, 70, False, False, screen)
confirmGameText = TextButton("Confirm", "White", "Yellow", 900, 720, 60, True, False, screen)
backGameText = TextButton("Back", "White", "Yellow", 110, 720, 60, True, True, screen)
computerGuessText1 = TextButton("Is", "White", "Yellow", 875, 300, 70, False, True, screen)
computerGuessText2 = TextButton("in your word?", "White", "Yellow", 900, 400, 70, False, True, screen)
computerGuessText3 = TextButton("", "Yellow", "White", 950, 300, 70, False, True, screen)
blanksText = TextButton("", "Yellow", "White", 910, 140, 80, False, True, screen)
winText = TextButton("Your word was", "White", "Yellow", 900, 400, 70, False, False, screen)
outOfAttemptsText = TextButton("Out of attempts!", "White", "Yellow", 900, 300, 70, False, False, screen)

userGuessPromptText = TextButton("Make a guess!", "White", "Yellow", 900, 300, 70, False, True, screen)  # User game screen.
userLetterGuessInputText = TextButton("", "Yellow", "White", 900, 380, 70, False, True, screen)
correctGameText = TextButton("Correct", buttonGrey, "Yellow", 750, 600, 60, False, True, screen)
incorrectGameText = TextButton("Incorrect", buttonGrey, "Yellow", 1050, 600, 60, False, True, screen)

# Other objects.
question = Question(vowelsString, consonantsString)
hangman = Hangman(hangmanImages, 300, 370, screen)
user = User(wordList)

# TextButton object arrays.
menuObjectArray = [hangmanMenuText, playMenuText, helpMenuText, quitText]  # Stores all the TextButton objects for the menu screen.
helpObjectArray = [infoText1, infoText2, infoText3, backHelpText]  # Stores all the TextButton objects for the help screen.
gamemodeChooseObjectArray = [chooseGamemodeText, userGuessesText, computerGuessesText, backGamemodeText]  # Stores all the TextButton objects for the gamemode choosing screen.
stagingObjectArray = [lengthQuestion1, lengthQuestion2, lengthQuestion3, lengthInputText, confirmStagingText, backStagingText]  # Stores all the TextButton objects for the staging screen.
computerGameObjectArray = [yesText, noText, backGameText, blanksText, outOfAttemptsText, computerPositionText, computerPositionInputText, confirmGameText, computerGuessText1, computerGuessText2, computerGuessText3, winText, outOfAttemptsText, quitText]  # Stores all the TextButton objects for the AI game screen.
userGameObjectArray = [userGuessPromptText, userLetterGuessInputText, blanksText, backGameText, confirmGameText, correctGameText, incorrectGameText, outOfAttemptsText, winText, quitText]  # Stores all the Text


# Used to call all the common methods inside the primary game loop common to every TextButton object.
def renderScreenTextObjects(objectArray):  # Takes an array of all TextButton objects on the specific screen as a parameter.
    for object in objectArray:  # Loops through each object in the array passed in.
        if object.returnEnabled():  # Checks if the object is currently enabled.
            object.renderText()  # Calls the renderText() function.
            object.createRect()  # Calls the createRect() function.
            object.hoverEffect()  # Calls the hoverEffect() function.
            object.blitText()  # Calls the blitText() function.d

# Used to call the necessary methods when the user makes an input inside the staging screen.
def handleStagingInput(num):  # Takes the user input number.
    buttonHover.play()  # Plays the appropriate sound effect once.
    question.setWordLength(num)  # Sets the word length for the object with the user's input.
    lengthInputText.setText(str(num))  # Sets the text input for the appropriate TextButton object to display it on screen.

# Used to call all the necessary methods when the user makes a numerical input inside the computer game screen.
def handleGamePositionInput(num):
    buttonHover.play()  # Plays the appropriate sound effect once.
    computerPositionInputText.setText(str(num))  # Sets the text input for the appropriate TextButton object to display it on screen.
    question.setGreyState(False)  # Used to make the confirmGameText TextButton interactable again.

# Used to call all the necessary methods when the user makes an alphabetical input inside the computer game screen.
def handleGameLetterInput(letter):
    buttonHover.play()  # Plays the appropriate sound effect once.
    user.letterGuess(letter)  # Sends the user's guess input to be checked.
    userLetterGuessInputText.setText(letter)  # Sets the text input for the appropriate TextButton object to display it on screen.


# Main game loop.
while True:  # Runs the main game loop.

    if not gameplayMusicPlaying and not musicPlayedOnce:
        gameplayMusic.fadeout(3000)  # Fades out the gameplay music over 3000ms.
        backgroundMusic.play(-1)  # Plays the background music on loop.
        musicPlayedOnce = True  # Prevents the music from continuously being started over.

    if gameplayMusicPlaying and not musicPlayedOnce:
        backgroundMusic.fadeout(3000)  # Fades out the background music over 3000ms.
        gameplayMusic.play(-1)  # Plays the gameplay music on loop.
        musicPlayedOnce = True  # Prevents the music from continuously being started over.

    # Menu screen.
    if menuActive:  # Runs only if the menu screen is being displayed.
        quitText.setEnabled(True)
        screen.blit(graveyardImage, graveyardImageRect)  # Sets the menu background.
        renderScreenTextObjects(menuObjectArray)  # Calls all the common methods for menu screen TextButton objects.

    # Help screen.
    elif helpActive:  # Runs only if the help screen is being displayed.
        quitText.setEnabled(False)
        screen.fill(graveyardGreen)  # Fills the background with the specified shade of green.
        renderScreenTextObjects(helpObjectArray)  # Calls all the common methods for help screen TextButton objects.

    # Game mode choosing screen.
    elif gamemodeChooseActive:  # Runs only if the game mode choosing screen is being displayed.
        quitText.setEnabled(False)
        screen.fill(graveyardGreen)
        renderScreenTextObjects(gamemodeChooseObjectArray)
        screen.blit(userImage, userImageRect)
        screen.blit(computerImage, computerImageRect)

    # Staging screen.
    elif stagingActive:  # Runs only if the staging screen is being displayed.
        quitText.setEnabled(False)
        screen.fill(graveyardGreen)  # Fills the background with the specified shade of green.
        renderScreenTextObjects(stagingObjectArray)  # Calls all the common methods for staging screen TextButton objects.
        if question.returnWordLength() is None:  # Checks if the user has entered an input for the length of their chosen word.
            confirmStagingText.setColour(buttonGrey)  # Changes the colour of confirmStagingText to grey if there is no input or if the input is 0.

    # Computer game screen.
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
                backGameText.setEnabled(False)
                quitText.setSize(50)
                quitText.setEnabled(True)
                quitText.setPos(110, 720)
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
            backGameText.setEnabled(False)
            quitText.setSize(50)
            quitText.setEnabled(True)
            quitText.setPos(110, 720)
            hangman.renderHangman(11)  # Renders the final "win" image of the hangman and creates a hitbox for it.
            hangman.displayHangman()  # Displays the final "win" hangman.
            if not endgameTextDisplayed:  # Checks if the endgame text has been displayed.
                blanksText.setPos(900, 500)  # Moves the blanks grid downwards.
                blanksText.setText(f"{blanksText.returnText()}!")  # Adds an exclamation point to the end of the word.
                endgameTextDisplayed =  True  # Prevents the exclamation point from continuously being added to the end of blanksText.

    # User game screen.
    elif userGameActive:
        screen.fill(graveyardGreen)  # Fills the background with the specified shade of green.
        renderScreenTextObjects(userGameObjectArray)  # Calls all the common methods for TextButton objects on the user game screen.
        confirmGameText.setEnabled(True)  # Enables the confirm button on the user game screen.
        userGuessMade = False  # Prevents the user from confirming a guess.
        if not blanksGridDoneOnce:  # Checks if the blanks grid have been generated.
            user.chooseWord()  # Chooses a random word.
            while not user.checkLetterDuplicates():  # Checks if the word has duplicate letters.
                user.chooseWord()  # If so, a new word is generated until it doesn't.
            user.generateBlanks()  # Generates the blanks.
            blanksText.setText(user.returnBlanks())  # The grid is set as the text to be displayed for blanksText.
            blanksGridDoneOnce = True  # Prevents the blanks from being continuously generated.
        if userLetterGuessInputText.returnText() == "":  # Checks if the user has made an input.
            confirmGameText.setColour(buttonGrey)  # If not, greys out the confirm button.
        if user.checkIfGuessed():
            confirmGameText.setColour(buttonGrey)
        if user.returnAttemptsMade() == 10:  # Checks if the user has reached their limit on attempts.
            userGuessPromptText.setEnabled(False)  # Disables the guess prompt text.
            userLetterGuessInputText.setEnabled(False)  # Disables the text of the user's guess input.
            confirmGameText.setEnabled(False)  # Disables the confirm button.
            correctGameText.setEnabled(False)  # Disables the correct answer indicator text.
            incorrectGameText.setEnabled(False)  # Disables the incorrect answer indicator text.
            outOfAttemptsText.setEnabled(True)  # Enables the text that states the user is out of attempts.
            backGameText.setEnabled(False)
            quitText.setSize(50)
            quitText.setEnabled(True)
            quitText.setPos(110, 720)
            winText.setEnabled(True)
            winText.setText("The word was")
            blanksText.setPos(900, 500)
            blanksText.setText(f"{user.returnChosenWord()}!")
        if user.returnAttemptsMade() != 10:  # Checks if the user still has attempts left.
            if user.checkIfComplete():  # Checks if the user has correctly guessed all the letters.
                user.resetAttempts()
                hangman.renderHangman(11)  # Renders the final "win" image of the hangman and creates a hitbox for it.
                hangman.displayHangman()  # Displays the final "win" hangman.
                userGuessPromptText.setEnabled(False)  # Disables the guess prompt text.
                userLetterGuessInputText.setEnabled(False)  # Disables the text of the user's guess input.
                confirmGameText.setEnabled(False)  # Disables the confirm button.
                correctGameText.setEnabled(False)  # Disables the correct answer indicator text.
                incorrectGameText.setEnabled(False)  # Disables the incorrect answer indicator text.
                backGameText.setEnabled(False)
                quitText.setSize(50)
                quitText.setEnabled(True)
                quitText.setPos(110, 720)
                winText.setEnabled(True)  # Enables the text that states the user has won.
                winText.setText("The word was")  # Sets the text for winText.
                if not endgameTextDisplayed:  # Checks if the endgame text has been displayed.
                    blanksText.setPos(900, 500)  # Moves the blanks grid downwards.
                    blanksText.setText(f"{blanksText.returnText()}!")  # Adds an exclamation point to the end of the word.
                    endgameTextDisplayed = True  # Prevents the exclamation point from continuously being added to the end of blanksText.
        hangman.renderHangman(user.returnAttemptsMade())  # Renders the appropriate hangman image and creates a hitbox for it.
        hangman.displayHangman()  # Displays the hangman image to the screen.

        if displayResultTicker > 0:
            displayResultTicker -= 1
        else:
            incorrectGameText.setColour(buttonGrey)
            correctGameText.setColour(buttonGrey)


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
                    handleStagingInput(1)
                elif event.key == pygame.K_2:  # If the input key is 2.
                    handleStagingInput(2)
                elif event.key == pygame.K_3:  # If the input key is 3.
                    handleStagingInput(3)
                elif event.key == pygame.K_4:  # If the input key is 4.
                    handleStagingInput(4)
                elif event.key == pygame.K_5:  # If the input key is 5.
                    handleStagingInput(5)
                elif event.key == pygame.K_6:  # If the input key is 6
                    handleStagingInput(6)
                elif event.key == pygame.K_7:  # If the input key is 7.
                    handleStagingInput(7)
                elif event.key == pygame.K_8:  # If the input key is 8.
                    handleStagingInput(8)
                elif event.key == pygame.K_9:  # If the input key is 9.
                    handleStagingInput(9)

            elif computerGameActive:  # Keyboard input for the game screen.

                if event.key == pygame.K_0:  # If the input key is 0.
                    computerPositionInputText.setText("15")
                    question.setGreyState(True)
                elif event.key == pygame.K_1:  # If the input key is 1.
                    handleGamePositionInput(1)
                elif event.key == pygame.K_2:  # If the input key is 2.
                    handleGamePositionInput(2)
                elif event.key == pygame.K_3:  # If the input key is 3.
                    handleGamePositionInput(3)
                elif event.key == pygame.K_4:  # If the input key is 4.
                    handleGamePositionInput(4)
                elif event.key == pygame.K_5:  # If the input key is 5.
                    handleGamePositionInput(5)
                elif event.key == pygame.K_6:  # If the input key is 6
                    handleGamePositionInput(6)
                elif event.key == pygame.K_7:  # If the input key is 7.
                    handleGamePositionInput(7)
                elif event.key == pygame.K_8:  # If the input key is 8.
                    handleGamePositionInput(8)
                elif event.key == pygame.K_9:  # If the input key is 9.
                    handleGamePositionInput(9)
                else:
                    break
                if int(computerPositionInputText.returnText()) > len(blanksText.returnText()):  # Checks if the position input is greater than the total length of the word.
                    computerPositionInputText.setText("")  # If so, doesn't show the input on screen.
                    question.setGreyState(True)  # Sets the confirm button to be greyed out.

            elif userGameActive:
                if not userGuessMade:

                    if event.key == pygame.K_a:
                        handleGameLetterInput("A")
                    elif event.key == pygame.K_b:
                        handleGameLetterInput("B")
                    elif event.key == pygame.K_c:
                        handleGameLetterInput("C")
                    elif event.key == pygame.K_d:
                        handleGameLetterInput("D")
                    elif event.key == pygame.K_e:
                        handleGameLetterInput("E")
                    elif event.key == pygame.K_f:
                        handleGameLetterInput("F")
                    elif event.key == pygame.K_g:
                        handleGameLetterInput("G")
                    elif event.key == pygame.K_h:
                        handleGameLetterInput("H")
                    elif event.key == pygame.K_i:
                        handleGameLetterInput("I")
                    elif event.key == pygame.K_j:
                        handleGameLetterInput("J")
                    elif event.key == pygame.K_k:
                        handleGameLetterInput("K")
                    elif event.key == pygame.K_l:
                        handleGameLetterInput("L")
                    elif event.key == pygame.K_m:
                        handleGameLetterInput("M")
                    elif event.key == pygame.K_n:
                        handleGameLetterInput("N")
                    elif event.key == pygame.K_o:
                        handleGameLetterInput("O")
                    elif event.key == pygame.K_p:
                        handleGameLetterInput("P")
                    elif event.key == pygame.K_q:
                        handleGameLetterInput("Q")
                    elif event.key == pygame.K_r:
                        handleGameLetterInput("R")
                    elif event.key == pygame.K_s:
                        handleGameLetterInput("S")
                    elif event.key == pygame.K_t:
                        handleGameLetterInput("T")
                    elif event.key == pygame.K_u:
                        handleGameLetterInput("U")
                    elif event.key == pygame.K_v:
                        handleGameLetterInput("V")
                    elif event.key == pygame.K_w:
                        handleGameLetterInput("W")
                    elif event.key == pygame.K_x:
                        handleGameLetterInput("X")
                    elif event.key == pygame.K_y:
                        handleGameLetterInput("Y")
                    elif event.key == pygame.K_z:
                        handleGameLetterInput("Z")

        elif event.type == pygame.MOUSEBUTTONDOWN:  # Checks if there is a mouse input.
            if event.button == 1:  # Checks if the mouse input was the left mouse button.

                if menuActive:  # Mouse input for the menu screen.
                    if playMenuText.detectMouse():  # Checks if the play button is pressed by the user.
                        buttonClick.play()
                        gamemodeChooseActive = True  # Changes screen to the staging screen.
                        menuActive = False
                    elif helpMenuText.detectMouse():  # Checks if the help button is pressed by the user.
                        buttonClick.play()
                        helpActive = True  # Changes screen to the help screen.
                        menuActive = False
                    elif quitText.detectMouse():
                        buttonClick.play()
                        pygame.quit()
                        sys.exit()

                elif helpActive:  # Mouse input for the help screen.
                    if backHelpText.detectMouse():  # Checks if the back button on the help screen is pressed by the user.
                        buttonClick.play()
                        menuActive = True  # Changes screen to the menu screen.
                        helpActive = False

                elif gamemodeChooseActive:
                    blanksGridDoneOnce = False
                    question.resetAttempts()
                    user.resetAttempts()
                    if backGamemodeText.detectMouse():  # Checks if the back button on the game mode choosing screen is pressed by the user.
                        buttonClick.play()
                        menuActive = True  # Changes screen to the menu screen.
                        gamemodeChooseActive = False
                    elif userGuessesText.detectMouse():  # Checks if the option to guess the word themselves was pressed.
                        gameplayMusicPlaying = True
                        musicPlayedOnce = False
                        buttonClick.play()
                        userGuesses = True  # Changes screen to the game screen where the user guesses.
                        computerGuesses = False
                        userGameActive = True
                        gamemodeChooseActive = False
                    elif computerGuessesText.detectMouse():  # Checks if the option to have the AI guess the word was pressed.
                        buttonClick.play()
                        confirmGameText.setEnabled(False)
                        computerGuesses = True  # Changes screen to the game screen where the AI guesses.
                        userGuesses = False
                        stagingActive = True
                        gamemodeChooseActive = False

                elif stagingActive:  # Mouse input for the staging screen.
                    if backStagingText.detectMouse():  # Checks if the back button on the staging screen is pressed by the user.
                        buttonClick.play()
                        gamemodeChooseActive = True  # Changes screen to the menu screen.
                        stagingActive = False
                    if confirmStagingText.detectMouse():  # Checks if the confirm button on the staging screen is pressed by the user.
                        if confirmStagingText.returnColour() == buttonGrey:  # Checks if the confirm button is greyed out.
                            stagingActive = True  # If so, keeps the user on the staging screen.
                        else:
                            gameplayMusicPlaying = True
                            musicPlayedOnce = False
                            buttonClick.play()
                            computerGameActive = True  # If not, changes screen to the game screen.
                            stagingActive = False

                elif computerGameActive:  # Mouse input for the game screen when the AI is guessing.
                    if guessShown:  # Checks if the AI's guess is currently being shown.
                        if displayingAnswerOptions:  # Checks if the answer options for the user are being displayed.
                            if yesText.detectMouse():  # Checks if the yes button is pressed by the user.
                                buttonClick.play()
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
                                    buttonClick.play()
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
                                buttonClick.play()
                                question.attemptMade()  # Removes an attempt from the AI.
                                guessShown = False  # Removes the AI's guess so that a new one can be generated.
                                userDecisionMade = True  # Set to True because the user has made their decision.
                    if question.checkIfComplete():  # If the AI has guessed the word fully.
                        gameComplete = True  # Initiates the win screen.
                    if backGameText.detectMouse():  # Checks if the back button on the game screen is pressed by the user.
                        gameplayMusicPlaying = False
                        musicPlayedOnce = False
                        buttonClick.play()
                        stagingActive = True  # Changes screen to the staging screen.
                        computerGameActive = False
                        blanksGridDoneOnce = False  # Allows the blanks to be updated.
                        question.resetAttempts()
                    elif quitText.detectMouse():
                        buttonClick.play()
                        pygame.quit()
                        sys.exit()

                elif userGameActive:
                    if backGameText.detectMouse():  # Checks if the back button on the user game screen is pressed.
                        gameplayMusicPlaying = False
                        musicPlayedOnce = False
                        buttonClick.play()
                        gamemodeChooseActive = True  # Changes screen to the game mode choosing screen.
                        userGameActive = False
                    elif quitText.detectMouse():
                        buttonClick.play()
                        pygame.quit()
                        sys.exit()
                    if confirmGameText.detectMouse():  # Checks if the confirm button on the user game screen is pressed.
                        user.storeGuess()
                        correctGameText.setColour(buttonGrey)  # Greys out the correct answer indicator text.
                        incorrectGameText.setColour(buttonGrey)  # Greys out the incorrect answer indicator text.
                        if not userGuessMade:  # Checks if the user has confirmed a guess.
                            if confirmGameText.returnColour() == buttonGrey:  # Checks if the confirm button is greyed out.
                                break  # If so, breaks from the rest of the loop.
                            else:  # If not, runs the rest of the loop.
                                buttonClick.play()
                                userGuessMade = True
                                userLetterGuessInputText.setText("")  # Clears the text that displays the user's chosen guess.
                            if not user.checkLetter():  # Checks if the guess was incorrect.
                                user.attemptMade()  # If so, adds 1 to the total number of guesses made.
                                incorrectGameText.setColour("Yellow")  # Highlights the incorrect answer indicator.
                                displayResultTicker = 30  # Allows the incorrect answer indicator to be highlighted for half a second.
                            if user.checkLetter():  # Checks if the guess was correct.
                                user.updateBlanks()  # If so, updates the blanks with the new letter.
                                blanksText.setText(user.returnBlanks())  # Passes the updated blanks to blanksText to be displayed.
                                correctGameText.setColour("Yellow")  # Highlights the correct answer indicator.
                                displayResultTicker = 30  # Allows the correct answer indicator to be highlighted for half a second.

    pygame.display.update()  # Updates the display.
    clock.tick(60)  # Sets the framerate; 60FPS has been set as the target FPS.