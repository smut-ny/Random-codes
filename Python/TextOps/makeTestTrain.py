#příliš mnoho forů, result na začátek, 



import math
from collections import Counter

data = [("pes", 1), ("pes", 2), ("pes", 3), ("pes", 4), ("pes", 5), ("jezevec", 1), ("jezevec", 2), ("jezevec", 3), ("jezevec", 4), ("kočka", 1), ("kočka", 2), ("kočka", 3)]

# Alternative random data verification ------------------------>

def data_generator(list_of_features, times, random_rat):
    from random import randrange
    storage = []
    rand = 1

    if random_rat == True:
        rand = randrange(1, 9)


    for name in list_of_features:
        # Resets
        id = 0
        tuple_item = ()
        for i in range(0, int(times / rand)):
            id += 1
            tuple_item = (name, id)
            storage.append(tuple_item)
    
    return storage

data2 = data_generator(["habanero", "jalapeno", "nagaJolokia", "bhutJolokia"], 400, True)
# <--------------


def makeTestTrain(data_to_split, ratio):


    def getMinOccurrenceItemInList(list_of_tuples):
        all_items_list = []

        for tuple in list_of_tuples:
            all_items_list.append(tuple[0])

        unique_items_counted = Counter(all_items_list).items()

        return min(unique_items_counted, key = lambda number: number[1])


    def getUniqueNames(list_of_tuples):
        unique_names = set()

        for item in list_of_tuples:
            unique_names.add(item[0])

        return unique_names
    
    def splitTrainTestFunc(data_to_split, test_limit, max_limit):
        train_after_split = []
        test_after_split = []

        for item_id in data_to_split:

            if item_id[1] <= test_limit:
                test_after_split.append(item_id) 
            elif item_id[1] <= max_limit:
                train_after_split.append(item_id)
        
        return test_after_split, train_after_split

    def splitTrainTestPerItem(list_of_tuples, set_of_names):
        list_of_unique_items = []

        for name in set_of_names:

            for item in list_of_tuples:

                if item[0] == name:
                    list_of_unique_items.append(item)

        return splitTrainTestFunc(list_of_unique_items, baseline_test, split_max_borderline)


    min_occurances_in_list = getMinOccurrenceItemInList(data_to_split)
    set_of_unique_items = getUniqueNames(data_to_split)

    baseline_test = math.floor(min_occurances_in_list[1] * ratio)
    baseline_train = math.floor(min_occurances_in_list[1] * (1 - ratio))

    split_max_borderline = baseline_test + baseline_train

 
    train_test_split_return = []
    
    train_test_split_return = splitTrainTestPerItem(data_to_split, set_of_unique_items)


    return train_test_split_return

print("\n Kočka, pes, jezevec:")
print(makeTestTrain(data, 2/3))




# Alternative random data verification ------------------------>
print("\n Alternative data SUM:")
def validateSplit(input):
    
    validation = []
    tuple_list = []
    
    for test_train_list in input:
        for tuple in test_train_list:
            tuple_list.append(tuple[0])
            
        sum_all_items = Counter(tuple_list).items()

        validation.append(sum_all_items)
        
    return validation       

fin = makeTestTrain(data2, 2/3)
print(validateSplit(fin))
# <--------------
