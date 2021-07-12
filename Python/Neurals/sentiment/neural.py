from __future__ import print_function
from re import X
from tarfile import XGLTYPE
from tkinter import N
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, f1_score, precision_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
import tensorflow as tf
from sklearn.metrics import classification_report




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

[x_train, x_test, y_train, y_test] = train_test_split(x, y, test_size=0.33, random_state=50)


def validate_split_test(x_train, x_test, y_train, y_test):
    return ["y_train: ", sum(y_train == 1), sum(y_train == 0), "x_train: ", len(x_train),  "y_test: ", sum(y_test == 1), sum(y_test == 0), "x_test: ", len(x_test)]

# from sklearn.neighbors import KNeighborsClassifier
# neigh = KNeighborsClassifier(n_neighbors=3)
# neigh.fit(x_train, y_train)

# from sklearn.naive_bayes import GaussianNB
# muj_model = GaussianNB()
# muj_model.fit(x_train, y_train)

# y_pred = muj_model.predict(x_test)


model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten()) #Flattening
model.add(tf.keras.layers.Dense(300, activation=tf.nn.relu))
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.Dense(20, activation=tf.nn.relu))
model.add(tf.keras.layers.Dropout(0.4))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.relu))
model.add(tf.keras.layers.Dropout(0.6))
model.add(tf.keras.layers.Dense(5, activation=tf.nn.relu))
model.add(tf.keras.layers.Dropout(0.8))
model.add(tf.keras.layers.Dense(2, activation=tf.nn.sigmoid)) #Output = 2   

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs = 99)

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

y_true = y_train.flatten().tolist()
y_pred = model.predict_classes(x_train).tolist()
print(classification_report(y_true, y_pred))
print(confusion_matrix(y_true, y_pred))

y_true = y_test.flatten().tolist()
y_pred = model.predict_classes(x_test).tolist()
print(classification_report(y_true, y_pred))
print(confusion_matrix(y_true, y_pred))


# y_pred = neigh.predict(x_test)

# print(f1_score(y_test, y_pred, average = 'micro'))
# print(precision_score(y_test, y_pred, average='macro'))
# print(classification_report(y_test, y_pred))