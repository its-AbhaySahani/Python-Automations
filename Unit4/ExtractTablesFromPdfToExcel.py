# create a pdf that conatains table and then extract the table from the pdf and save it to an new excel file
import pdfreader
import os
import pandas as pd
from tabula import read_pdf
from tabula import convert_into
from pypdf import PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_table_pdf(output="table.pdf"):
    # Create a PDF with a table
    c = canvas.Canvas(output, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, "Name")
    c.drawString(200, 750, "Age")
    c.drawString(300, 750,  "City")
    c.drawString(100, 700, "Abhay")
    c.drawString(200, 700, "21")
    c.drawString(300, 700, "Mumbai")
    c.drawString(100, 650, "Aman")
    c.drawString(200, 650, "24")
    c.drawString(300, 650, "GorakhPur")
    c.save()

def extract_table(input_pdf, output_excel):
    # Extract table from PDF and save it to an Excel file
    tables = read_pdf(input_pdf, pages="all")
    for i, table in enumerate(tables):
        table.to_excel(f"table_{i}.xlsx", index=False)

# Create a PDF with a table
create_table_pdf()

# Extract the table from the PDF and save it to an Excel file
extract_table("table.pdf", "table.xlsx")

print("Table extracted successfully!")