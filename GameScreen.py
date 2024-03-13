import pygame
import random


# Game.
class GameScreen:

    def __init__(self, wordList, wordLength):
        self.__wordList = wordList
        self.__wordLength = wordLength
        self.__matchedWords = []  # Will store all the words with the same length as that of the user.
        self.__completedWord = []  # Will store the correct guesses to progressively form the answer.
        self.__guessedLetters = []  # Will store every letter that has been used as a guess.

    def matchWords(self):
        for i in range(0, len(self.__wordList)):  # Traverses through the list storing every word.
            if len(self.__wordList[i]) == self.__wordLength:  # Checks if a word is the same length as that of the user's input.
                self.__matchedWords.append(self.__wordList[i])  # Appends it to the matchedWords list if it is the same length.

    def scaleAttempts(self):  # Sets the number of attempts depending on how many letters the word has.
        self.__attempts = 0
        if 1 <= self.__wordLength <= 3:
            self.__attempts = 5
        elif 4 <= self.__wordLength <= 7:
            self.__attempts = 10
        elif 8 <= self.__wordLength <= 11:
            self.__attempts = 15
        elif self.__wordLength >= 12:
            self.__attempts = 20

    def generateGuess(self):
        self.__currentWord = None
        self.__currentLetter = None
        if self.__attempts != 0:  # Prevents a guess from being generated if there are no more attempts left.
            self.__currentWord = random.choice(self.__matchedWords)  # Makes a random word choice from the list of matched words.
            self.__currentLetter = self.__currentWord[random.randint(0, len(self.__currentWord) - 1)]  # Chooses a random letter from the chosen word.

    def checkGuess(self):
        for i in self.__guessedLetters:
            if self.__guessedLetters[i] == self.__currentLetter:
                return False

    # def drawHangman(self):

