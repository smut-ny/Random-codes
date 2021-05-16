import os

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

    file_info = []

    for filename in os.listdir(folder):
        file = {}
        file["file_path"] = filename
        with open(os.path.join(folder, filename), 'r') as f:
            file["plain_text"] = f.read()
            file_info.append(file)
            
    
    return file_info


def get_dataframe_from_folders(rel_path_list):
    dataframe = []

    for folder in rel_path_list:
        dataframe.append(get_dataframe(folder))
    
    return dataframe
