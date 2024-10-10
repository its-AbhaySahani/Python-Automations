# write a python code to read Sample_CSV.csv file and print the content of the file
import csv
with open('Unit 5\Sample_CSV.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

