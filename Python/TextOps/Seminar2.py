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
def mostSimilar(pathToFolder, targetFileName):
    import os
    
    def getDictItem(list_of_dicts, target_dict, dict_key_file_name):
        for dict in list_of_dicts:
            if target_dict in dict[dict_key_file_name]:
                return dict


    def addCosineDistanceAsDictKey(list_of_dicts, dict_key_bow_data):
        for dict in list_of_dicts:
            similiarity = cosineDistance(target_bow[dict_key_bow_data], dict[dict_key_bow_data])

            #adds similiarity calculation as a new key to existing dictionare
            dict["similiarity"] = similiarity
        return list_of_dicts
    

    def getMaxDictValue(list_of_dicts, dict_key_similiarity):
        list_of_similiarity = [dict[dict_key_similiarity] for dict in list_of_dicts]
        max_value_in_list = max(list_of_similiarity)
        max_value_list_index = list_of_similiarity.index(max_value_in_list)
        return list_of_dicts[max_value_list_index]

    bows_dict_list = folderToBoW(pathToFolder)
    target_file_dict_key_name = os.path.join(pathToFolder, targetFileName)

    target_bow = getDictItem(bows_dict_list, target_file_dict_key_name, "name")
    bows_dict_list.remove(target_bow)
    bows_with_similiarity_key = addCosineDistanceAsDictKey(bows_dict_list, "data")

    bow_with_max_similiarity_value = getMaxDictValue(bows_with_similiarity_key, "similiarity")
    
    return bow_with_max_similiarity_value["name"]

# print(mostSimilar("assets/", "lyric.txt"))

# 
# DATA STRUCTURE:
# [{'name': 'assets/3.txt', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'similiarity': 0.0}, {'name': 'assets/2.txt', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'similiarity': 0.23904572186687878}, {'name': 'assets/1.txt', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'similiarity': 0.0}])

# 7) Funkce MujMap(tokeny, funkceKAplikaci), které zadáváme seznam tokenů a referenci na funkci. Funkce MujMap vrací seznam tokenů po aplikaci funkce funkceKAplikac
def mujMap(tokeny, funct):
    map_result = []
    for token in tokeny:
        funct_applied = funct(token)
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


    
# def vynasobDeseti(number): return number * 10
# print(mujHromadnyMap(["lapsus", "kapsus", "tropez"], [len, vynasobDeseti]))


# 9) Vytvořte funkci MakeTestTrain(dataset, ratio), která pro zadaný seznam kategorií (uvedené v prvním prvku n-tice) vytvoří přípravu na trénovací a testovací datasety v zadaném poměru ratio. Výstupem funkce je dictionare se dvěma klíči: train a test, které jsou seznamy vybraných n-tic dle kategorií pro train a test datasety. Poměr ratio určuje poměr velikosti trénovacího vůči testovacímu datasetu.  Každá kategorie musí být v obou datasetech (train i test) zastoupeny shodně (viz dále).

data = [("pes", 1), ("pes", 2), ("pes", 3), ("pes", 4), ("pes", 5), ("jezevec", 1), ("jezevec", 2), ("jezevec", 3), ("jezevec", 4), ("kočka", 1), ("kočka", 2), ("kočka", 3)]


def makeTestTrain(dataset, ratio):
    pass


# Nejméně četná kategorie??
def getMinItemCount(list_of_tuples):
    from collections import Counter

    list_of_elements = []

    for tuple in list_of_tuples:
        list_of_elements.append(tuple[0])

    list_of_elements_counter = Counter(list_of_elements).items()
    return min(list_of_elements_counter, key = lambda numb: numb[1])


# Get all names
def getUniqueNames(list_of_tuples):
    storage = set()
    for item in list_of_tuples:
        storage.add(item[0])
    return storage

        
min_occurances_in_list = getMinItemCount(data)
set_of_names = getUniqueNames(data)
ratio = 2/3


# Pro každé jméno funkce, co rozdělí list

def splitTrainTest(ratio, list_of_tuples):
    train = []
    test = []

    rest = 1 - ratio
    baseline_test = min_occurances_in_list[1] * ratio
    baseline_train = min_occurances_in_list[1] * rest

    print(baseline_test, baseline_train)

    for name in list_of_tuples:
        if name[1] > baseline_test:
            test.append(name) 
        elif name[1] < baseline_train:
            train.append(name)

    return train, test
data_pes = ("pes", 1), ("pes", 2), ("pes", 3), ("pes", 4), ("pes", 5)
print(splitTrainTest(ratio, data_pes))





# print(makeTestTrain(data, 20))

