import pandas as pd
import os
import re
from functions import *




"""
Load files into dataframe


Required structure:
1, 2, 3: BAD, GOOD, NEUTRAL

{
    file_name: 9.txt
    plain_text: But it does n't leave you with much .
    folder_name: dataset/BAD

    text_id: 9
    tokenized_text: ["but", "it", "doesnt", "leave", "you", "with", "much"]
    input: 1
}


"""
dataset_relative_path = "dataset"
subdir_paths = get_subdir_names_and_files(dataset_relative_path)[0] #[1] would get txt file names

dataframe = get_dataframe_in_subfolders(subdir_paths)
dataframe = get_tokens_id_input_to_dataframe(dataframe, "plain_text", "folder_name", "file_name")
print(dataframe)

# ADD ID
# ADD INPUT (1, 2, 3)