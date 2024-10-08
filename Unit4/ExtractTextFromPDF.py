# extract text from existing pdf i.e., Love.pdf by using pdfReader

import pdfReader
import os

# Open the existing pdf file
pdf_file = open('Love.pdf', 'rb')

# Create a pdf reader object
pdf_reader = pdfReader.PdfFileReader(pdf_file)


# Get the number of pages in the pdf
num_pages = pdf_reader.numPages

# Extract text from each page
for page_num in range(num_pages):
    page = pdf_reader.getPage(page_num)
    text = page.extract_text()
    print(f"Page {page_num + 1}:\n{text}")

# Close the pdf file
pdf_file.close()
print("Text extracted successfully.")
