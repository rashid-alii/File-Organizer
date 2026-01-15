import os
import shutil

#folder paths you wwant to organize
FOLDER_PATH = os.getcwd()  # Current working directory

#File type mappings
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
}


# create folders if they don't exist
def create_folders(): # create folders based on file types
    for folder in FILE_TYPES.keys(): # iterate through the keys in FILE_TYPES
        folder_path = os.path.join(FOLDER_PATH, folder) # create the full path for the folder   
        if not os.path.exists(folder_path): # check if the folder already exists
            os.makedirs(folder_path) # create the folder if it doesn't exist


# organize files
for file in os.listdir(FOLDER_PATH): # iterate through the files in the folder
    file_path = os.path.join(FOLDER_PATH, file) # create the full path for the file

    #skip folders
    if os.path.isdir(file_path):
        continue

    # get file extension
    file_ext = os.path.splitext(file)[1].lower() # get the file extension and convert it to lowercase

    # for folder, extensions in FILE_TYPES.items(): # iterate through the FILE_TYPES dictionary
    for folder, extensions in FILE_TYPES.items(): # iterate through the FILE_TYPES dictionary
        if file_ext in extensions: # check if the file extension is in the list of extensions
           shutil.move(file_path, os.path.join(FOLDER_PATH, folder, file)) # move the file to the corresponding folder
           break  # break the loop once the file is moved

print("Files organized successfully ✅") 