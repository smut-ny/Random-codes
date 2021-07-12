from __future__ import print_function
from re import X
from tarfile import XGLTYPE
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize


df = pd.read_pickle("processed_dataframe.pkl")


x = np.array(df.iloc[:, 7])
y = np.array(df.iloc[:, 4])


[x_train, x_test, y_train, y_test] = train_test_split(x, y, test_size=0.5, random_state=50)

def validate_split_test(x_train, x_test, y_train, y_test):
    return ["y_train: ", sum(y_train == 1), sum(y_train == 0), "x_train: ", len(x_train),  "y_test: ", sum(y_test == 1), sum(y_test == 0), "x_test: ", len(x_test)]

# x_train = np.array(x_train).reshape(1000, 300)

# from sklearn.naive_bayes import GaussianNB

# model = GaussianNB()
# model.fit(x_train, y_train)
