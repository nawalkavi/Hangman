# Importing the necessary library.
import random


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