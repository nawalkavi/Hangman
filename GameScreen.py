# Importing the necessary libraries.
import random


# User.
class User:

    def __init__(self, wordList):  # Constructor for the class; takes all the necessary parameters.
        self.__wordList = wordList
        if type(self.__wordList) != list:  # Validates that the value entered for self.__wordList is a list data type.
            self.__wordList = []  # If not, assigns it a default value of an empty list.
        self.__blanks = ""
        self.__guessedLetters = []
        self.__attemptsMade = 0  # Starts at 0 and ends at 10.

    def chooseWord(self):
        self.__chosenWord = None
        self.__chosenWord = random.choice(self.__wordList)  # Chooses a random word from self.__wordList.
        while len(self.__chosenWord) >= 10:  # Checks if the length of the chosen word is more than or equal to 10.
            self.__chosenWord = random.choice(self.__wordList)  # If so, keeps choosing a different word until the length is less than 10.

    def checkLetterDuplicates(self):
        self.__letter = None  # Holding variable to store an individual letter inside self.__chosenWord.
        self.__seenLetters = set()  # Using set() removes all duplicate letters.
        for self.__letter in self.__chosenWord:  # Traverses through every letter in self.__chosenWord.
            if self.__letter in self.__seenLetters:  # Checks if the current letter is inside self.__seenLetters.
                return False  # If so, returns False, meaning there is a duplicate.
            self.__seenLetters.add(self.__letter)  # Adds the current letter to the self.__seenLetters set.
        return True  # If there are no duplicates, returns True.

    def returnChosenWord(self):
        return self.__chosenWord  # Returns the word chosen.

    def checkLetter(self):
        self.__letterPosition = 0
        for letter in self.__chosenWord:  # Traverses through every letter in the chosen word.
            if letter == self.__letterGuessed:  # Checks if the current letter is equal to the user's guess.
                return True  # If so, returns True.
            self.__letterPosition += 1  # If not, increments self.__letterPosition by 1.
        return False  # Returns False since the guess was not in the word.

    def generateBlanks(self):
        count = 0  # Temporary variable to hold a value.
        tempArray = []  # Temporary array to hold the blanks.
        count += len(self.__chosenWord)
        while count != 0:  # While count does not match the user's word length.
            tempArray.append("_")  # An underscore is appended to tempArray for every time the loop is run to create the blanks array.
            count -= 1  # 1 is subtracted from count to eventually have it match the user's word length.
        self.__blanks = "".join(tempArray)  # Converts tempArray into a string, which creates the blanks string.

    def updateBlanks(self):
        tempArray = []  # Temporary variable to hold each position of the blanks as a position in an array.
        for letter in self.__blanks:  # Traverses through every position in self.__blanks.
            tempArray.append(letter)  # Appends each position to tempArray.
        tempArray[self.__letterPosition] = self.__letterGuessed  # Uses self.__letterPosition from self.checkLetter() as an index and replaces it with the user's guess.
        self.__blanks = "".join(tempArray)  # Converts the array back into a string to be used for blanksText.

    def checkIfComplete(self):
        for letter in self.__blanks:  # Traverses through every position in self.__blanks.
            if letter == "_":  # Checks if the current position is an underscore - a blank.
                return False  # If so, returns False, meaning the word is not completed.
        return True  # If not, returns True, meaning the word is complete.

    def returnBlanks(self):
        return self.__blanks  # Returns the blanks.

    def letterGuess(self, letterGuessed):
        self.__letterGuessed = letterGuessed  # Allows the user to guess.

    def storeGuess(self):
        for letter in self.__guessedLetters:  # Traverses through every letter that has been used as a guess so far.
            if letter == self.__letterGuessed:  # Checks if the current letter input matches the current already guessed letter.
                return None  # If so, returns None to end the function.
        self.__guessedLetters.append(self.__letterGuessed)  # If no match is found, the new letter input is added to the list.

    def checkIfGuessed(self):
        for letter in self.__guessedLetters:  # Traverses through every letter that has been used as a guess so far.
            if self.__letterGuessed == letter:  # Checks if the current letter input matches the current already guessed letter.
                return True  # If so, returns True, meaning it has already been used as a guess previously inside the round.
        return False  # If not, returns False, meaning it is a new guess.

    def returnLetterGuessed(self):
        return self.__letterGuessed  # Returns the user's guessed letter.

    def attemptMade(self):
        self.__attemptsMade += 1  # Increments the number of attempts by 1; a maximum of 10 is allowed before a loss.

    def resetAttempts(self):
        self.__attemptsMade = 0  # Resets the number of attempts made back to 0.

    def returnAttemptsMade(self):
        return self.__attemptsMade  # Returns the number of attempts made by the user.


# Question.
class Question:

    def __init__(self, vowels, consonants):
        self.__vowels = vowels
        if type(self.__vowels) != str:  # Validates that the value entered for self.__vowels is a string data type.
            self.__vowels = "AEIOU"  # If not, assigns it a default value of a string containing the vowels.
        self.__consonants = consonants
        if type(self.__consonants) != str:  # Validates that the value entered for self.__consonants. is a string data type.
            self.__consonants = "BCDFGHJKLMNPQRSTVWXYZ"  # If not, assigns it a default value of a string containing the consonants.
        self.__wordLength = None  # Will be assigned a value depending on the user's input.
        self.__matchedWords = []  # Will store all the words with the same length as that of the user.
        self.__attemptsMade = 0  # Starts at 0 and ends at 10.
        self.__blanks = ""  # Will be assigned the appropriate number of underscores in a string as per the word length.
        self.__greyedOut = False  # Controls whether confirmGameText is greyed out or not when computerGameActive is True.
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
        if self.__currentGeneratedGuess is not None:  # Checks if there is currently a valid guessed letter.
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

    def resetAttempts(self):
        self.__attemptsMade = 0  # Resets the number of attempts used back to 0.

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
            if self.__vowels != "":  # Checks if there are still vowels left to guess.
                self.__currentGeneratedGuess = random.choice(self.__vowels)  # Chooses a random vowel.
                self.__vowels = self.__vowels.replace(self.__currentGeneratedGuess, "")  # Removes the chosen vowel from the string to prevent double guessing.
            elif self.__vowels == "":  # Checks if all the vowels have been used as guesses.
                self.__currentGeneratedGuess = random.choice(self.__consonants)  # Chooses a random consonant.
                self.__consonants = self.__consonants.replace(self.__currentGeneratedGuess, "")  # Removes the chosen consonant so that it cannot be chosen again.

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