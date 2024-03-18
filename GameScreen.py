# Importing the necessary libraries.
import pygame
import random
from Text import TextButton


# Game.
class Question:

    def __init__(self, wordList, screen):
        self.__wordList = wordList
        self.__wordLength = None
        self.__screen = screen
        self.__attemptsLeft = 0
        self.__matchedWords = []  # Will store all the words with the same length as that of the user.
        self.__completedWord = []  # Will store the correct guesses to progressively form the answer.
        self.__guessedLetters = []  # Will store every letter that has been used as a guess.
        self.__textButton = TextButton("", "Black", "Yellow", 800, 400, 70, self.__screen)
        self.__grid = ""

    def matchWords(self):
        for i in range(0, len(self.__wordList)):  # Traverses through the list storing every word.
            if len(self.__wordList[i]) == self.__wordLength:  # Checks if a word is the same length as that of the user's input.
                self.__matchedWords.append(self.__wordList[i])  # Appends it to the matchedWords list if it is the same length.

    def setLength(self, wordLength):
        if self.__wordLength is None:
            self.__wordLength = wordLength

    def resetLength(self):
        self.__wordLength = None


    # Prototype 2.
    # def scaleAttempts(self):  # Sets the number of attempts depending on how many letters the word has.
    #     self.__doneOnce = False  # Ensures this method is only run once.
    #     if not self.__doneOnce:
    #         if 1 <= self.__wordLength <= 3:
    #             self.__attemptsLeft = 5
    #         elif 4 <= self.__wordLength <= 7:
    #             self.__attemptsLeft = 10
    #         elif 8 <= self.__wordLength <= 11:
    #             self.__attemptsLeft = 15
    #         elif self.__wordLength >= 12:
    #             self.__attemptsLeft = 20
    #     self.__doneOnce = True



    def generateGuess(self):
        self.__currentWord = None
        self.__currentLetter = None
        if self.__attemptsLeft != 0:  # Prevents a guess from being generated if there are no more attempts left.
            self.__currentWord = random.choice(self.__matchedWords)  # Makes a random word choice from the list of matched words.
            self.__currentLetter = self.__currentWord[random.randint(0, len(self.__currentWord) - 1)]  # Chooses a random letter from the chosen word.

    def checkIfGuessed(self):
        for i in self.__guessedLetters:
            if self.__guessedLetters[i] == self.__currentLetter:
                return True  # Returns True if the current letter has already been guessed once.

    def displayQuestion(self):
        self.__textButton.setText(f"Is {self.__currentLetter} in your word?")
        # Try to detect click on yes or no.

    def grid(self):
        self.__count = 0
        self.__count += self.__wordLength
        while self.__count != 0:
            self.__completedWord.append("_")
            self.__count -= 1
        self.__grid = " ".join(self.__completedWord)



class Hangman:

    def __init__(self, hangmanDictionary, screen):
        self.__screen = screen
        self.__hangmanDictionary = hangmanDictionary
        self.__attemptsLeft = 0

    def returnCurrentHangmanCount(self):
        self.__currentHangmanCount = 10 - self.__attemptsLeft
        return self.__currentHangmanCount

    def createHangmanRect(self):
        self.__currentHangmanImage = self.__hangmanDictionary[self.__currentHangmanCount]
        self.__hangmanRect = self.__currentHangmanImage.get_rect(center=(100, 100))

    def displayHangman(self):
        self.__screen.blit(self.__currentHangmanImage, self.__hangmanRect)