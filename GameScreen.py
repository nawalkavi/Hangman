# Importing the necessary libraries.
import random


class User:

    def __init__(self, wordList):
        self.__wordList = wordList
        if type(self.__wordList) == list:
            self.__wordList = []
        self.__chosenWord = None
        self.__blanks = ""
        self.__attemptsMade = 0

    def chooseWord(self):
        self.__seenLetters = None
        self.__chosenWord = random.choice(self.__wordList)
        while len(self.__chosenWord) > 10:
            self.__chosenWord = random.choice(self.__wordList)

    def checkLetterDuplicates(self):
        self.__letter = None
        self.__seenLetters = set()
        for self.__letter in self.__chosenWord:
            if self.__letter in self.__seenLetters:
                return False
            self.__seenLetters.add(self.__letter)
        return True

    def returnChosenWord(self):
        return self.__chosenWord

    def generateBlanks(self):
        count = 0  # Temporary variable to hold a value.
        tempArray = []  # Temporary array to hold the blanks.
        count += len(self.__chosenWord)
        while count != 0:  # While count does not match the user's word length.
            tempArray.append("_")  # An underscore is appended to tempArray for every time the loop is run to create the blanks array.
            count -= 1  # 1 is subtracted from count to eventually have it match the user's word length.
        self.__blanks = "".join(tempArray)  # Converts tempArray into a string, which creates the blanks string.

    def returnBlanks(self):
        return self.__blanks

    def updateBlanks(self):
        tempArray = []
        for letter in self.__blanks:
            tempArray.append(letter)
        tempArray[self.__letterPosition] = self.__letterGuessed
        self.__blanks = "".join(tempArray)

    def letterGuess(self, letterGuessed):
        self.__letterGuessed = letterGuessed

    def returnLetterGuessed(self):
        return self.__letterGuessed

    def checkLetter(self):
        self.__letterPosition = 0
        for letter in self.__chosenWord:
            if letter == self.__letterGuessed:
                return True
            self.__letterPosition += 1
        return False

    def attemptMade(self):
        self.__attemptsMade += 1

    def returnAttemptsMade(self):
        return self.__attemptsMade

    def checkIfComplete(self):
        for letter in self.__blanks:
            if letter == "_":
                return False
        return True


# Question.
class Question:

    def __init__(self, alphabet):
        self.__alphabet = alphabet
        if type(self.__alphabet) != str:  # Validates that the value entered for self.__alphabet is a string data type.
            self.__alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # If not, assigns it a default value of a string containing the alphabet.
        self.__wordLength = None  # Will be assigned a value depending on the user's input.
        self.__matchedWords = []  # Will store all the words with the same length as that of the user.
        self.__attemptsMade = 0  # Starts at 0 and ends at 10.
        self.__blanks = ""
        self.__greyedOut = False  # Controls whether confirmGameText is greyed out or not.
        self.__currentGeneratedGuess = None

    def generateBlanks(self):
        count = 0  # Temporary variable to hold a value.
        tempArray = []  # Temporary array to hold the blanks.
        count += self.__wordLength  # Holds the value of the user's word length.
        while count != 0:  # While count does not match the user's word length.
            tempArray.append("_")  # An underscore is appended to tempArray for every time the loop is run to create the blanks array.
            count -= 1  # 1 is subtracted from count to eventually have it match the user's word length.
        self.__blanks = "".join(tempArray)  # Converts tempArray into a string, which creates the blanks string.

    def returnBlanks(self):
        return self.__blanks  # Returns the blanks.

    def setAnswerPosition(self, letterPosition):
        self.__letterPosition = letterPosition - 1  # Value is subtracted by 1 to account for the index value difference.
        tempArray = []  # Temporary array to hold the updated blanks.
        if self.__currentGeneratedGuess is not None:
            for letter in self.__blanks:  # Loops through every letter space in self.__blanks.
                tempArray.append(letter)  # The positions are appended to tempArray.
            tempArray[self.__letterPosition] = self.__currentGeneratedGuess  # The user's specified position is used to replace that position in the array with the current guess.
            self.__blanks = "".join(tempArray)  # The array is converted back into a string.

    def returnLetterPosition(self):
        return self.__letterPosition  # Returns the user's specified letter position.

    def setWordLength(self, newWordLength):  # Allows the word length to be changed.
        self.__wordLength = newWordLength  # Sets self.__wordLength to the new word length passed in.

    def resetWordLength(self):  # Allows the word length to be reset.
        self.__wordLength = None  # Resets the word length.

    def returnWordLength(self):
        return self.__wordLength  # Returns the word length.

    def attemptMade(self):
        if self.__attemptsMade < 10:  # Checks if the AI has already reached the 10 attempt limit.
            self.__attemptsMade += 1  # If not, increments the number of attempts made by 1.

    def returnAttemptsMade(self):
        return self.__attemptsMade  # Returns the number of attempts made by the AI.

    def checkIfComplete(self):  # Checks if the AI has guessed all the letters in the player's word.
        for letter in self.__blanks:  # Loops through each position in the blanks.
            if letter == "_":  # Checks if the position is an underscore; a blank.
                return False  # If so, returns False, meaning the AI has not won.
        return True  # If not, returns True, meaning the AI has won.

    def generateGuess(self):
        self.__currentGeneratedGuess = None  # Clears the previous guess.
        if self.__attemptsMade != 10:  # Prevents a guess from being generated if there are no more attempts left.
            self.__currentGeneratedGuess = random.choice(self.__alphabet)  # Chooses a random letter.
            self.__alphabet = self.__alphabet.replace(self.__currentGeneratedGuess, "")  # Removes the chosen letter so that it cannot be chosen again.

    def returnCurrentGuess(self):
        return self.__currentGeneratedGuess  # Returns the current guess.

    def setGreyState(self, newState):  # Allows the boolean in self.__greyedOut to be changed.
        self.__greyedOut = newState  # Sets self.__greyedOut to the new boolean state.

    def returnGreyState(self):
        return self.__greyedOut  # Returns the boolean held in self.__greyedOut.

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