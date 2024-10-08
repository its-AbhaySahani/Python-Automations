import pandas as pd
from fpdf import FPDF

#load the excel file
df = pd.read_excel('Unit4/sample.xls')

# Create a pdf document
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

pdf.set_font("Arial", size=12)

# write the colum headers
for col in df.columns:
    pdf.cell(50, 10, str(col), 1)
pdf.ln()

# write the data
for i in range(len(df)):
    for col in df.columns:
        pdf.cell(50, 10, str(df.iloc[i][col]), 1)
    pdf.ln()

# save the pdf with name .pdf
pdf.output("ExcelToPDF.pdf")

print("PDF created successfully.")