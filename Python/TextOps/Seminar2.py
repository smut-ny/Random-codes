from textEdits import openFile
from textEdits import getSyllabesCZ
from textEdits import getTokenizedList
import numpy as np
import re


# 1) Napište program, který zadaný textový soubor tokenizuje a uloží jej do vertikály společně s informací o délce tokenu a odhadovaném počtu slabik (využijte již hotové funkce pro získávání informací o tokenu)
def getVerticalCZ(plain_text):
    vertical = ''
    tokenizeText = getTokenizedList(plain_text)
    for word in tokenizeText:
        if word:
            sylabes = getSyllabesCZ(word)
            vertical += word + " | tok: " + str(len(word)) + " syl: " + str(sylabes) + "\n"
    return vertical


# 2) Vytvořte funkci GetTokensFreqs(soubor), která pro zadaný textový soubor získá získá slovník vč. četností jednotlivých slov formou dictionaru, kde klíčem bude slovo a hodnotou jeho frekvence.
def getTokensFreqs(plain_text):
    tokens_list = getTokenizedList(plain_text)
    frequency_table = {}

    for word in tokens_list:
        word_occurrence = tokens_list.count(word)
        frequency_table[word] = word_occurrence
 
    return frequency_table

# následně vytvořte funkci, která z tohoto výsledného slovníku vypočítá TTR (type-to-token ratio) neboli velikost slovníku / délka textu ve slovech, a to pomocí funkce CalcTTRFromDict(slovník)
def CalcTTRFromDict(frequency_table):
    tokens = 0
    types = len(frequency_table)
    frequency_table = frequency_table.items()

    for word, frequency in frequency_table:
        tokens += frequency
    
    type_to_token_ratio = types / tokens
    return type_to_token_ratio

# 3) Funkce MakeBow, která pro zadaný seznam textů zadaných pomocí dictionare obsahující jméno a text (viz příklad) vytvoří model Bag-Of-Words (popis viz níže):
# TODO - Zkontrolovat výsledek, nevím jestli funguje TADY JSEM SKONČIL S REFACTOREM
texts = [{"name": "text1", "data": "Jsem jeseter Pepa"},{"name": "text2", "data": "Jsem jeseter Franta"},{"name": "text3", "data": "Nejsem jeseter Franta"}]

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




# 4) Vytvořte funkci CosineDistance(vektorA, vektorB), která vypočítá kosinovou vzdálenost vektorů A a B
# TODO - JEŠTĚ VERZE BEZ NUMPY


def cosineDistance (a, b):
    citatel = sum(np.multiply(a, b))
    jmenovatel = np.multiply(np.sqrt(sum(np.power(a, 2))), np.sqrt(sum(np.power(b, 2))))
    return(citatel / jmenovatel)

a = [0, 2, 1, 0]
b = [0, 0, 1, 1]
# print(cosineDistance(a,b))

# Funguje to špatně s tímto vektorem, když mám v returnu to 1 - : a = [0, 2, 1, 0] b = [0, 0, 1, 1]
# Kontrola
# from scipy import spatial
# print(1 - spatial.distance.cosine(a, b))


# Alternativa pro np.multiply by mohl být for skrze zip() funkci


# 5) Vytvořte funkci FolderToBoW, která načte všechny TXT soubory ze zadaného adresáře a vytvoří z nich bag-of-words model.

def folderToBoW(path):
    import glob 
    texts = glob.glob(path + "*.txt")
    texts_dict = {}
    texts_list = []

    for text in texts:
        texts_dict['name'] = text
        texts_dict['data'] = ''.join(openFile(text))
        texts_list.append(texts_dict.copy())
    
    return makeBow(texts_list)




    