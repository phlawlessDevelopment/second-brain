import os

for (dirpath, folder_names, files) in os.walk(os.path.curdir):
    for filename in files:
        if '.md' not in filename:
            continue
        file_location = dirpath + '/' + filename  #file location is location is the location of the file
        if os.path.isfile(file_location):
            if os.path.getsize(file_location) == 0:#Checking if the file is empty or not
                os.remove(file_location)  #If the file is empty then it is deleted using remove method