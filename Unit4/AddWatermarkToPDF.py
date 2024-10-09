from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_watermark(text, output="watermark.pdf"):
    # Create a watermark PDF with the desired text
    c = canvas.Canvas(output, pagesize=letter)
    c.setFont("Helvetica", 36)
    c.setFillColorRGB(0.6, 0.6, 0.6)  # Light gray color for watermark
    c.saveState()
    c.translate(300, 500)
    c.rotate(45)
    c.drawCentredString(0, 0, text)
    c.restoreState()
    c.save()

def add_watermark(input_pdf, output_pdf, watermark_pdf):
    # Open the input and watermark PDFs
    pdf_reader = PdfReader(input_pdf)
    pdf_writer = PdfWriter()
    watermark = PdfReader(watermark_pdf).pages[0]

    # Add the watermark to each page
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        page.merge_page(watermark)
        pdf_writer.add_page(page)

    # Write the output PDF
    with open(output_pdf, "wb") as out_file:
        pdf_writer.write(out_file)

# Create the watermark PDF
create_watermark("Volim te")

# Add watermark to each page of Love.pdf
add_watermark("Love.pdf", "Love_with_watermark.pdf", "watermark.pdf")

print("Watermark added successfully!")
