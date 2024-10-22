# open a new file in write mode
with open("newfile.txt", "w") as file:
    # write some lines of text
    file.write("Hello World\n")
    file.write("This is our new text file\n")
    file.write("and this is another line.\n")
    file.write("Why? Because we can.\n")
    # close the file

print("File created and content added successfully")