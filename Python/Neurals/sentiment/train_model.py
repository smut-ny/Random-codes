from re import X
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, f1_score, precision_score
from sklearn.model_selection import train_test_split
import tensorflow as tf




df = pd.read_pickle("processed_dataframe.pkl")

x = np.array(df.iloc[:, 7])
y = np.array(df.iloc[:, 4])


array_of_sentences = []

for array in x:
    array_of_numbers = []
    for number in array:
        array_of_numbers.append(number)
    
    array_of_sentences.append(array_of_numbers)

x = np.array(array_of_sentences)
print(x.shape)

[x_train, x_test, y_train, y_test] = train_test_split(x, y, test_size=0.3, random_state=20 , stratify=y)


def validate_split_test(x_train, x_test, y_train, y_test):
    return ["y_train: ", sum(y_train == 1), sum(y_train == 0), "x_train: ", len(x_train),  "y_test: ", sum(y_test == 1), sum(y_test == 0), "x_test: ", len(x_test)]



print( 

validate_split_test(x_train, x_test, y_train, y_test)

)



def evalML(model, x_train, y_train, x_test, y_test):
    
    print("X_TEST")
    y_pred = model.predict(x_test)
    print(f1_score(y_test, y_pred, average = 'micro'))
    print(precision_score(y_test, y_pred, average='macro'))
    print(classification_report(y_test, y_pred))

    print("X_TRAIN")
    y_pred = model.predict(x_train)
    print(f1_score(y_train, y_pred, average = 'micro'))
    print(precision_score(y_train, y_pred, average='macro'))
    print(classification_report(y_train, y_pred))

def train_ML(x_train, y_train, x_test, y_test):
    # KNN
    from sklearn.neighbors import KNeighborsClassifier
    modelNeigh = KNeighborsClassifier(n_neighbors=3)
    modelNeigh.fit(x_train, y_train)

    # NB
    from sklearn.naive_bayes import GaussianNB
    modelNB = GaussianNB()
    modelNB.fit(x_train, y_train)

    # XGBOOST
    from xgboost import XGBClassifier
    modelBoost = XGBClassifier()
    modelBoost.fit(x_train, y_train)
    
    # SVM
    from sklearn.svm import SVC
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    modelSVM = make_pipeline(StandardScaler(), SVC(gamma='auto'))
    modelSVM.fit(x_train, y_train)

    print("Naive")
    evalML(modelNB, x_train, y_train, x_test, y_test)
    print("KNN")
    evalML(modelNeigh, x_train, y_train, x_test, y_test)
    print("XGBOOST")
    evalML(modelBoost, x_train, y_train, x_test, y_test)
    print("SVM")
    evalML(modelSVM, x_train, y_train, x_test, y_test)


def eval_neural(model, y_train, y_test, x_train, x_test):
    from sklearn.metrics import classification_report
    from sklearn.metrics import confusion_matrix

    print("X_TRAIN")
    y_true = y_train.flatten().tolist()
    y_pred = model.predict_classes(x_train).tolist()
    print(classification_report(y_true, y_pred))
    print(confusion_matrix(y_true, y_pred))

    print("X_TEST")
    y_true = y_test.flatten().tolist()
    y_pred = model.predict_classes(x_test).tolist()
    print(classification_report(y_true, y_pred))
    print(confusion_matrix(y_true, y_pred))              


def train_Neural(x_train, y_train, x_test, y_test):
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten()) #Flattening
    model.add(tf.keras.layers.Dense(300, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(20, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dropout(0.6))
    model.add(tf.keras.layers.Dense(7, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dropout(0.7))
    model.add(tf.keras.layers.Dense(5, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dropout(0.8))
    model.add(tf.keras.layers.Dense(2, activation=tf.nn.sigmoid)) #Output = 2   

    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs = 99)
    
    model.save("trained/model_neural.h5")


    eval_neural(model, y_train, y_test, x_train, x_test)    



def getModels(x_train, y_train, x_test, y_test):
    # train_Neural(x_train, y_train, x_test, y_test)
    train_ML(x_train, y_train, x_test, y_test)





getModels(x_train, y_train, x_test, y_test)



