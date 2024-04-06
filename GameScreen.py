# Importing the necessary libraries.
import random


# Question.
class Question:

    def __init__(self, wordList, alphabet, screen):
        self.__wordList = wordList
        if type(self.__wordList) != list:
            self.__wordList = []
        self.__alphabet = alphabet
        if type(self.__alphabet) != str:
            self.__alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__screen = screen
        self.__wordLength = None
        self.__attemptsLeft = 0
        self.__matchedWords = []  # Will store all the words with the same length as that of the user.
        self.__completedWord = []  # Will store the correct guesses to progressively form the answer.
        self.__guessedLetters = []  # Will store every letter that has been used as a guess.
        self.__attemptsMade = 0
        self.__blanks = ""
        self.__greyedOut = False

    def generateBlanks(self):
        self.__count = 0
        self.__count += self.__wordLength
        while self.__count != 0:
            self.__completedWord.append("_")
            self.__count -= 1
        self.__blanks = "".join(self.__completedWord)

    def returnBlanks(self):
        return self.__blanks

    def setAnswerPosition(self, letterPosition):
        tempArray = []
        for letter in self.__blanks:
            tempArray.append(letter)
        self.__letterPosition = letterPosition - 1
        tempArray[self.__letterPosition] = self.__currentGuess
        self.__blanks = "".join(tempArray)

    def setWordLength(self, newWordLength):
        self.__wordLength = newWordLength

    def resetWordLength(self):
        self.__wordLength = None

    def returnWordLength(self):
        return self.__wordLength

    def returnLetterPosition(self):
        return self.__letterPosition

    def matchWords(self):
        for i in range(0, len(self.__wordList)):  # Traverses through the list storing every word.
            if len(self.__wordList[i]) == self.__wordLength:  # Checks if a word is the same length as that of the user's input.
                self.__matchedWords.append(self.__wordList[i])  # Appends it to the matchedWords list if it is the same length.

    def returnMatchedWords(self):
        return self.__matchedWords

    def attemptMade(self):
        if self.__attemptsMade < 10:
            self.__attemptsMade += 1

    def returnAttemptsMade(self):
        return self.__attemptsMade

    def checkIfComplete(self):
        for letter in self.__blanks:
            if letter == "_":
                return False
        return True

    def generateGuess(self):
        self.__currentGuess = None
        if self.__attemptsMade != 10:  # Prevents a guess from being generated if there are no more attempts left.
            self.__currentGuess = random.choice(self.__alphabet)
            self.__alphabet = self.__alphabet.replace(self.__currentGuess, "")
            self.__guessedLetters.append(self.__currentGuess)

    def returnCurrentGuess(self):
        return self.__currentGuess

    def returnGuessedLetters(self):
        return self.__guessedLetters

    def greyState(self, newState):
        self.__greyedOut = newState

    def returnGreyState(self):
        return self.__greyedOut

# Hangman.
class Hangman:

    def __init__(self, hangmanDictionary, xPos, yPos, screen):
        self.__hangmanDictionary = hangmanDictionary
        if type(self.__hangmanDictionary) != dict:
            self.__hangmanDictionary = {}
        self.__xPos = xPos
        if not 0 <= self.__xPos <= 1200:
            self.__xPos = 300
        self.__yPos = yPos
        if not 0 <= self.__yPos <= 800:
            self.__xPos = 350
        self.__screen = screen

    def renderHangman(self, attemptsMade):
        self.__attemptsMade = str(attemptsMade)
        self.__currentHangmanImage = self.__hangmanDictionary[self.__attemptsMade]
        self.__hangmanRect = self.__currentHangmanImage.get_rect(center=(self.__xPos, self.__yPos))

    def displayHangman(self):
        self.__screen.blit(self.__currentHangmanImage, self.__hangmanRect)