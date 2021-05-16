import pandas as pd
import os
from functions import *

dataset_relative_path = "dataset"



"""
Load files into dataframe


Required structure:
1, 2, 3: BAD, GOOD, NEUTRAL

{
    text_id: 9
    text: But it does n't leave you with much .
    input: 1
}

"""
subdir_paths = get_subdir_names_and_files(dataset_relative_path)[0]
dataframe = get_dataframe_from_folders(subdir_paths)

print(dataframe)