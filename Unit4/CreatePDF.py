from fpdf import FPDF

# Create a pdf document
pdf = FPDF()

# Add a page
pdf.add_page()

# set title
pdf.set_title("Hey Honey")

# set font
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Welcome to the world of Love", ln=True, align='C')

# add a line break
pdf.ln(10)
pdf.cell(200, 10, 'This is the story of my love.', ln = True)
pdf.cell(200, 10, 'Just Kidding.', ln=True)

# save the pdf with name .pdf
pdf.output("Love.pdf")

print("PDF created successfully.")