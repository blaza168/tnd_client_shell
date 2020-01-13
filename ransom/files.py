import os

interesting_extensions = ['.jpg', '.png', '.jpeg', # images
                          '.doc', '.docx', '.txt']  # documents

# This function goes throw everything in root path and return every interesting file
def find_files(starting_path):
    for current_path, directories, files_found in os.walk(starting_path):
        for arq in files_found:
            file_extension = os.path.splitext(os.path.join(current_path, arq))[1].lower()
            if(file_extension in interesting_extensions or file_extension == ''):
                yield os.path.join(current_path, arq).encode()
