from textEdits import openFile
from textEdits import getSyllabesCZ
from textEdits import getTokenizedList
import math
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
def makeBow(texts_dict):
    global_vocabulary = []

    for text in texts_dict:
        tokenizeText = getTokenizedList(text["data"])
        text.update({"data": tokenizeText})
        global_vocabulary += tokenizeText

    #Unique words in global vocabulary
    global_vocabulary_unique = {}
    global_vocabulary_unique = set(global_vocabulary)

    #Match words with global vocabulary
    for text in texts_dict:
        word_match = []

        for word in global_vocabulary_unique:
            if word in text["data"]:
                word_match += [1]
            else:
                word_match += [0]
                
        text["data"] = word_match

    return texts_dict

# texts = [{"name": "text1", "data": "Jsem jeseter Pepa"},{"name": "text2", "data": "Jsem jeseter Franta"},{"name": "text3", "data": "Nejsem jeseter Franta"}]
# print(makeBow(texts))


# 4) Vytvořte funkci CosineDistance(vektorA, vektorB), která vypočítá kosinovou vzdálenost vektorů A a B
def cosineDistanceNumpy (a, b):
    numerator = sum(np.multiply(a, b))
    denominator = np.multiply(np.sqrt(sum(np.power(a, 2))), np.sqrt(sum(np.power(b, 2))))
    return(numerator / denominator)

def cosineDistance(a, b):
    numerator = m.suma(m.multiply(a, b))
    denominator = math.sqrt(m.suma(m.powerList(a, 2))) * math.sqrt(m.suma(m.powerList(b, 2)))

    return (numerator / denominator)

class m:

    def power(x, n):
        return x**n

    def powerList(c, b):
        result = []
        for num in c:
            result.append(m.power(num, b))
        return result

    def suma(vector):
        sum = 0
        for i in vector:
            sum += i
        return sum

    def multiply(list_a, list_b):
        multiply_list = []
        for num_a, num_b in zip(list_a, list_b):
            multiply_list.append(num_a*num_b)
        return multiply_list


a = [3, 2, 1, 0, 0, 1]
b = [2, 0, 1, 1, 9, 1]


# print(cosineDistance(a, b))
# print(cosineDistanceNumpy(a, b))

# # Kontrola
# from scipy import spatial
# print(1 - spatial.distance.cosine(a, b))




# 5) Vytvořte funkci FolderToBoW, která načte všechny TXT soubory ze zadaného adresáře a vytvoří z nich bag-of-words model.

def folderToBoW(path):
    import glob 
    texts = glob.glob(path + "*.txt") #Os join
    texts_dict = {}
    texts_list = []

    for text in texts:
        texts_dict['name'] = text
        texts_dict['data'] = ''.join(openFile(text))
        texts_list.append(texts_dict.copy())
    
    return makeBow(texts_list)

# print(folderToBoW("assets/"))


# 6) Vytvořte funkci MostSimilar(bow, fileName), která pro zadaný bag-of-words získaný pomocí úlohy (5) a zadaného jména souboru z něj najde k němu nejpodobnější text.
def mostSimilar(pathToFolder, fileName):
    def getDictItem(dicts_list, item, dict_key_naming):
        for dict in dicts_list:
            if item in dict[dict_key_naming]:
                return dict


    def addCosineDistancePair(dicts_list, dict_key_naming):
        for dict in dicts_list:
            similiarity = cosineDistance(chosen_bow[dict_key_naming], dict[dict_key_naming])
            dict["similiarity"] = similiarity
        return dicts_list
    

    def maxValue(dicts_list, dict_key):
        sequence = [dict[dict_key] for dict in dicts_list]
        maxValue = max(sequence)
        maxValueIndex = sequence.index(maxValue)
        return dicts_list[maxValueIndex]

    all_bows = folderToBoW(pathToFolder)
    chosen_bow_name = pathToFolder + fileName

    chosen_bow = getDictItem(all_bows, chosen_bow_name, "name")
    all_bows.remove(chosen_bow)
    all_bows_with_similiarity = addCosineDistancePair(all_bows, "data")

    max_value_bow = maxValue(all_bows_with_similiarity, "similiarity")


    return max_value_bow["name"]

# print(mostSimilar("assets/", "lyric.txt"))

# 7) Funkce MujMap(tokeny, funkceKAplikaci), které zadáváme seznam tokenů a referenci na funkci. Funkce MujMap vrací seznam tokenů po aplikaci funkce funkceKAplikac
def mujMap(tokeny, funct):
    map_result = []
    for i in tokeny:
        funct_applied = funct(i)
        map_result.append(funct_applied)
    return map_result

# print(mujMap(["lapsus", "kapsus", "tropez"], len))

#Co kdybych chtěl volat built in metodu? try/except?


# 8) Vytvořte analogickou funkci k MujMap: MujHromadnyMap, která pro zadaný seznam tokenů aplikuje seznam funkcí
def mujHromadnyMap(map_list, functs_list):
    map_items = map_list

    for funct in functs_list:
        result = mujMap(map_items, funct)
        map_items = result

    return map_items


    
def vynasobDeseti(number):
    return number * 10
print(mujHromadnyMap(["lapsus", "kapsus", "tropez"], [len, vynasobDeseti]))


# 9) Vytvořte funkci MakeTestTrain(dataset, ratio), která pro zadaný seznam kategorií (uvedené v prvním prvku n-tice) vytvoří přípravu na trénovací a testovací datasety v zadaném poměru ratio. Výstupem funkce je dictionare se dvěma klíči: train a test, které jsou seznamy vybraných n-tic dle kategorií pro train a test datasety. Poměr ratio určuje poměr velikosti trénovacího vůči testovacímu datasetu.  Každá kategorie musí být v obou datasetech (train i test) zastoupeny shodně (viz dále).
def makeTestTrain():
    pass
