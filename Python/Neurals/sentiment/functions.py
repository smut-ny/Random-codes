import os
from pyexpat import model
import re
import pandas as pd
from sqlite3 import DatabaseError
from bleach import clean
import spacy

nlp = spacy.load("en_core_web_sm")

def remove_empty_lists(list_data):
   return [ele for ele in list_data if ele != []]


def get_subdir_name_alt(relative_path):
    dirs = [folder[1] for folder in os.walk(relative_path)]

    return remove_empty_lists(dirs)


def get_subdir_names_and_files(relative_path):
    subdir_names = []
    subdir_file = []

    for root, dirs, files in os.walk(relative_path):

        for name in files:
            subdir_names.append(os.path.join(root, name))

        for name in dirs:
            subdir_file.append(os.path.join(root, name))
    
    return subdir_file, subdir_names


def get_dataframe(folder):
    dataframe = []

    for filename in os.listdir(folder):
        file = {}
        file["folder_name"] = folder
        file["file_name"] = filename
        if ".txt" in filename: #In order to ignore DS.Store and other trash/non txt files
            with open(os.path.join(folder, filename), 'r') as f:
                    file["plain_text"] = f.read()
                    dataframe.append(file)
                
    return dataframe


def get_dataframe_from_subfolders(rel_path_list):
    dataframe = []

    for folder in rel_path_list:
        dataframe.append(get_dataframe(folder))
    
    return dataframe

def get_tokenized_list(plain_text): #Alternative tokenizer
    word = []
    word = re.split('\W+', plain_text.lower())
    word = list(filter(None, word))

    return word

def get_target_value(folder_name):
    if folder_name == "dataset/BAD":
        return 0
    elif folder_name == "dataset/GOOD":
        return 1
    else:
        return 2

def del_filename_extension(filename, extension):
    return re.sub(extension, "", filename)

def lemmatize_and_remove_punct_stops(text):
    
    doc = nlp(text)

    tokenized_text = []
    remove_trash = ['\n', '`', 've', '-LRB-', '-RRB-', '-rrb-']

    for token in doc:
        if not token.is_punct and not token.is_stop and token.lemma_ not in remove_trash:
            tokenized_text.append(token.lemma_)
    return tokenized_text

def get_custom_columns(dataframe, plain_text_key, folder_key, filename_key):
    for data_block in dataframe:
        for data in data_block:
            data["cleaned_text"] = lemmatize_and_remove_punct_stops(data[plain_text_key]) #Main Spacy pipeline function
            data["input"] = get_target_value(data[folder_key])
            data["text_id"] = del_filename_extension(data[filename_key], ".txt")

    return dataframe

        