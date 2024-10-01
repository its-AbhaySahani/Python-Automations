import os
import sys

def addPrefixToFiles(path, prefix):
    if not os.path.exists(path):
        print("Path does not exist")
        return
    for filename in os.listdir(path):
        old_file_path = os.path.join(path, filename)

        # check if its a file (not a directory)
        if os.path.isfile(old_file_path):
            new_file_path = os.path.join(path, prefix + filename)
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {old_file_path} to {new_file_path}")

# check the funtion



    