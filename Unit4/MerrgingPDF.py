# mERGE love.pdf and table.pdf
import os
from pypdf import PdfReader, PdfWriter

# Open the existing PDF files
pdf1 = PdfReader("Love.pdf")
pdf2 = PdfReader("table.pdf")

# Create a PDF writer object
pdf_writer = PdfWriter()

# Add the pages from the first PDF
for page_num in range(len(pdf1.pages)):
    page = pdf1.pages[page_num]
    pdf_writer.add_page(page)


# Add the pages from the second PDF
for page_num in range(len(pdf2.pages)):
    page = pdf2.pages[page_num]
    pdf_writer.add_page(page)

# Write the output PDF
with open("merged.pdf", "wb") as out_file:
    pdf_writer.write(out_file)

print("PDFs merged successfully!")