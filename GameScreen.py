# Importing the necessary libraries.
import random


# Question.
class Question:

    def __init__(self, wordList, alphabetString, screen):
        self.__wordList = wordList
        self.__alphabetString = alphabetString
        self.__screen = screen
        self.__wordLength = None
        self.__attemptsLeft = 0
        self.__matchedWords = []  # Will store all the words with the same length as that of the user.
        self.__completedWord = []  # Will store the correct guesses to progressively form the answer.
        self.__guessedLetters = []  # Will store every letter that has been used as a guess.
        self.__grid = ""

    def generateGrid(self):
        self.__count = 0
        self.__count += self.__wordLength
        while self.__count != 0:
            self.__completedWord.append("_")
            self.__count -= 1
        self.__grid = " ".join(self.__completedWord)

    def returnGrid(self):
        return self.__grid

    def setWordLength(self, newWordLength):
        self.__wordLength = newWordLength

    def resetWordLength(self):
        self.__wordLength = None

    def returnWordLength(self):
        return self.__wordLength

    def matchWords(self):
        for i in range(0, len(self.__wordList)):  # Traverses through the list storing every word.
            if len(self.__wordList[i]) == self.__wordLength:  # Checks if a word is the same length as that of the user's input.
                self.__matchedWords.append(self.__wordList[i])  # Appends it to the matchedWords list if it is the same length.

    def returnMatchedWords(self):
        return self.__matchedWords

    def scaleAttempts(self):  # Sets the number of attempts depending on how many letters the word has.
        self.__doneOnce = False  # Ensures this method is only run once.
        if not self.__doneOnce:
            if 1 <= self.__wordLength <= 3:
                self.__attemptsLeft = 5
            elif 4 <= self.__wordLength <= 7:
                self.__attemptsLeft = 10
            elif 8 <= self.__wordLength <= 11:
                self.__attemptsLeft = 15
            elif self.__wordLength >= 12:
                self.__attemptsLeft = 20
        self.__doneOnce = True

    def removeAttempt(self):
        self.__attemptsLeft -= 1

    def returnAttemptsLeft(self):
        return self.__attemptsLeft

    def generateGuess(self):
        self.__currentGuess = None
        if self.__attemptsLeft != 0:  # Prevents a guess from being generated if there are no more attempts left.
            self.__currentGuess = random.choice(self.__alphabetString)
            self.__alphabetString = self.__alphabetString.replace(self.__currentGuess, "")
            self.__guessedLetters.append(self.__currentGuess)

    def returnCurrentGuess(self):
        return self.__currentGuess

    def returnGuessedLetters(self):
        return self.__guessedLetters


# Hangman.
class Hangman:

    def __init__(self, hangmanDictionary, screen):
        self.__hangmanDictionary = hangmanDictionary
        self.__screen = screen

    def returnCurrentHangmanCount(self, attemptsLeft):
        self.__attemptsLeft = attemptsLeft
        self.__currentHangmanCount = 10 - self.__attemptsLeft
        return self.__currentHangmanCount

    def createHangmanRect(self):
        self.__currentHangmanImage = self.__hangmanDictionary[self.__currentHangmanCount]
        self.__hangmanRect = self.__currentHangmanImage.get_rect(center=(100, 100))

    def displayHangman(self):
        self.__screen.blit(self.__currentHangmanImage, self.__hangmanRect)
