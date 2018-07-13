import random
import operator

def noDamage():
    print("  |----")
    print("      |")
    print("      |")
    print("      |")
    print("      |")
    print("     ---")
def oneDamage():
    print("  |----")
    print("  O   |")
    print("      |")
    print("      |")
    print("      |")
    print("     ---")
def twoDamage():
    print("  |----")
    print("  O   |")
    print("  |   |")
    print("      |")
    print("      |")
    print("     ---")
def threeDamage():
    print("  |----")
    print("  O   |")
    print("  |   |")
    print(" /    |")
    print("      |")
    print("     ---")
def fourDamage():
    print("  |----")
    print("  O   |")
    print("  |   |")
    print(" /    |")
    print("      |")
    print("     ---")
def fiveDamage():
    print("  |----")
    print("  O   |")
    print("  |   |")
    print(" / \  |")
    print("      |")
    print("     ---")
def sixDamage():
    print("  |----")
    print("  O   |")
    print(" -|   |")
    print(" / \  |")
    print("      |")
    print("     ---")
def sevenDamage():
    print("  |----")
    print("  O   |")
    print(" -|-  |")
    print(" / \  |")
    print("      |")
    print("     ---")

def playBeginner():
    beginner = ["tiger", "elephant", "blue", "apple", "morning", "snow", "green", "rainbow", "taco"]
    noDamage()
    word = random.choice(beginner)
    guessed = []
    l = len(word)
    blank = ""
    for x in range(l):
        blank += "_"
    wrong = 0
    print(blank)
    while wrong < 7 and blank != word:
        guess = input("Please enter a letter guess: ")
        if guess in guessed:
            print("You have already guessed this letter.")
            continue
        guessed.append(guess)
        if(guess in word):
            print("Correct!")
            for y in range(l):
                if(word[y] == guess):
                    b = list(blank)
                    b[y] = guess
                    blank = "".join(b)
                else:
                    continue
            print(blank)
        else:
            print("Sorry, that's incorrect")
            wrong += 1
            if(wrong == 1):
                oneDamage()
            elif(wrong == 2):
                twoDamage()
            elif(wrong == 3):
                threeDamage()
            elif(wrong == 4):
                fourDamage()
            elif(wrong == 5):
                fiveDamage()
            elif(wrong == 6):
                sixDamage()
            elif(wrong == 7):
                sevenDamage()
        if(blank == word):
            print("You win!")
            break
        if wrong == 7:
            print("I'm sorry, you lose.")

def playIntermediate():
    intermediate = ["design", "pineapple", "dusk", "incredible", "violet", "thunderstorm"]
    noDamage()
    word = random.choice(intermediate)
    guessed = []
    l = len(word)
    blank = ""
    for x in range(l):
        blank += "_"
    wrong = 0
    print(blank)
    while wrong < 7 and blank != word:
        guess = input("Please enter a letter guess: ")
        if guess in guessed:
            print("You have already guessed this letter.")
            continue
        guessed.append(guess)
        if(guess in word):
            print("Correct!")
            for y in range(l):
                if(word[y] == guess):
                    b = list(blank)
                    b[y] = guess
                    blank = "".join(b)
                else:
                    continue
            print(blank)
        else:
            print("Sorry, that's incorrect")
            wrong += 1
            if(wrong == 1):
                oneDamage()
            elif(wrong == 2):
                twoDamage()
            elif(wrong == 3):
                threeDamage()
            elif(wrong == 4):
                fourDamage()
            elif(wrong == 5):
                fiveDamage()
            elif(wrong == 6):
                sixDamage()
            elif(wrong == 7):
                sevenDamage()
        if(blank == word):
            print("You win!")
            break
        if wrong == 7:
            print("I'm sorry, you lose.")
def playAdvanced():
    advanced = ["jazz", "galaxy", "gazebo", "oxygen", "rhythm", "fluff", "millennium"]
    noDamage()
    word = random.choice(advanced)
    guessed = []
    l = len(word)
    blank = ""
    for x in range(l):
        blank += "_"
    wrong = 0
    print(blank)
    while wrong < 7 and blank != word:
        guess = input("Please enter a letter guess: ")
        if guess in guessed:
            print("You have already guessed this letter.")
            continue
        guessed.append(guess)
        if(guess in word):
            print("Correct!")
            for y in range(l):
                if(word[y] == guess):
                    b = list(blank)
                    b[y] = guess
                    blank = "".join(b)
                else:
                    continue
            print(blank)
        else:
            print("Sorry, that's incorrect")
            wrong += 1
            if(wrong == 1):
                oneDamage()
            elif(wrong == 2):
                twoDamage()
            elif(wrong == 3):
                threeDamage()
            elif(wrong == 4):
                fourDamage()
            elif(wrong == 5):
                fiveDamage()
            elif(wrong == 6):
                sixDamage()
            elif(wrong == 7):
                sevenDamage()
        if(blank == word):
            print("You win!")
            break
        if wrong == 7:
            print("I'm sorry, you lose.")
def playAnimalsBeginner():
    beginner2 = ["panda", "wolf", "crab", "hippo", "lion", "cat"]
    noDamage()
    word = random.choice(beginner2)
    guessed = []
    l = len(word)
    blank = ""
    for x in range(l):
        blank += "_"
    wrong = 0
    print(blank)
    while wrong < 7 and blank != word:
        guess = input("Please enter a letter guess: ")
        if guess in guessed:
            print("You have already guessed this letter.")
            continue
        guessed.append(guess)
        if(guess in word):
            print("Correct!")
            for y in range(l):
                if(word[y] == guess):
                    b = list(blank)
                    b[y] = guess
                    blank = "".join(b)
                else:
                    continue
            print(blank)
        else:
            print("Sorry, that's incorrect")
            wrong += 1
            if(wrong == 1):
                oneDamage()
            elif(wrong == 2):
                twoDamage()
            elif(wrong == 3):
                threeDamage()
            elif(wrong == 4):
                fourDamage()
            elif(wrong == 5):
                fiveDamage()
            elif(wrong == 6):
                sixDamage()
            elif(wrong == 7):
                sevenDamage()
        if(blank == word):
            print("You win!")
            break
        if wrong == 7:
            print("I'm sorry, you lose.")
def playAnimalsIntermediate():
    inter = ["squid", "gnat", "goose", "jellyfish", "koala"]
    noDamage()
    word = random.choice(inter)
    guessed = []
    l = len(word)
    blank = ""
    for x in range(l):
        blank += "_"
    wrong = 0
    print(blank)
    while wrong < 7 and blank != word:
        guess = input("Please enter a letter guess: ")
        if guess in guessed:
            print("You have already guessed this letter.")
            continue
        guessed.append(guess)
        if(guess in word):
            print("Correct!")
            for y in range(l):
                if(word[y] == guess):
                    b = list(blank)
                    b[y] = guess
                    blank = "".join(b)
                else:
                    continue
            print(blank)
        else:
            print("Sorry, that's incorrect")
            wrong += 1
            if(wrong == 1):
                oneDamage()
            elif(wrong == 2):
                twoDamage()
            elif(wrong == 3):
                threeDamage()
            elif(wrong == 4):
                fourDamage()
            elif(wrong == 5):
                fiveDamage()
            elif(wrong == 6):
                sixDamage()
            elif(wrong == 7):
                sevenDamage()
        if(blank == word):
            print("You win!")
            break
        if wrong == 7:
            print("I'm sorry, you lose.")
def playAnimalsAdvanced():
    advancedAnimals = ["hyena", "lemur", "mosquito", "quail", "herring", "giraffe"]
    noDamage()
    word = random.choice(advancedAnimals)
    guessed = []
    l = len(word)
    blank = ""
    for x in range(l):
        blank += "_"
    wrong = 0
    print(blank)
    while wrong < 7 and blank != word:
        guess = input("Please enter a letter guess: ")
        if guess in guessed:
            print("You have already guessed this letter.")
            continue
        guessed.append(guess)
        if(guess in word):
            print("Correct!")
            for y in range(l):
                if(word[y] == guess):
                    b = list(blank)
                    b[y] = guess
                    blank = "".join(b)
                else:
                    continue
            print(blank)
        else:
            print("Sorry, that's incorrect")
            wrong += 1
            if(wrong == 1):
                oneDamage()
            elif(wrong == 2):
                twoDamage()
            elif(wrong == 3):
                threeDamage()
            elif(wrong == 4):
                fourDamage()
            elif(wrong == 5):
                fiveDamage()
            elif(wrong == 6):
                sixDamage()
            elif(wrong == 7):
                sevenDamage()
        if(blank == word):
            print("You win!")
            break
        if wrong == 7:
            print("I'm sorry, you lose.")
def helper():
    level = input("Please enter your level option (beginner, intermediate, advanced, beginner animals, intermediate animals, advanced animals): ")
    if level == "beginner" or level == "Beginner":
        playBeginner()
    elif level == "intermediate" or level == "Intermediate":
        playIntermediate()
    elif level == "advanced" or level == "Advanced":
        playAdvanced()
    elif level == "beginner animals" or level == "Beginner animals":
        playAnimalsBeginner()
    elif level == "intermediate animals" or level == "Intermediate animals":
        playAnimalsIntermediate()
    elif level == "advanced animals" or level == "Advanced animals":
        playAnimalsAdvanced()
helper()
