import pandas as pd
import os
import re
from functions import *



#Create dictionare file structure with data-text info
"""

Required structure:
0, 1: BAD, GOOD

{
    file_name: 9.txt
    plain_text: But it does n't leave you with much .
    folder_name: dataset/BAD

    text_id: 9
    tokenized_text: ["but", "it", "doesnt", "leave", "you", "with", "much"]
    input: 1
}<


"""

dataset_relative_path = "dataset"
subdir_paths = get_subdir_names_and_files(dataset_relative_path)[0] #[1] would get txt file names
dataframe = get_dataframe_from_subfolders(subdir_paths)
dataframe = get_custom_columns(dataframe, "plain_text", "folder_name", "file_name") #Main function for adding info into data frame, to add more info manipulate this function



#Convert dictionare into pandas dataframe type
pd_dataframe_bad = pd.DataFrame.from_dict(dataframe[0])
pd_dataframe_good = pd.DataFrame.from_dict(dataframe[1])

df = pd_dataframe_bad.append(pd_dataframe_good, ignore_index = True)
print(df)




