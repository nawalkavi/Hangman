# Importing the necessary library.
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