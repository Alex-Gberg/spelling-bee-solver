import re
from tqdm import tqdm
import enchant
import keyboard

def getLetters():
    letters = list(input("Input the letters as a string, with the first letter as the required letter:\n"))
    while len(letters) != 7 or (len(letters) > len(set(letters))):
        print("INVALID INPUT: Your input must consist of 7 unique letters!")
        letters = list(input("Input the letters as a string, with the first letter as the required letter:\n"))

    return letters

# require >3 letters
def makeRE(letters):
    mustContainRE = f"(?=^.*{letters[0]}.*$)"

    usableLetters = "^["
    for a in letters:
        usableLetters += a
    usableLetters += "]{4,}$"


    return re.compile(mustContainRE + usableLetters)

def findPossibilities(pattern, fileName):
    possibilities = []
    with open(fileName) as wordList:
        for word in wordList:
            if re.match(pattern, word):
                possibilities.append(word.strip())

    return possibilities

def filterWithDictionary(possibilities):
    realPossibilities = []
    numEliminated = 0
    pbar = tqdm(possibilities)
    for p in pbar:
        pbar.set_description(f"Words eliminated: {numEliminated}")
        if enchant.Dict("en_US").check(p):
            realPossibilities.append(p)
        else:
            numEliminated += 1

    return realPossibilities

if __name__ == "__main__":
    letters = getLetters()
    regEx = makeRE(letters)
    possibilities = findPossibilities(regEx, "words_alpha.txt")
    print(f"{len(possibilities)} total possibilities:\n", possibilities)
    realPossibilities = filterWithDictionary(possibilities)
    print(f"{len(realPossibilities)} real possibilities:\n", realPossibilities)
