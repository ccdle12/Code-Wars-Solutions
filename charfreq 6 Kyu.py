import re
def letter_frequency(text):

    hashTable = {}
    cleanString = re.sub("[^A-Za-z]+", "", text).lower()

    for eachLetter in cleanString:
        hashTable[eachLetter] = hashTable.get(eachLetter, 0) + 1

    listByAlpha = sorted(hashTable.items(), key=lambda x: x[0])
    outputList = sorted(listByAlpha, key=lambda x: x[1], reverse=True)
    print outputList

letter_frequency('JJJKKKbb')
