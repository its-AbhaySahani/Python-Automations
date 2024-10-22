from openpyxl import Workbook

# Create a workbook and select activer worksheet
wb = Workbook()
sheet = wb.active

sheet['A1'] = 10
sheet['A2'] = 20
sheet['A3'] = 30
sheet['A4'] = 40
sheet['A5'] = '=AVERAGE(A1:A4)'
sheet['A6'] = '=SUM(A1:A4)'
sheet['A7'] = '=MAX(A1:A4)'
sheet['A8'] = '=MIN(A1:A4)'

wb.save('ExcelFuntiion.xlsx')



