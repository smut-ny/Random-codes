# 9) Vytvořte funkci MakeTestTrain(dataset, ratio), která pro zadaný seznam kategorií (uvedené v prvním prvku n-tice) vytvoří přípravu na trénovací a testovací datasety v zadaném poměru ratio. Výstupem funkce je dictionare se dvěma klíči: train a test, které jsou seznamy vybraných n-tic dle kategorií pro train a test datasety. Poměr ratio určuje poměr velikosti trénovacího vůči testovacímu datasetu.  Každá kategorie musí být v obou datasetech (train i test) zastoupeny shodně (viz dále).
import math
data = [("pes", 1), ("pes", 2), ("pes", 3), ("pes", 4), ("pes", 5), ("jezevec", 1), ("jezevec", 2), ("jezevec", 3), ("jezevec", 4), ("kočka", 1), ("kočka", 2), ("kočka", 3)]


def makeTestTrain(list_of_tuples, ratio):

    def getMinItemCount(list_of_tuples):
        from collections import Counter

        list_of_elements = []

        for tuple in list_of_tuples:
            list_of_elements.append(tuple[0])

        list_of_elements_counter = Counter(list_of_elements).items()
        return min(list_of_elements_counter, key = lambda numb: numb[1])


    def getFeatureNames(list_of_tuples):
        storage = set()
        for item in list_of_tuples:
            storage.add(item[0])
        return storage
    
    def splitTrainTestFunc(feature, test_limit, max_limit):
        for name in feature:
            if name[1] <= test_limit:
                test.append(name) 
            elif name[1] <= max_limit:
                train.append(name)
        
        return test, train

    def splitTrainTestPerFeature(set_of_names):
        feature_list = []
        for name in set_of_names:
            for i in data:
                if i[0] == name:
                    feature_list.append(i)
        return splitTrainTestFunc(feature_list, baseline_test, max_data)


    min_occurances_in_list = getMinItemCount(data)
    set_of_names = getFeatureNames(data)

    rest = 1 - ratio
    baseline_test = math.floor(min_occurances_in_list[1] * ratio)
    baseline_train = math.floor(min_occurances_in_list[1] * rest)
    max_data = baseline_test + baseline_train


    train = []
    test = []
    
    splitTrainTestPerFeature(set_of_names)


    return train, test




print(makeTestTrain(data, 1/3))