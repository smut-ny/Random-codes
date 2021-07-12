import pandas as pd
import os
import re
from functions import *



#Create dictionare file structure with data-text info

dataset_relative_path = "dataset"
subdir_paths = get_subdir_names_and_files(dataset_relative_path)[0] #[1] would get txt file names
dataframe = get_dataframe_from_subfolders(subdir_paths)
dataframe = get_custom_columns(dataframe, "plain_text", "folder_name", "file_name") #Main function for adding info into data frame, to add more info manipulate this function



#Convert dictionare into pandas dataframe type
pd_dataframe_bad = pd.DataFrame.from_dict(dataframe[0])
pd_dataframe_good = pd.DataFrame.from_dict(dataframe[1])

df = pd_dataframe_bad.append(pd_dataframe_good, ignore_index = True)

# Remove empty columns (no data)
df = remove_empty_columns(df, "cleaned_text")


# Exports
df.to_csv('processed_dataframe.csv')
df.to_pickle('processed_dataframe.pkl')






