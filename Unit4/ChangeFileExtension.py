import os
import shutil

def change_file_extension(file_name, new_extension):
    # Split the file name and extension
    base_name, _ = os.path.splitext(file_name)
    new_file_name = base_name + new_extension
    try:
        shutil.move(file_name, new_file_name)
        print(f"File extension changed from {file_name} to {new_file_name}")
    except FileNotFoundError:
        print(f"File {file_name} not found.")

def main():
    # Specify the file name and the new extension
    file_name = 'Unit4/mypic.jpeg'  # Replace with your file name
    new_extension = '.png'  # Replace with the new extension

    # Change the file extension
    change_file_extension(file_name, new_extension)

if __name__ == '__main__':
    main()