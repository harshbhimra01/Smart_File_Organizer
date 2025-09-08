import os 
import shutil 

# path to the directory.
source_dir = "YOUR PATH TO DIRECTORY"


# listing all the files and folders in source directory.
all_items = os.listdir(source_dir)


# looping through all_items and check each one to organize files.
for item_name in all_items:
    # creating full path to the items.
    item_path = os.path.join(source_dir, item_name)


    # check if it's a files (we don't want to move a folder)
    if os.path.isfile(item_path):
        print(f"Found file: {item_name}") # will help in debugging!

# Imported tools, given path, and scanning files completed.
# Now here goes the logic to organize the files  

# we will split the names of the files to there extentions (.pdf , .jpg etc)
# that way we can decide its folder
# example = pdf files will be in DOC folder and jpg files will be in IMG folder
# so inside the same if os.path.isfile loop
        file_name, file_extension = os.path.splitext(item_name)#this will split the file name into it's base and extension

        file_extension = file_extension.lower() # this will convert all the extentions in lower case

# mapping extention to folder names
        extension_to_folder = {
            '.pdf' : 'DOC',
            '.txt' : 'DOC',
            '.docx' : 'DOC',
            '.jpg' : 'IMG',
            '.png' : 'IMG',
            '.gif' : 'IMG',
            '.jpeg' : 'IMG',
            '.mp4' : 'VIDEO',
            '.mov' : 'VIDEO',
            '.mp3' : 'MUSIC',
            '.aac' : 'MUSIC',
            '.py' : 'CODE',
            '.zip' : 'ARCHIVE',
            '.tar.gz' : 'ARCHIVE',
        }

        # if the extention isn't in our list it will put all them in a folder name Misc.
        destination_folder_name = extension_to_folder.get(file_extension, 'Misc')

        # creating full path for the destination folders
        destination_dir = os.path.join(source_dir, destination_folder_name)

        # creating the destination folder if it doesn't exist
        os.makedirs(destination_dir, exist_ok=True) # this will create folders for the different extentions as we set.

        # have to create a full new path for the files
        new_file_path = os.path.join(destination_dir, item_name)

        # Finally, move the file from its old path to its new path by using shutil
        shutil.move(item_path, new_file_path)
        print(f"Moved: {item_name} -> {destination_folder_name}/")

        # AND BOOM! IT'S COMPLETED!