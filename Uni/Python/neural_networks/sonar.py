import pandas as pd

# 1) načíst data
df = pd.read_csv('Uni/Python/neural_networks/sonar.csv', header=None)

# 2) přepsat R a M na 0 a 1
df.loc[:, "MineZeroOne"] = df.iloc [:, 60] == "R"
df.loc[:, "MineZeroOne"] = df.loc [:, "MineZeroOne"].astype(int)

df = df.drop(columns=[60])

# 3) získat vlastnosti a labely
x = df.iloc[:, 0:60]
y = df.iloc[:, 60]

# 4) rozdělit na trenovaci a testovaci dataset
from sklearn.model_selection import train_test_split

# Kontrolovat jestli jsou data y_train v poměru!
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=50)


def normalize_column(column):
    mean = column.mean()
    sd = column.std()

    normalized_column (column - mean)/sd 
    return normalized_column, mean, sd   