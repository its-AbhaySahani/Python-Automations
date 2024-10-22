# read conetent in newfile.txt
with open("newfile.txt", "r") as file:
    # read the content of the file
    content = file.read()
    # print the content
    print(content)