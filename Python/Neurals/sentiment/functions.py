import os
import re


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

        with open(os.path.join(folder, filename), 'r') as f:
            file["plain_text"] = f.read()
            dataframe.append(file)
            
    return dataframe


def get_dataframe_in_subfolders(rel_path_list):
    dataframe = []

    for folder in rel_path_list:
        dataframe.append(get_dataframe(folder))
    
    return dataframe

def get_tokenized_list(plain_text):
    word = []
    word = re.split('\W+', plain_text.lower())
    word = list(filter(None, word))

    return word

def get_target_value(folder_name):
    if folder_name == "dataset/BAD":
        return 1
    elif folder_name == "dataset/GOOD":
        return 2
    else:
        return 3

def del_filename_extension(filename, extension):
    return re.sub(extension, "", filename)

def get_tokens_id_input_to_dataframe(dataframe, plain_text_key, folder_key, filename_key):
    for data_block in dataframe:
        for data in data_block:
            data["tokenized_text"] = get_tokenized_list(data[plain_text_key])
            data["input"] = get_target_value(data[folder_key])
            data["text_id"] = del_filename_extension(data[filename_key], ".txt")

    return dataframe