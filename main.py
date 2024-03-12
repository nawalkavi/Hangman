import random

with open("Assets//Word Dictionary//words_alpha.txt", "r") as f:
    data = f.read()
dataList = data.split("\n")
dataList = [word.upper() for word in dataList]

print("Think of a word! How many letters does it have?")
wordLength = int(input("Answer: "))

matchedWords = []
wordMaster = []
gridCount = wordLength + 0
while gridCount > 0:
    wordMaster.append("_")
    gridCount -= 1
guessedLetters = []
print(wordMaster)


for i in range(0, len(dataList)):
    if len(dataList[i]) == wordLength:
        matchedWords.append(dataList[i])

guessed = False
attempts = 10
while attempts != 0:
    if not guessed:
        currentWord = random.choice(matchedWords)
        currentLetter = currentWord[random.randint(0, len(currentWord) - 1)]
        isAvailable = False

        for i in range(0, len(guessedLetters)):
            if guessedLetters[i] == currentLetter:
                isAvailable = False
                currentWord = random.choice(matchedWords)
                currentLetter = currentWord[random.randint(0, len(currentWord) - 1)]
            else:
                isAvailable = True

        print(f"\nIs {currentLetter} in the word?")
        answer = input("Answer: ")
        if answer == "yes" or answer == "Yes":
            attempts += 0
            print("How many times?")
            count = int(input("Answer: "))
            while count != 0:
                print("What position?")
                position = int(input("Answer: "))
                wordMaster[position - 1] = currentLetter
                print(wordMaster)
                count -= 1
            guessedLetters.append(currentLetter)
            print("Attempts:", attempts)
        elif answer == "no" or answer == "No":
            attempts -= 1
            guessedLetters.append(currentLetter)
            print(wordMaster)
            print("Attempts:", attempts)
        guessed = True
        for letter in wordMaster:
            if letter == "_":
                guessed = False