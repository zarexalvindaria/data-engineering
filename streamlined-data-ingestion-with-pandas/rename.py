import os
import re

'''
This program replaces the filename of all files 
containing underscore "-" with the '-' dash character.
'''

def rename_files(folder):

    # Replace $folder with the folder name where files are located
    folder = "$folder"

    for count, filename in enumerate(os.listdir(folder)):
        # If the filename contains underscore '_', replace it with '-' dash
        if ("_" in filename):
            count = count + 1
            
            new_file_name = re.sub("_", "-", filename)

            source = f"{folder}/{filename}"
            destination = f"{folder}/{new_file_name}"
            
            os.rename(source, destination)


if __name__ == '__main__':
    rename_files()