from textEdits import openFile
from textEdits import sylabesNumCZ
from textEdits import getTokenizedList
import re

rawText = openFile("/Users/smutny/Documents/Coding/_github/Random-codes/Uni/Python/lyric.txt")



# 1) Napište program, který zadaný textový soubor tokenizuje a uloží jej do vertikály společně s informací o délce tokenu a odhadovaném počtu slabik (využijte již hotové funkce pro získávání informací o tokenu)


def getVerticalCZ(rawText):
    vertical = ''
    tokenizeText = getTokenizedList(rawText)
    for word in tokenizeText:
        if word:
            sylabes = sylabesNumCZ(word)
            vertical += word + " | tok: " + str(len(word)) + " syl: " + str(sylabes) + "\n"
    return vertical



# 2) Vytvořte funkci GetTokensFreqs(soubor), která pro zadaný textový soubor získá získá slovník vč. četností jednotlivých slov formou dictionaru, kde klíčem bude slovo a hodnotou jeho frekvence.

 

def getTokensFreqs(rawText):
    tokenizedList = getTokenizedList(rawText)
    # tokenizedList.sort() Kdybych to chtěl abecedně
    freqTable = {}

    for word in tokenizedList:
        frequency = tokenizedList.count(word)
        freqTable[word] = frequency
 
    return freqTable

# následně vytvořte funkci, která z tohoto výsledného slovníku vypočítá TTR (type-to-token ratio) neboli velikost slovníku / délka textu ve slovech, a to pomocí funkce CalcTTRFromDict(slovník)
def CalcTTRFromDict(freqTable):
    freqTable = freqTable.items()
    tokens = 0
    types = len(freqTable)

    for key, value in freqTable:
        tokens += value
    
    TTR = types / tokens
    return TTR

# print(getTokensFreqs(rawText))


# 3) Funkce MakeBow, která pro zadaný seznam textů zadaných pomocí dictionare obsahující jméno a text (viz příklad) vytvoří model Bag-Of-Words (popis viz níže):

texts = [{"name": "text1", "data": "Já jsem vojta Ahoj ?? ahoj Vojta"},{"name": "text2", "data": "Já nejsem Vojta, ale mohl bych být"}]

def makeBow(texts):
    globalVocabulary = {}
    tokList = []

    #Convert dictionare into global vocabulary and tokenize words
    for data in texts:
        tokenizeText = getTokenizedList([data["data"]])
        tokList += tokenizeText
        #Update original dictionare data string with tokenized list
        data.update({"data": tokenizeText})

    #Only unique words
    globalVocabulary = set(tokList)

    #Match texts
    for data in texts:
        matchedWords = []

        for word in globalVocabulary:
            if word in data["data"]:
                matchedWords += [1]
            else:
                matchedWords += [0]
                
        data["data"] = matchedWords

    return texts

print(makeBow(texts))

# Co musím udělat
# [ ] Tokenizovat 
# [ ] Globální slovník
# [ ] Validaci

