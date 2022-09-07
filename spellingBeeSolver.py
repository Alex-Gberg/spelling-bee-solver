import re
import keyboard # TODO requirements file for keyboard module

def getLettersManual():
    letters = list(input("Input the letters as a string, with the first letter as the required letter:\n"))
    while len(letters) != 7 or (len(letters) > len(set(letters))):
        print("INVALID INPUT: Your input must consist of 7 unique letters!")
        letters = list(input("Input the letters as a string, with the first letter as the required letter:\n"))

    return letters

def makeRE(letters):
    alphabet = "".join(letters)

    regEx = "^[" + alphabet + "]*" + letters[0] + "[" + alphabet + "]*$"

    return re.compile(regEx)

def findPossibilities(pattern, fileName):
    possibilities = []
    with open(fileName) as wordList:
        for word in wordList:
            if re.match(pattern, word):
                possibilities.append(word.strip())

    return possibilities

def autoType(words):
    for i, word in enumerate(words):
        print(f"{i+1}: {word}")
        keyboard.write(word+"\n", 0.1)

def findMissingAnswers(guesses, answers):
    missing = []
    for a in answers:
        a = a.strip()
        if a not in guesses:
            missing.append(a)

    return missing

def displayList(list):
    for i, x in enumerate(list):
        print(x, end=", ") if i != len(list)-1 else print(x)

if __name__ == "__main__":
    letters = getLettersManual()

    regEx = makeRE(letters)
    possibilities = findPossibilities(regEx, "words_alpha.txt")

    print(f"{len(possibilities)} possibilities found!")
    inp = input("Type 1 to display the words\nType 2 to auto type the words\n")
    if  inp == "1":
        displayList(possibilities)
    elif inp == "2":
        print("press \"esc\" to start typing")
        keyboard.wait("esc")
        autoType(possibilities)

    if input("Check for missing answers (Only works if you have filled the answers.txt file)? (y/n): ") == "y":
        with open("answers.txt") as answers:
            missingAnswers = findMissingAnswers(possibilities, answers)
        print(f"Missing Answers:")
        displayList(missingAnswers)
